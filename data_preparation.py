import pandas as pd
import numpy as np

def load_and_clean_data():
    # Load the data
    movies = pd.read_csv('data/movies_metadata.csv', low_memory=False)
    ratings = pd.read_csv('data/ratings_small.csv')

    # Data cleaning (Drop NaN, handle missing values, convert columns as needed)
    movies = movies.dropna(subset=['title', 'overview'])
    ratings = ratings.dropna()

    # Select relevant columns
    movies = movies[['id', 'title', 'overview', 'genres']]
    ratings = ratings[['userId', 'movieId', 'rating']]

    return movies, ratings

if __name__ == '__main__':
    movies, ratings = load_and_clean_data()