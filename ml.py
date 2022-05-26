import pickle
from telnetlib import STATUS
# from typing_extensions import runtime
from numpy import full
import requests
  

def fetch_detail(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json() 
 
    moviedetail=[]
    
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    full_path_details = "https://image.tmdb.org/t/p/w500/" + poster_path
    moviedetail.append({
        "title":data['title'],
        "movieoverview":data['overview'],
        'poster_path':data['poster_path'],
        'moviereleasedate':data['release_date'],
          'movierating' : data['vote_average'],
    'movierevenue' : data['revenue'],
    'moviehomepagelink' : data['homepage'],
    'moviebudget' : data['budget'],
    'movieruntime' : data['runtime'],
    "full_path":full_path,
    "full_path_details":full_path_details
    })

    return moviedetail

  
 
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    totalmovie=[]
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        moviedetail = fetch_detail(movie_id)
        totalmovie.append({"moviedetail":moviedetail})
    return  totalmovie


def getallmovie():
    movie_list = movies['title'].values
    return movie_list


movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
