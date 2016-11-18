## What is this?
It's a Python script designed to take an array of movie objects and output them into a pretty website that allows you to filter movies by genre.

[Screenshot](img/Screenshot.png)

## Requirements
Make sure you've got the following Python libraries before running this: webbrowser, os, urllib2 and json.

## Running this program
To run this program, the script you want is`findamovie.py`. It will write (or rewrite) code for a simple website to `findamovie.html`, then open that file in your default web browser.

`findamovie.py` uses `media.py`, which defines the class "Movie," and `movies.py`, which creates nine movie objects and retrieves some information from the Open Movie Database API. You can add more movies or edit the existing ones in this file.