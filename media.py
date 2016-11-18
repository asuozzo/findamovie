class Movie(object):
    """This is a movie object, containing information about a movie

    Attributes:
        movie_title (str): the title of the movie
        poster_image (str): a URL for the movie poster
        trailer_youtube (str): a youtube URL for the trailer
        genre (str): the movie's genre
        release_year (str): the year of the movie's release
    """
    def __init__(self, movie_title, poster_image,
                 trailer_youtube, genre, release_year):
        self.title = movie_title
        self.poster_image = poster_image
        self.summary = ""
        self.trailer = trailer_youtube
        self.genre = genre
        self.year = release_year
