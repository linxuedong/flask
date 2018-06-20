from flask import Flask
from . import exercise

app = Flask(__name__)
app.register_blueprint(exercise.simple_page)
