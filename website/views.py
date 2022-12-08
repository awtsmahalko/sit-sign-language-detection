from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, Response
from . import generate_frames
import json
from werkzeug.utils import secure_filename
import os

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({ "result": "this is home" })
    # return render_template("home.html", user=current_user)

@views.route('/detects', methods=['GET', 'POST'])
def detects():
    return render_template("views/detect.html")

@views.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')