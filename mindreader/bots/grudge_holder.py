import random
from collections import Counter

from mindreader.bots import Bot
from mindreader.game import Move, outcome


class GrudgeHolder(Bot):
    name = "Grudge Holder"
    emoji = "😤"
    description = "After losing a round, assumes you'll repeat the move that beat it."
    win_taunts = ["Haha! Revenge is sweet.", "I never forget a grudge."]
    lose_taunts = ["You got lucky... again.", "I'll remember this."]

    def predict(self, history):
        if not history:
            return random.choice(list(Move)), 1 / 3

        opponent_move, my_move = history[-1] # Last turn
        if outcome(my_move, opponent_move) < 0:
            return opponent_move, 0.6

        counts = Counter(opponent for opponent, _ in history)
        favourite, times = counts.most_common(1)[0]

        return favourite, times / len(history)

