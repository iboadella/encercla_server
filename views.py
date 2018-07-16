from run import app
from flask import jsonify,render_template,send_from_directory
import requests

@app.route('/')
def serve_index():
     return send_from_directory('./dist', 'index.html')

