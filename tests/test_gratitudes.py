from lib.gratitudes import *

def test_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("food")
    gratitude.add("drinks")
    result = gratitude.format()
    assert result == "Be grateful for: food, drinks"