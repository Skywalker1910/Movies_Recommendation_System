import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle
from data_preparation import load_and_clean_data

def build_content_model(movies):
    # Content-based recommendation using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    movies['overview'] = movies['overview'].fillna('')
    tfidf_matrix = tfidf.fit_transform(movies['overview'])

    # Compute cosine similarity
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Save the model
    with open('models/content_model.pkl', 'wb') as f:
        pickle.dump(cosine_sim, f)

    return cosine_sim

def build_collaborative_model(ratings):
    from surprise import SVD
    from surprise import Dataset, Reader
    from surprise.model_selection import train_test_split
    from surprise import accuracy

    # Load the data into Surprise
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2)

    # Train the model (Collaborative Filtering with SVD)
    algo = SVD()
    algo.fit(trainset)

    # Evaluate and save model
    predictions = algo.test(testset)
    accuracy.rmse(predictions)

    with open('models/collaborative_model.pkl', 'wb') as f:
        pickle.dump(algo, f)

    return algo

if __name__ == '__main__':
    movies, ratings = load_and_clean_data()
    build_content_model(movies)
    build_collaborative_model(ratings)