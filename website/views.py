from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import json
from werkzeug.utils import secure_filename
import os

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({ "result": "this is home" })
    # return render_template("home.html", user=current_user)