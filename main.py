import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Camera not found")
    raise SystemExit

while True:
    ok, frame = cap.read()
    if not ok:
        break
    results = model(frame, verbose=False)
    vehicle_count = 0
    for b in results[0].boxes:
        cls = int(b.cls[0])
        if cls in [2,3,5,7]:
            vehicle_count += 1
    frame = results[0].plot()
    cv2.putText(frame,f"Vehicle Count: {vehicle_count}",(20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("AI Traffic Management", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()