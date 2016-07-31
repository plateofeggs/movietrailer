import webbrowser


class Movie():
    """ Movie is a class to show movie related information

    Attributes:
        movie_title (str): sets the title of the movie
        storyline (str): sets the plot of the movie
        poster_image_url (str): sets the url of the movie's poster
        trailer_youtube_url (str): sets the url of the movie's trailer
    """

    def __init__(self,
                 movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
