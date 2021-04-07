 
import pandas as pd
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    

    @app.route('/')
    def root():
        return render_template('base.html')

