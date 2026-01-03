from src.meme import random_meme, spongify, get_reacts, generate_excuse


def test_random_meme():
    assert random_meme()


def test_random_excuse():
    assert generate_excuse()


def test_spongify():
    assert spongify("test") == "tEsT"

    assert spongify("free beer") == "fReE BeEr"


def test_reacts():
    assert get_reacts("error") == ["⚠️"]
    
    assert len(get_reacts("timecard error")) == 2

    assert len(get_reacts(
        "The timecard error happened again I need to resign the email chargecode"
        )) == 5