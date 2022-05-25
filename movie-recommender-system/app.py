import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_chat import message
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration

# for web app icon and title:
st.set_page_config(page_title='Movie.Matrix', page_icon='🍿')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# for hiding hamburger menu in streamlit app:
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# function for fetching movie posters from tmdb api key:
# error handling if movie posters are not found:
def fetch_poster(movie_id):
    try:
        response = requests.get(
            r'https://api.themoviedb.org/3/movie/{}?api_key=d761e5827dfd0e25f917996b722e26ae&language=en-US'.format(
                movie_id))
        data = response.json()
        return r"https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except:
        st.error('Oops! not found  ')
        st.error('try another movie or check your internet connection! 😊')
        st.stop()


# loading data frame:
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie.Matrix 🎬')  # webapp title

# select box for movie selection:
selected_movie_name = st.selectbox(
    'Search the movie name here! ⬇️',
    movies['title'].values
)

# main function for recommendation:
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_id = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_id.append(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters, recommended_movies_id

# recommendation after selecting movie from the select box:
if st.button('Recommend ✔️'):
    names, posters, m_id = recommend(selected_movie_name)
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            my_expander = st.expander(label=names[0])
            clicked = my_expander.write("[⭐ More **_info_** ⭐](https://www.themoviedb.org/movie/{})".format(m_id[0]))
            st.image(posters[0])

        with col2:
            my_expander = st.expander(label=names[1])
            clicked = my_expander.write("[⭐ More **_info_** ⭐](https://www.themoviedb.org/movie/{})".format(m_id[1]))
            st.image(posters[1])

        with col3:
            my_expander = st.expander(label=names[2])
            clicked = my_expander.write("[⭐ More **_info_** ⭐](https://www.themoviedb.org/movie/{})".format(m_id[2]))
            st.image(posters[2])

        with col4:
            my_expander = st.expander(label=names[3])
            clicked = my_expander.write("[⭐ More **_info_** ⭐](https://www.themoviedb.org/movie/{})".format(m_id[3]))
            st.image(posters[3])

    with st.container():
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            my_expander = st.expander(label=names[4])
            clicked = my_expander.write("[⭐ More **_info_** ⭐](https://www.themoviedb.org/movie/{})".format(m_id[4]))
            st.image(posters[4])

        with col6:
            my_expander = st.expander(label=names[5])
            clicked = my_expander.write("[⭐ More **_info_** ⭐](https://www.themoviedb.org/movie/{})".format(m_id[5]))
            st.image(posters[5])

        with col7:
            my_expander = st.expander(label=names[6])
            clicked = my_expander.write("[⭐ More **_info_** ⭐](https://www.themoviedb.org/movie/{})".format(m_id[6]))
            st.image(posters[6])

        with col8:
            my_expander = st.expander(label=names[7])
            clicked = my_expander.write("[⭐ More **_info_** ⭐](https://www.themoviedb.org/movie/{})".format(m_id[7]))
            st.image(posters[7])

# sidebar features of webapp:

# sidebar title:
with st.sidebar:
    st.title('**WELCOME.** ')

# chatbot implementation:
with st.sidebar:
    @st.experimental_singleton
    def get_models():
        model_name = "facebook/blenderbot-400M-distill"
        tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
        model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
        return tokenizer, model

    if "history" not in st.session_state:
        st.session_state.history = []

    st.header("_Hello Chatbot!_ 🤖")

    def generate_answer():
        tokenizer, model = get_models()
        user_message = st.session_state.input_text
        inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
        result = model.generate(**inputs)
        message_bot = tokenizer.decode(
            result[0], skip_special_tokens=True
        )  # .replace("<s>", "").replace("</s>", "")

        st.session_state.history.append({"message": user_message, "is_user": True})
        st.session_state.history.append({"message": message_bot, "is_user": False})

    for chat in st.session_state.history:
        message(**chat)  # unpacking

    st.text_input("Talk to the bot...", key="input_text", on_change=generate_answer)


# how to navigate website guide:
with st.sidebar:
    my_expander = st.expander('Walk through Movie.Matrix 🔎')
    clicked = my_expander.write('_How to navigate_')
    clicked = my_expander.image('ss1.png')
    clicked = my_expander.image('ss2.png')
    clicked = my_expander.image('ss3.png')
    clicked = my_expander.image('ss4.png')
    clicked = my_expander.image('ss5.png')

# contact-us details in sidebar:
with st.sidebar:
    st.header('_Contact Us_ 📞')
    my_expander = st.expander('Email')
    clicked = my_expander.write('_sweta.singh.cse20@itbhu.ac.in_')
    my_expander = st.expander('GitHub')
    clicked = my_expander.write("[_24swetaa_](https://github.com/24swetaa)")
    my_expander = st.expander('LinkedIn ')
    clicked = my_expander.write("[_sweta-singh_](https://www.linkedin.com/in/sweta-singh-932b34206/)")

# feedback form in sidebar:
with st.sidebar:
    st.header("_Send us your feedback!_  📬")
    ans = st.radio('Did you find this page useful?',('MAYBE','YES','NO'))
    if ans == 'MAYBE':
        st.write("")
    elif ans == 'YES':
        st.balloons()
        st.write("Please leave your feedback below. 🤗")
    elif ans == 'NO':
        st.write("Please help us improve! 😇")
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    contact_form = """
    <form action="https://formsubmit.co/sweta.singh.cse20@itbhu.ac.in" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style.css")


