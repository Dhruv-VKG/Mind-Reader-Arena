import random

from mindreader.bots import Bot
from mindreader.game import Move


class ChaosMonkey(Bot):
    name = "Chaos Monkey"
    emoji = "🐒"
    description = "Doesn't think at all. Pure random. Surprisingly hard to beat."
    win_taunts = ["OOK OOK! 🍌", "Banana brain wins again!"]
    lose_taunts = ["*throws banana at you*", "Ook... 🙈"]

    def predict(self, history):
        return random.choice(list(Move)), 1 / 3
