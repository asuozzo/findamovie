import media
import urllib2
import json

# Create movie objects
harold_and_maude = media.Movie("Harold and Maude",
                                "https://t2.gstatic.com/images?q=tbn:ANd9GcRGDD-RPAD2zrsxe9mhXnOWMVQC6qOPe7nFiDjzhsypiVlKUmhk",# NOQA
                                "https://www.youtube.com/watch?v=u-cOukYeGVM",
                                "comedy",
                                "1971")

inside_out = media.Movie("Inside Out",
                         "https://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",# NOQA
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY",
                         "comedy",
                         "2015")

duck_soup = media.Movie("Duck Soup",
                        "https://t2.gstatic.com/images?q=tbn:ANd9GcSfBxLjdtAdbNZwIfLbp6gpCwWlz8c5PEVYhb85yTlg6dCWOft7", # NOQA
                        "https://www.youtube.com/watch?v=AF0Pa1uMP4Q",
                        "comedy",
                        "1933")

inception = media.Movie("Inception",
                        "https://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD", # NOQA
                        "https://www.youtube.com/watch?v=YkVRTbleoSU",
                        "action",
                        "2010")

bourne_identity = media.Movie("The Bourne Identity",
                              "https://www.gstatic.com/tv/thumb/movieposters/28900/p28900_p_v8_ai.jpg", # NOQA
                              "https://www.youtube.com/watch?v=cD-uQreIwEk",
                              "action",
                              "2002")

captain_america = media.Movie("Captain America: Civil War",
                              "https://t3.gstatic.com/images?q=tbn:ANd9GcTz1xU3qYlGXViIS51HIQh71D339ceW2nlWnb8zzSaJAL0newVj", # NOQA
                              "https://www.youtube.com/watch?v=dKrVegVI0Us",
                              "action",
                              "2016")

atonement = media.Movie("Atonement",
                        "https://www.gstatic.com/tv/thumb/movieposters/167496/p167496_p_v8_af.jpg", # NOQA
                        "https://www.youtube.com/watch?v=Dznc_LJIJ4c",
                        "drama",
                        "2007")

spotlight = media.Movie("Spotlight",
                        "https://t0.gstatic.com/images?q=tbn:ANd9GcS8FoV_CqN1-EetgwddDzbfaFYsOlAufiupBdzDTGLm6l8ty-F1", # NOQA
                        "https://www.youtube.com/watch?v=Zg5zSVxx9JM",
                        "drama",
                        "2015")

almost_famous = media.Movie("Almost Famous",
                            "https://t0.gstatic.com/images?q=tbn:ANd9GcQBfoQp1r6qJCTme8tT_OKkNsITBsQjPRRVNqwN8PdWZTID3ZXZ", # NOQA
                            "https://www.youtube.com/watch?v=SHNETQXKlY4",
                            "drama",
                            "2000")


movielist = [spotlight, harold_and_maude, captain_america, inside_out,
             duck_soup, inception, almost_famous, bourne_identity,
             atonement]


# Grab a movie's plot summary from the Opem Movie Database API.
def get_plot(movie):
    # strip punctuation from movie title, replace spaces with plus signs
    title = movie.title.translate(None, ":!.").replace(" ", "+")
    url = "http://www.omdbapi.com/?t=" + title + "&y=" + movie.year + "&plot=short&r=json" # NOQA
    moviedata = urllib2.urlopen(url)
    moviejson = json.loads(moviedata.read())
    movie.summary = moviejson["Plot"]

for movie in movielist:
    get_plot(movie)
