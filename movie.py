import json

class Movie():
    def __init__(self, id, title, year, duration, genre, ageRatingName, abstract, audioTracks, subtitles, director, cast, writer):
        self.id = id
        self.title = title
        self.year = year
        self.duration = duration
        self.genre = genre
        self.ageRatingName = ageRatingName
        self.abstract = abstract
        self.audioTracks = audioTracks
        self.subtitles = subtitles
        self.director = director
        self.cast = cast
        self.writer = writer

    def showMovie(self):
        print("##########################")
        print(self.id)
        print(self.title)
        print(self.year)
        print(self.duration)
        print(self.genre)
