# Movie-Matrix 🎬

_Movie Recommendation System_

A movie suggestion from the server-based system has made discovering a good movie much easier these days. Movie recommendations assist cinephiles and movie fans by proposing top-tier films to watch without wasting time searching through large databases. To solve this problem, I propose a content-based model that will use Python-based Machine Learning algorithms to analyse large datasets and generate a movie recommendation.

**Movie Matrix** is a web application which recommends similar movies to a movie the user likes.

# Table of content:
1. [About dataset](#data)
2. [Architecture](#arch)
3. [Tech stack](#tech)
4. [Install dependencies](#dep)
5. [To get API Key](#api)
6. [To run the project](#run)
7. [Approach](#approach)
8. [Features](#features)
9. [Acknowledgment](#ak)


<a name = "data"></a>
## About dataset:
* TMDB ~5000 movie dataset [TMDB 5000 movie dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
* The data contained following files:
  ```
  tmdb_5000_credits.csv
  tmdb_5000_movies.csv
  ```
 
<a name = "arch"></a>
 ## Architecture:
![architecture movie matrix](https://user-images.githubusercontent.com/75166814/169737665-497d8f77-7916-413d-9f8d-fd6f0bcabfab.png)

<a name = "tech"></a>
## Tech Stack:
![Untitled design](https://user-images.githubusercontent.com/75166814/170471714-d559b78d-20a6-4d8c-92d8-42b822cb43c1.png)

> Recommender system: 
   - Anaconda 2022.05
   - Jupyter Notebook 6.4.8
   - Pandas
   - Pickle
   - Scikit-learn
   - ntlk
> Web App:
   - Python 3.10.4
   - PyCharm 2022.1.1
   - Streamlit 1.9.0
   - PyTorch-Transformers 1.11.0

<a name = "dep"></a>
## Install dependencies:
  Install dependencies for webapp using PyCharm terminal in windows OS:
  - Copy require.txt file in movie-recommender-system folder.
  - Open PyCharm terminal and run:
  ``` 
    pip install require.txt
    pip install torch
  ```

<a name = "api"></a>
## To get API Key:
- Create an account in [TMDB Website](https://www.themoviedb.org/).
- Click on the API link from the left-hand sidebar in your account settings. 
- Fill in the details to apply for the API key.
- You will see the API key in your API sidebar once your request is approved.

<a name = "run"></a>
## To run the project:
- Clone the repository into your local machine.
- Install all the dependencies for web app. (Refer to the install dependencies section).
- Unzip similarlity.pkl file present in recommendation-system folder and movie-recommender-system folder.
- Get your API key. (Refer to the To get API key section).
- Then replace api_key in line 30 of recommendation system/movie-recommender-system (open in PyCharm or any other IDE).
- Run the following command :
  ``` streamlit run app.py ```
- Go to http://localhost:8501 on your browser.

<a name = "approach"></a>
## Approach:
The problem was divided into several steps:
  > Dataset Collection:
  
       Dataset was collected from TMDB 5000 movie dataset from the Kaggle website.
  > Data Wrangling:
       
       Null values and duplicate entries were dropped from the dataset.
  > Data Preprocessing:

       Created a new data frame by removing unnecessary columns and made tags for a particular movie by
       concatenating columns.
  > Model building:

       Implemented Content-based filtering (Recommendation algorithm). Movies were transformed into vectors.
       Cosine Similarity function from the scikit-learn module of python was used to give similarity scores. 
       Similarity scores were given to all movies when compared with a particular movie. The greater the 
       similarity score, the more chance for its recommendation. 
    
   ###### For more on ***Cosine Similarity*** [Here](https://towardsdatascience.com/cosine-similarity-explained-using-python-machine-learning-pyshark-5c5d6b9c18fa).
   
   
   > Web App:

      Built a web app in PyCharm by importing Streamlit module. Connected the data frame with the web app 
      using pickle library functions.Fetched posters of the movie through TMDB API. Implemented a chatbot
      using PyTorch-Transformers.
      
  ###### For implementing a chat-bot [Here](https://huggingface.co/docs/transformers/model_doc/blenderbot).
  
  <a name = "features"></a>
  ## Features:
  - On selecting a movie 8 similar movies are recommended along with their posters.
  - For more information user can click the title and through a link, it will get directed to the TMDB website for movie details.
  - A chatbot for interacting with the user. It can answer the various question of the user related to movie recommendations
  - Contact information for communication purposes.

<a name = "ak"></a>
## Acknowledgement:
- [Heroku](https://www.heroku.com/)
- [TMDB website](https://www.themoviedb.org/)
- [Kaggle](https://www.kaggle.com/)
- [Streamlit discuss](https://discuss.streamlit.io/)
- [Huggingface for chatbot](https://huggingface.co/)
- [Algorithm](https://towardsdatascience.com/cosine-similarity-explained-using-python-machine-learning-pyshark-5c5d6b9c18fa) 
  

