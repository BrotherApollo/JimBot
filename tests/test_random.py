from src.meme import random_meme
from src.excuses import generate_excuse

def test_random_meme():
    assert random_meme()
    
def test_random_excuse():
    assert generate_excuse()