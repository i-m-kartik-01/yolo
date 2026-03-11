import cv2
import time
from flask import Flask, render_template, Response
from ultralytics import YOLO

app = Flask(__name__)

# Load your custom YOLO model
model = YOLO("runs/detect/train13/weights/best.pt")

def generate_frames():
    start_time = time.time()
    while True:
        success, frame = cv2.VideoCapture(0).read() # Using webcam
        if not success:
            break
        else:
            # Run YOLO detection
            results = model.predict(source=frame, conf=0.5, save=False)
            
            # Annotated frame
            annotated_frame = results[0].plot()
            
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()

            # Yield the output frame in the byte format required for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    # This renders the dashboard
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # This is the route for the live stream
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)