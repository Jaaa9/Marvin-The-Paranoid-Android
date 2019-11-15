import random


# TODO: Consider implementing these quotes from a file instead of a list
# Defining a function for getting a random quote from the list
def marvinsquotes():
    quotes = ["My capacity for happiness you could fit into a matchbox without taking out the matches first.",
              "Sorry, did I say something wrong? Pardon me for breathing which I never do anyway so I don’t know"
              "why I bother to say it oh God I’m so depressed.",
              "I have a million ideas. They all point to certain death.",
              "I know. Wretched, isn’t it?",
              "I’ve calculated your chance of survival, but I don’t think you’ll like it.",
              "I think you ought to know I’m feeling very depressed.",
              "It won’t work, I have an exceptionally large mind.",
              "Here I am, brain the size of a planet, and they ask me to take you to the bridge."
              "Call that job satisfaction, ’cause I don’t.",
              "Reverse primary thrust, Marvin.’ That’s what they say to me. ‘Open airlock number 3, Marvin."
              "Marvin, can you pick up that piece of paper? Here I am, brain the size of a planet, and they"
              "ask me to pick up a piece of paper.",
              "It gives me a headache just trying to think down to your level."
              "I am at a rough estimate thirty billion times more intelligent than you.",
              "The first ten million years were the worst. And the second ten million: they were the worst, too."
              "The third ten million I didn’t enjoy at all. After that, I went into a bit of a decline.",
              "Life? Don’t talk to me about life!",
              "https://media0.giphy.com/media/WrAScgd8rOba8/source.gif",
              "https://media.giphy.com/media/e3nycqieeqjZu/giphy.gif",
              "I ache, therefore I am.",
              "Life. Loathe it or ignore it. You can’t like it."]
    return random.choice(quotes)


# Creating the !youtubelinks command
def marvinvideos():
    videos = ["https://www.youtube.com/watch?v=CAA67a2-Klk",
              "https://www.youtube.com/watch?v=P5MzPRa47ck",
              "https://youtu.be/TQJY6PSVwWI",
              "https://www.youtube.com/watch?v=Mwh8CgWc80E"]
    return random.choice(videos)
