import random
import os

def random_meme():
    memes = os.listdir("assets/")
    choice = random.choice(memes)
    return f"assets/{choice}"


def spongify(s):
    return "".join([s[i].upper() if i % 2 else s[i].lower() for i in range(len(s))])