import random
import os

def random_meme():
    memes = os.listdir("assets/")
    choice = random.choice(memes)
    return f"assets/{choice}"