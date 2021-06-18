import requests
import json
from movie import Movie

def getInfoMovies(id, list_of_movie_info):
    magic_url = "https://api-cache-b.hbogola.com/contentgw/v7.0/Content/SPA/COMP/" + id + "/f5d80122-51d5-46c6-bcf0-ec3b73b2e45b"
    response = requests.get(magic_url)
    res_json = json.loads(response.text)
    movie = Movie(res_json["Id"],
                  res_json["Name"],
                  res_json["ProductionYear"] if res_json.get("ProductionYear") else None,
                  res_json["DurationText"] if res_json.get("DurationText") else None,
                  res_json["Genre"] if res_json.get("Genre") else None,
                  res_json["AgeRatingName"] if res_json.get("AgeRatingName") else None,
                  res_json["Abstract"] if res_json.get("Abstract") else None,
                  res_json["AudioTracks"] if res_json.get("AudioTracks") else None,
                  res_json["Subtitles"] if res_json.get("Subtitles") else None,
                  res_json["Director"] if res_json.get("Director") else None,
                  res_json["Cast"] if res_json.get("Cast") else None,
                  res_json["Writer"] if res_json.get("Writer") else None,)
    list_of_movie_info.append(movie.__dict__)
