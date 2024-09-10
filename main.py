from flask import Flask, render_template, redirect, url_for, jsonify, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "harrypotter"

app.run(debug = True)