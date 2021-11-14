from flask import Flask, jsonify, request
import csv

all_movies = []

with open('movies.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch_movies = []
popular_movie = []
recommended_movie = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    }) 

@app.route("/liked-movie", methods = ['POST'])
def liked_movie():
    movie = all_movies[0]
    allMovies = all_movies[1:]
    liked_movie.append(movie)
    
    return jsonify({
        "status": "success"
    
    }), 201 

@app.route("/unliked-movie", methods = ['POST'])
def unliked_movie():
    movie = all_movies[0]
    allMovies = all_movies[1:]
    unliked_movie.append(movie)
    
    return jsonify({
        "status": "success"
    
    }), 201 

@app.route("/notwatch-movie", methods = ['POST'])
def notwatch_movie():
    movie = all_movies[0]
    allMovies = all_movies[1:]
    notwatch_movie.append(movie)
    
    return jsonify({
        "status": "success"
    
    }), 201 

@app.route("/popular-movie", methods = ['POST'])
def notwatch_movie():
    movie = all_movies[0]
    allMovies = all_movies[1:]
    popular_movie.append(movie)
    
    return jsonify({
        "status": "success"
    
    }), 201

@app.route("/recommended-movie", methods = ['POST'])
def notwatch_movie():
    movie = all_movies[0]
    allMovies = all_movies[1:]
    recommended_movie.append(movie)
    
    return jsonify({
        "status": "success"
    
    }), 201 

if __name__ == "__main__":
    app.run()