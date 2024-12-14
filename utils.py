import pandas as pd

def recommend_content(cosine_sim, movies, num_recommendations=10):
    # Dummy content-based recommendation function for demo
    recommendations = movies[['title']].head(num_recommendations)
    return recommendations

def recommend_collaborative(collaborative_model, user_id, num_recommendations=10):
    # Dummy collaborative recommendation function for demo
    return []