# CPSC 8740 A.I Receptive Software Engineering
# Final Project | Aditya More | CU-ID – C97857734
# Movie Recommendation System

This project is a **Movie Recommendation System** that provides personalized movie recommendations based on content-based and collaborative filtering techniques. It uses a Flask web application to enable users to rate movies and view recommendations.

---

## Features
1. **Content-Based Filtering**: Recommends movies similar to the ones the user has rated highly.
2. **Collaborative Filtering**: Provides recommendations based on similar user preferences.
3. **Interactive Web UI**: Users can rate movies and view recommendations through an intuitive interface.
4. **Trained Models**: Models for content-based and collaborative filtering are trained and stored externally.

---

## Requirements
- Python 3.8 or higher
- Web browser to access the Flask app

---

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/Skywalker1910/Movies_Recommendation_System
cd movies-recommendation-system
```
### 2. Download trained Models:
- The trained models were large in size and are hosted on OneDrive. Download them using the link below:

<[Trained_Models](https://clemson-my.sharepoint.com/:f:/g/personal/more_clemson_edu/EuddtKH1EhtCu06fAQ8Et-IBUA4Ty0w24mTqzSAxB0UJuA?e=LseOHA)>

- Place the downloaded models in the models/ directory of the project:

models/
├── content_model.pkl       # Content-based filtering model
├── collaborative_model.pkl # Collaborative filtering model

### 3. Install Dependencies
- Create a virtual environment and install the required Python packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```
### 4. Data
- Ensure the required datasets are in the data/ directory:

data/movies_metadata.csv
data/ratings_small.csv


## Run the Application

### 1. Start the Flask server:
```bash
python app.py
```
### 2. Open a web browser and navigate to http://127.0.0.1:5000.

## How to Use
### 1. Homepage:
- Browse the list of movies.
- Rate movies using the provided sliders.
### 2. Submit Ratings:
- Click on the "Submit Ratings" button to save your ratings.
### 3. View Recommendations:
- After submitting ratings, view personalized movie recommendations.


## File Structure 
```graphql
movies-recommendation-system/
│
├── app.py                  # Flask app to run the web server
├── data/
│   ├── movies_metadata.csv # Dataset containing movie metadata
│   ├── ratings_small.csv   # Dataset containing user ratings
├── models/
│   ├── content_model.pkl   # Trained content-based model
│   ├── collaborative_model.pkl # Trained collaborative filtering model
├── static/
│   ├── style.css           # CSS file for styling
│   └── app.js              # JavaScript for interactivity
├── templates/
│   ├── index.html          # Homepage
│   ├── recommendations.html # Recommendations page
├── requirements.txt        # Python dependencies
├── data_preparation.py     # Script for data cleaning and preparation
├── model.py                # Script for building models
└── utils.py                # Helper functions
```

## Troubleshooting
### 1. Missing Dependencies:

 - Ensure you have installed all required packages using pip install -r requirements.txt.

### 2. Model File Missing:

- Verify that the pre-trained models are downloaded and placed in the models/ directory.

### 3. Dataset Missing:

- Check that the required datasets are available in the data/ directory.

### 4. Server Not Running:

- Confirm that Python 3.8 or higher is installed, and all dependencies are correctly set up.

