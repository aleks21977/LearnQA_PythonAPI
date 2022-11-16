def test_short_phrase ():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, "The phrase is more than 14 characters"