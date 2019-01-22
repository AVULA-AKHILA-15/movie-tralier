import webbrowser
class Tollywoodmovies():
    def __init__(self,movie_title,movie_storyline,
              mov_poster_url,movie_youtube_url):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=mov_poster_url
        self.trailer_youtube_url=movie_youtube_url
    def show_movie_trailers(self):
        webbroweser.open(self.trailer_youtubeurl)
