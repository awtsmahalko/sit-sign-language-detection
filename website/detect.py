from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, Response
from werkzeug.utils import secure_filename
import cv2
import os

detect = Blueprint('detect', __name__)

camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            print("not");
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@detect.route('/detects', methods=['GET', 'POST'])
def detects():
    return render_template("views/detect.html")

@detect.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
