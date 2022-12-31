from flask import Flask, render_template, request
import numpy as np
import pickle
import requests
import ml

app = Flask(__name__)


@app.route("/", methods= ["GET","POST"])
def hello():
    movie=[]
    movie_detail=[]
    moviename=[]
    movie_l=ml.getallmovie()
    if request.method == "POST":
       selectedmovie = request.form['selectedmovie']
       totalmovie = ml.recommend(selectedmovie)
       movie_detail= totalmovie
      
    return render_template('index.html', rm=movie_detail, moviel=movie_l)

if __name__ == "__main__":
    app.run(debug=False)