#!/usr/bin/env python3
#app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    """An implementation of a simple greet function"""
    return "Hello, World!"
