"""Módulo para detección de manos en tiempo real usando OpenCV y cvzone.

Este script captura video de la cámara web, detecta manos y muestra
qué dedos están levantados en cada mano detectada.
"""

import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector


def main():
    """Función principal para la detección de manos."""
    # Verificar versiones
    print(f"NumPy: {np.__version__}")
    print(f"OpenCV: {cv2.__version__}")  # Versión directa del módulo

    # Inicializar detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)
    cap = cv2.VideoCapture(0)  # pylint: disable=no-member

    try:
        while True:
            success, img = cap.read()
            if not success:
                break

            # Detección de manos
            hands, img = detector.findHands(img)

            # Mostrar información
            if hands:
                for hand in hands:
                    fingers = detector.fingersUp(hand)
                    print(f"Dedos detectados: {fingers}")

            cv2.imshow("Detección de Manos", img)  # pylint: disable=no-member
            if cv2.waitKey(1) & 0xFF == ord('q'):  # pylint: disable=no-member
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()  # pylint: disable=no-member


if __name__ == "__main__":
    main()
