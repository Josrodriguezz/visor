🎯 Sistema de Detección de Objetos y Materiales Reciclables
Sistema de visión por computadora que detecta objetos en tiempo real, identifica materiales reciclables y reconoce gestos de manos usando YOLOv8 y OpenCV.
## 📁 Estructura del Proyecto

Visor/
├── 📁 .vscode/
│   └── settings.json                 # Configuración de VS Code
├── 📁 detector_object_yolo11.v1i.yolov11/
│   ├── 📁 test/
│   │   ├── 📁 images/               # Imágenes de prueba
│   │   └── 📁 labels/               # Etiquetas de prueba
│   ├── 📁 train/                    # Datos de entrenamiento
│   ├── 📁 valid/                    # Datos de validación
│   ├── data.yaml                    # Configuración del dataset
│   └── README.roboflow.txt          # Información de Roboflow
├── 📁 visor-1/
│   ├── 📁 env/                      # Entorno virtual
│   ├── 📁 runs/                     # Resultados de entrenamiento
│   └── 📁 static/                   # Archivos estáticos
├── 📁 templates/
│   └── index1.html                  # Plantilla HTML
├── .gitignore                       # Archivos ignorados por Git
├── app.py                           # Aplicación Flask principal
├── index1.html                      # Interfaz web alternativa
├── reciclaje.yaml                   # Configuración YAML para reciclaje
├── requirements.txt                 # Dependencias del proyecto
├── visor.py                         # Detector de manos
├── visor3.py                        # Detector de objetos mejorado
└── yolov8n.pt                       # Modelo YOLOv8 preentrenado

## ✨ Características
🌐 Aplicación Web Flask (app.py)
Servidor web con streaming en tiempo real

Detección de materiales reciclables

Clasificación de botellas por material (plástico, vidrio, metal)

Interfaz web integrada

## 🔍 Detección de Objetos (visor3.py)
Detección en tiempo real usando YOLOv8

Soporte para modelo personalizado YOLOv11

Múltiples clases de objetos

Bounding boxes y scores de confianza

## 👋 Detección de Manos (visor.py)
Reconocimiento de gestos y dedos

Detección de múltiples manos

Usa MediaPipe para tracking

## 🎯 Modelo Personalizado YOLOv11
Dataset: detector_object_yolo11.v1i.yolov11

Entrenado con Roboflow

Configuración en data.yaml

Modelos para entrenamiento, validación y prueba

## 🛠️ Instalación
Prerrequisitos
Python 3.12.10+

Webcam funcionando

4GB RAM mínimo

## Crear entorno virtual
python -m venv env    
.\env\Scripts\Activate   

## Instalar dependencias
📋 Dependencias
requirements.txt
flask==2.3.3
opencv-python==4.8.1.78
ultralytics==8.0.186
numpy>=1.26.0
cvzone==1.5.6
torch>=2.1.0
torchvision>=0.16.0
Pillow>=10.0.0
mediapipe==0.10.14

pip install -r requirements.txt

## 🌐 Aplicación Web Principal
python app.py

## 🔍 Detección de Objetos Mejorada
python visor3.py

## 👋 Detección de Manos
python visor.py

## 🎯 Usar Modelo Personalizado YOLOv11
Modifica los archivos para apuntar al modelo personalizado:
model = YOLO('detector_object_yolo11.v1i.yolov11/weights/best.pt')

## ⚙️ Configuración
Archivos de Configuración
reciclaje.yaml - Configuración para clasificación de materiales

data.yaml - Configuración del dataset YOLOv11

.vscode/settings.json - Configuración del editor

Personalización
Agregar nuevas clases: Editar reciclaje.yaml

Modificar modelo: Actualizar rutas en los scripts

Ajustar confianza: Modificar parámetros en las detecciones

🎮 Controles
Aplicaciones de escritorio: Presiona 
