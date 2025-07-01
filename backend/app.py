from flask import jsonify,render_template,Flask,Response
from keras.models import load_model
import cv2
import numpy as np
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

model = load_model('best_model.h5')

classes = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

camera = None
streaming = False

def preproccess_frame(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray,(48,48))
    normalized = resized/255.0
    reshaped = np.reshape(normalized,(1,48,48,1))
    return reshaped

def generate_frames():

    global camera, streaming

    streaming=True

    while streaming:

        success,frame = camera.read()

        if not success:
            break

        input_data = preproccess_frame(frame)

        prediction = model.predict(input_data)
        label = classes[np.argmax(prediction)]


        cv2.putText(frame,f"Emotion :{label}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        ret,buffer = cv2.imencode('.jpg',frame)
        frame_bytes=buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    
    if camera is not None:
        camera.release()
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop')
def stop():
    global streaming,camera

    streaming=False
    if camera is not None:
        camera.release()
        camera=None
    return jsonify({'message':'Camera stopped!'})


@app.route('/start')
def start():
    global streaming,camera

    if not streaming:

        streaming=True
        camera=cv2.VideoCapture(0)
    return jsonify({'message':'Camera started'})

if __name__ == '__main__':
    app.run(debug=True)