# coding=utf-8
from urllib import request
import json
import pyttsx3

class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"{self.setup} {self.punchline}"


jokes = []

url = "http://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
content = json.loads(r.read())

for j in content:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

numberOfJokes = len(jokes)

if numberOfJokes > 0:
    print(f"We got {numberOfJokes} jokes to lift you spirits!")

    for j in jokes:
        print(j)
        pyttsx3.speak(j.setup)
        pyttsx3.speak(j.punchline)

