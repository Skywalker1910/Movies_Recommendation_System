from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd
from utils import recommend_content, recommend_collaborative

app = Flask(__name__)

# Load data and models
movies = pd.read_csv('data/movies_metadata.csv', low_memory=False)
with open('models/content_model.pkl', 'rb') as f:
    content_sim = pickle.load(f)
with open('models/collaborative_model.pkl', 'rb') as f:
    collaborative_model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/rate', methods=['POST'])
def rate():
    user_rating = request.form
    # Save user ratings, for simplicity, append to a local CSV file
    # In a production scenario, you may use a database here.
    return redirect(url_for('recommendations'))

@app.route('/recommendations')
def recommendations():
    recommendations = recommend_content(content_sim, movies, 5)  # Example recommendation
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)