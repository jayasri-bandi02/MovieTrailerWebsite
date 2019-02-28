import webbrowser

class Movie():
    def __init__(self,name,storyline,poster,trailer):
        
        self.title=name
        self.storyline=storyline
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
