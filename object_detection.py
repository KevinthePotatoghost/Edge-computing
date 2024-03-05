import torch
import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# OpenCV capture for camera stream
cap = cv2.VideoCapture(0)  # Change 0 to the camera index if you have multiple cameras

# Create Tkinter window
root = tk.Tk()
root.title("Object Detection with YOLOv5")

# Create a label to display the video stream
label = tk.Label(root)
label.pack()

def update():
    ret, frame = cap.read()

    if ret:
        # Inference
        results = model(frame)

        # Draw bounding boxes on the frame
        frame_with_boxes = results.render()[0]

        # Convert OpenCV image to ImageTk format
        img = cv2.cvtColor(frame_with_boxes, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img_tk = ImageTk.PhotoImage(image=img)

        # Update label with the new image
        label.img = img_tk
        label.config(image=img_tk)

    # Schedule the update function to be called after 10 milliseconds
    root.after(1, update)

# Call the update function to start the video stream
update()

# Run the Tkinter event loop
root.mainloop()

# Release the capture when the Tkinter window is closed
cap.release()