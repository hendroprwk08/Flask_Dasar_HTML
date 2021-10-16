#render_template untuk render halaman HTML)
from flask import Flask, render_template

app = Flask(__name__)

#route 
@app.route('/')
def index():
    #return 'hello test!'
    return render_template("index.html")

@app.route('/profil')
def profil():
    return render_template("profil.html")

@app.route('/kontak')
def kontak():
    return render_template("kontak.html")