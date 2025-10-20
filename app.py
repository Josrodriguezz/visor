from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import numpy as np

app = Flask(__name__)
model = YOLO('yolov8n.pt')

# Mapeo de materiales reciclables por defecto (puedes ajustar según tu dataset personalizado)
MATERIALES = {
    39: 'Botella',
    # Puedes agregar más clases si tienes un modelo personalizado
}

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        results = model(frame, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = MATERIALES.get(cls, model.names[cls])
                material = "Desconocido"
                if cls == 39:  # Botella
                    # Recorte de la botella
                    bottle_roi = frame[y1:y2, x1:x2]
                    if bottle_roi.size > 0:
                        # Convertir a HSV para análisis de color
                        hsv = cv2.cvtColor(bottle_roi, cv2.COLOR_BGR2HSV)
                        # Calcular histograma de saturación
                        sat = hsv[:,:,1]
                        mean_sat = np.mean(sat)
                        # Heurística simple:
                        # - Baja saturación: vidrio
                        # - Alta saturación: plástico
                        # - Muy oscuro: metal
                        # - Muy claro: papel (poco probable en botellas)
                        mean_val = np.mean(hsv[:,:,2])
                        if mean_val < 60:
                            material = "Metal"
                        elif mean_sat < 40:
                            material = "Vidrio"
                        elif mean_sat > 100:
                            material = "Plástico"
                        else:
                            material = "Desconocido"
                    label = f"Botella ({material}) {conf:.2f}"
                    color = (0, 255, 0) if material == "Plástico" else (255, 255, 0) if material == "Vidrio" else (192,192,192) if material == "Metal" else (255,0,255)
                else:
                    color = (255, 0, 255)
                    label = f"{label} {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
