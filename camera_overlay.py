import cv2
import numpy as np
from detector import get_detection

cap = cv2.VideoCapture(0)

t = 0

def draw_human(frame, alpha=1.0):
    h, w = frame.shape[:2]
    cx, cy = w // 2, h // 2 - 50
    color = (0, int(255 * alpha), 0)

    cv2.circle(frame, (cx, cy - 60), 25, color, 2)
    cv2.line(frame, (cx, cy - 35), (cx, cy + 80), color, 2)
    cv2.line(frame, (cx - 50, cy), (cx + 50, cy), color, 2)
    cv2.line(frame, (cx, cy + 80), (cx - 40, cy + 140), color, 2)
    cv2.line(frame, (cx, cy + 80), (cx + 40, cy + 140), color, 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected, distance = get_detection()

    # scan lines
    for y in range(0, frame.shape[0], 4):
        cv2.line(frame, (0, y), (frame.shape[1], y), (0, 255, 0), 1)

    if detected:
        pulse = 0.6 + 0.4 * np.sin(t / 10)
        draw_human(frame, pulse)
        cv2.putText(frame, f"Detected | {distance}",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Scanning...",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0, 255, 0), 2)

    cv2.imshow("Wi-Fi Vision Demo", frame)
    t += 1

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
