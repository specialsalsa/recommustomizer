from flask import Flask
from flask import request
import requests
import base64
import json
from secret import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def auth():
    
    url = 'https://accounts.spotify.com/api/token'
    headers = {}
    data = {}



    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')

    headers['Authorization'] = f"Basic {base64Message}"
    
    data['grant_type'] = "client_credentials"

    r = requests.post(url, headers=headers, data=data)

    token = r.json()['access_token']

    return token

token = auth()


jsonReqObj = {}

@app.post('/getParamsFromBrowser')
def getParamsFromBrowser():
    
    jsonReq = json.loads(request.data)

    print(jsonReq)

    global jsonReqObj

    jsonReqObj = jsonReq

    # param = jsonReq['target_valence']

    # param = request.data['max_instrumentalness']

    print(jsonReqObj)

    # for key in jsonReqObj:
    #     print(key)
    #     print(jsonReqObj[key])


    return jsonReq



@app.route('/getRecs')
def getAlbum():

    

    headers = {
        "Authorization": "Bearer " + token
    }

    data = jsonReqObj

    # data['seed_artists'] = "72X6FHxaShda0XeQw3vbeF"
    # data['seed_genres'] = "alternative,rock"
    data['seed_tracks'] = "2TjzeWQI8tufyao0UDArJP"
    data['min_instrumentalness'] = 0.8
    data['target_instrumentalness'] = 0.9

    

    

    res = requests.get(url="https://api.spotify.com/v1/recommendations", headers=headers, params=data)
    
    return res.json()

@app.route('/getGenreSeeds')
def getGenreSeeds():
    token = auth()

    headers = {
        'Authorization': "Bearer " + token 
    }

    res = requests.get(url="https://api.spotify.com/v1/recommendations/available-genre-seeds", headers=headers)
    return res.json()

