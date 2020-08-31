from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import cv2
from werkzeug.utils import secure_filename
import socket

app = Flask(__name__)

from services import upload_services, yolo_door_services

cors = CORS(app)
UPLOAD_FOLDER = "inputs"
result_folder = "\\result"
ALLOWED_EXTENSIONS = {'jpg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = result_folder
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
classes = ["door"]


@app.route('/test/')
def test():
    # Python Program to Get IP Address




    return 'Connection Success'


@app.route('/image', methods=['GET','POST'])
def image():
    response = {}
    try:
        if request.method == 'POST':
            file = request.files['file']
            print("file received")
            fileName = upload_services.file_save(file)
            img = (UPLOAD_FOLDER + "/"+ fileName)
            print("File saved")
            print("Sending to yolo detection")
            width,height,result_image = yolo_door_services.door_yolo(fileName,img, classes)
            response = {
                'width':width,
                'height': height,
                'status':"Success"
            }
            result_directory = str(result_folder+"\"" + fileName)
            print(result_directory)

    except Exception as e:
        print(e)
        response = {
            'object': None,
            'status': "ERROR",
            'message': str(e)
        }

    #return jsonify(response), 400 if response['status'] == "ERROR" else 200
    return send_file('result/door.jpg',attachment_filename=fileName) or jsonify(response), 400 if response['status'] == "ERROR" else 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
