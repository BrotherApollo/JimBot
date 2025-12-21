from src.meme import random_meme, spongify
from src.excuses import generate_excuse

def test_random_meme():
    assert random_meme()
    
def test_random_excuse():
    assert generate_excuse()
    
    
def test_spongify():
    assert spongify("test") == "tEsT"
    
    assert spongify("free beer") == "fReE BeEr"