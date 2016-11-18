import movies
import webbrowser
import os

# Base page structure HTML/CSS sourced from Udacity project template
html_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>What Movie Should You Watch?</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .description {
            text-align:left
        }
        .poster {
            width:60%
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        @media all and (min-width : 768px) {
            .movie-tile{
                height:500px;
            }
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });

        $(document).ready(function(){
            $(".filter").on("click",function(){
                value = $(this).attr("value");
                if (value === "all") {
                    $("#movies").find(".all").show()
                } else {
                    $("#movies").find(".all").hide()
                    value = "."+value
                    $("#movies").find(value).show()
                }
            });
        });
    </script>
</head>
'''

html_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">What Movie Should You Watch?</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
        <div class="row">
            <div><h4>What kind of movie are you in the mood for?</h4>
                <div id="myFilter">
                    <button class="btn btn-primary filter" value="all">Anything!</button>
                    <button class="btn btn-primary filter" value="comedy">Comedy</button>
                    <button class="btn btn-primary filter" value="drama">Drama</button>
                    <button class="btn btn-primary filter" value="action">Action</button>
                </div>
            </div>
        </div>
        <div class="row" id="movies">
            {movie_tiles}
        </div>
    </div>
  </body>
</html>
'''

# A single movie entry html template
html_movie_tile = '''
<div class="col-sm-4 movie-tile text-center all {genre}" data-trailer-youtube-id="{trailer_youtube}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image}" class="poster">
    <h2>{movie_title}</h2>
    <div class="description"><p>{plot}</p>
    <p><i>Released: {release_year}</i></p></div>
</div>
'''


# Separate the YouTube trailer id from the url
def get_trailer_id(movie):
    startindex = movie.trailer.find("v=")
    trailerid = movie.trailer[startindex+2:]
    return trailerid


# add each movie's information to an HTML tile
def create_movie_tiles(movies):
    tilecontent = ""
    for movie in movies.movielist:
        tilecontent += html_movie_tile.format(
            trailer_youtube=get_trailer_id(movie),
            movie_title=movie.title,
            genre=movie.genre,
            poster_image=movie.poster_image,
            release_year=movie.year,
            plot=movie.summary
        )
    return tilecontent


# generate the webpage
def create_webpage(movies):
    outputfile = "index.html"
    webpage_file = open(outputfile, "w")

    webpage_file.write(html_head)

    webpage_file.write(html_content.format(
        movie_tiles=create_movie_tiles(movies)))

    webpage_file.close()

    filepath = os.getcwd()
    webbrowser.open("file://" + filepath + "/" + outputfile)

create_webpage(movies)
