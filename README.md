# Movie-Matrix 🎬

_Movie Recommendation System_

A movie suggestion from the server-based system has made discovering a good movie much easier these days. Movie recommendations assist cinephiles and movie fans by proposing top-tier films to watch without wasting time searching through large databases. To solve this problem, I propose a content-based model that will use Python-based Machine Learning algorithms to analyse large datasets and generate a movie recommendation.

**Movie Matrix** is a web application which recommends similar movies to a movie the user likes.

# Table of content:
1. [About the dataset](#data)
2. [Architecture](#arch)
3. [Tech stack](#tech)
4. [Install dependencies](#dep)
5. [To get API Key](#api)
6. [To run the project](#run)
7. [Approach](#approach)
8. [Features](#features)
9. [Screenshots of webapp](#ss)
10. [Webapp deployment](#deploy)
11. [Acknowledgment](#ak)
12. [Connect with me](#me)


<a name = "data"></a>
## About the dataset:
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
  Install dependencies for web app using PyCharm terminal in windows OS:
  - Copy the require.txt file in the movie-recommender-system folder.
  - Open the PyCharm terminal and run:
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
- Install all the dependencies for the web app. (Refer to the install dependencies section).
- Unzip the similarity.pkl file present in the recommendation-system folder and movie-recommender-system folder.
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
       Cosine Similarity function from the Scikit-learn module of python was used to give similarity scores. 
       Similarity scores were given to all movies when compared with a particular movie. The greater the 
       similarity score, the more chance for its recommendation. 
    
   ###### For more on ***Cosine Similarity*** [Here](https://towardsdatascience.com/cosine-similarity-explained-using-python-machine-learning-pyshark-5c5d6b9c18fa).
   
   
   > Web App:

      Built a web app in PyCharm by importing the Streamlit module. Connected the data frame with the web app 
      using pickle library functions.Fetched posters of the movie and movie details through TMDB API. Implemented a chatbot
      using PyTorch-Transformers.
      
  ###### For implementing a chat-bot [Here](https://huggingface.co/docs/transformers/model_doc/blenderbot).
  
  <a name = "features"></a>
  ## Features:
  - A ```selectbox``` for selecting movies. Around 5000 movie options are available.
  - ```Grid layout``` to show 8 similar movies recommended for a given movie.
  - Option of ```enlarging a movie poster```.
  - To know more about the recommended movie one can click the ```More info``` option and it gets directed to the tmdb
    movie website for movie details.
  - ```Error Page``` is shown if the recommendations for the selected movie are not fetched.
  - A ```Sidebar navigation``` present consists of a chatbot, contact us and feedback form.
  - ```Page icon``` and ```Page title``` to display the uniqueness of this web app.
  - ```Explore section``` in the web app helps the user to navigate through the web app.
  - An interactive ```Chatbot``` which can answer queries of a user-related to movie details, recommendations and 
    other stuff. 
  - A ```Contact Us``` section to get engaged with the users.
  - Valuable suggestions are appreciated by the users and they can submit them through ```Feedback forms``` present inside
    the web app.
  - The web app is ```Optimized for mobile view```.

<a name = "ss"></a>
## Screenshots of the web app:
<img width="533" alt="ss1" src="https://user-images.githubusercontent.com/75166814/170484325-0061cb78-4da4-4965-9932-e1865c9efdb6.png">
<img width="533" alt="ss2" src="https://user-images.githubusercontent.com/75166814/170484353-65285951-7598-48ac-8cd0-e721701352b3.png">
<img width="532" alt="ss3" src="https://user-images.githubusercontent.com/75166814/170484385-ad9374ed-85c2-4d81-91b0-4d245f3111c8.png">
<img width="533" alt="ss4" src="https://user-images.githubusercontent.com/75166814/170484415-cd9fad14-954b-42a7-a1fc-3513429fdc3f.png">
<img width="533" alt="ss5" src="https://user-images.githubusercontent.com/75166814/170484434-8fd3888a-501f-43bb-b05a-5d94a4e2aa8c.png">

<a name = "deploy"></a>
## Webapp deployment:
Link to Movie.matrix web app: https://movie-matrix.herokuapp.com/

_Steps to deploy in the Heroku server_ :
- Create an account in [Heroku](https://www.heroku.com/).
- Create a new app and give it a name.
- Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
- Run the following the commands in your IDE:
```
$ heroku login
$ cd my-project/
$ git init
$ heroku git:remote -a movie.matrix
$ git add .
$ git commit -am "initial deployment"
$ git push heroku master
```
> Note:

 Unable to deploy chatbot feature in Heroku app due to its slug size (larger than the maximum limit). 
 
 For adding the chatbot feature add the following lines in the requirements.txt file before deploying to the Heroku server.
 ```
 streamlit_chat
 torch
 transformers
 ```

<a name = "ak"></a>
## Acknowledgement:
- [Heroku](https://www.heroku.com/)
- [TMDB website](https://www.themoviedb.org/)
- [Kaggle](https://www.kaggle.com/)
- [Streamlit discuss](https://discuss.streamlit.io/)
- [Huggingface for chatbot](https://huggingface.co/)
- [Algorithm](https://towardsdatascience.com/cosine-similarity-explained-using-python-machine-learning-pyshark-5c5d6b9c18fa) 
  
<a name = "me"></a>
## Connect with me:
_Drop by and say hello_

[Linkedin](https://www.linkedin.com/in/sweta-singh-932b34206/)

