### Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Scikit-learn, and Streamlit. The system recommends movies similar to the selected movie based on their features such as genres, keywords, cast, crew, and overview. Movie posters are fetched dynamically using the TMDB API.

### Project Structure

CineMatch/
│
├── app/
│   └── app.py                        #Main Streamlit application


├── models/
│   ├── movies.pkl                    # Preprocessed movie DataFrame

│   └── similarity.pkl                # Cosine similarity matrix (can be large!)


├── notebooks/
│   └── movie_recommender.ipynb       # Data preprocessing & model building


├── data/                             # Raw csv files
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv


├── requirements.txt                  #  Python dependencies
├── .env                              # Environment variable template
├── .gitignore
└── README.md

### Features

-> Recommend movies based on content similarity.
-> Interactive web interface using Streamlit.
-> Displays movie posters using TMDB API.
-> Fast recommendations using Cosine Similarity.
-> User-friendly dropdown for movie selection.

### Tech Stack Used

Python
Pandas
NumPy
Scikit-learn
Streamlit
TMDB API
Joblib

### Demos
![Demo First](screenshots/demo1.png)


![Demo Second](screenshots/demo2.png)


![Selectbox](screenshots/demo3.png)


### Future Improvements
-> Collaborative Filtering Recommendation System
-> Hybrid Recommendation System
-> User Authentication
-> Search by Actor or Genre
-> Movie Ratings and Reviews

### To run locally on your device

-> Clone the repository:

git clone https://github.com/AayushAcharya12/Movie-Recommendation-System.git

-> Move into the project directory:

cd Movie-Recommendation-System

-> Install dependencies:

pip install -r requirements.txt

-> Run the Streamlit app:

streamlit run App/app.py

