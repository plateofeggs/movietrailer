import fresh_tomatoes
import media
import requests

# Use OMDb API to serve us some json movie info (http://www.omdbapi.com/)
# Getting movie data for The Departed
td = requests.get(
    "http://www.omdbapi.com/?t=The+Departed&y=&plot=short&r=json")
td_data = td.json()

# Getting movie data for 300
th = requests.get(
    "http://www.omdbapi.com/?t=300&y=&plot=short&r=json")
th_data = th.json()

# Getting movie data for Interstellar
st = requests.get(
    "http://www.omdbapi.com/?t=Interstellar&y=&plot=short&r=json")
st_data = st.json()

# Getting movie data for Pulp Fiction
pf = requests.get(
    "http://www.omdbapi.com/?t=Pulp+Fiction&y=&plot=short&r=json")
pf_data = pf.json()

# Getting movie data for The Dark Knight
tdk = requests.get(
    "http://www.omdbapi.com/?t=The+Dark+Knight&y=&plot=short&r=json")
tdk_data = tdk.json()

# Getting movie data for Deadpool
dp = requests.get(
    "http://www.omdbapi.com/?t=Deadpool&y=&plot=short&r=json")
dp_data = dp.json()

# Create instances of class Movie that will be sent to fresh_tomatoes.py
the_departed = media.Movie(td_data["Title"],
                           td_data["Plot"],
                           "http://ia.media-imdb.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=iojhqm0JTW4")


threehundred = media.Movie(th_data["Title"],
                           th_data["Plot"],
                           "http://ia.media-imdb.com/images/M/MV5BMjAzNTkzNjcxNl5BMl5BanBnXkFtZTYwNDA4NjE3._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=UrIbxk7idYA")


interstellar = media.Movie(st_data["Title"],
                           st_data["Plot"],
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=Lm8p5rlrSkY")


pulp_fiction = media.Movie(pf_data["Title"],
                           pf_data["Plot"],
                           "http://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")


the_dark_knight = media.Movie(tdk_data["Title"],
                              tdk_data["Plot"],
                              "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=yrJL5JxEYIw")


deadpool = media.Movie(dp_data["Title"],
                       dp_data["Plot"],
                       "http://ia.media-imdb.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=FyKWUTwSYAs&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DFyKWUTwSYAs&has_verified=1")  # NOQA

# fresh_tomatoes.py will use this list to make our web page
movies = [the_departed, threehundred, interstellar,
          pulp_fiction, the_dark_knight, deadpool]
fresh_tomatoes.open_movies_page(movies)
