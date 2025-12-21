from src.meme import random_meme, spongify, get_reacts, generate_excuse


def test_random_meme():
    assert random_meme()


def test_random_excuse():
    assert generate_excuse()


def test_spongify():
    assert spongify("test") == "tEsT"

    assert spongify("free beer") == "fReE BeEr"


def test_reacts():
    assert get_reacts("bot") == ["🤖"]
    
    assert len(get_reacts("lobster bot")) == 2

    assert len(get_reacts(
        """Hey Jimmy, the timecard bot found an error, please check your hours 
        ASAP. I emailed helpdesk about payroll and charge codes today since I’m 
        taking PTO next week. Sign it soon."""
        )) == 11