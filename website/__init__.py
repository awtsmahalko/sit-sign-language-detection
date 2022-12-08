from flask import Flask,Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import secure_filename
import cv2

db = SQLAlchemy()
global camera

def create_app():
    app = Flask(__name__)
    camera=cv2.VideoCapture(0)
    CORS(app)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    # NOTE: if password is present : 'mysql://user:password@host/database'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/sld_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
    db.init_app(app)

    from .views import views
    #from .detect import detect

    app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(detect, url_prefix='/')

    from .models import User

    return app

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