import webbrowser

class Movie:
    def __init__(self, youtube_url):
        self.trailer_url = youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
