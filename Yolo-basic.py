print("------ OBJECT DETECTION With YOLO v8")
from ultralytics import YOLO
import cv2

model = YOLO("Yolo-Weights/yolov8n.pt")

results = model("DECOC.jpg", show=True)

cv2.waitKey(0)