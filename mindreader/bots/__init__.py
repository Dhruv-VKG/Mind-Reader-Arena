"""Bot base class and auto-discovery.

Every .py file in this folder is imported automatically, and every Bot subclass
found becomes playable. The file name is the bot's id: bots/markov.py -> --bot markov.
One file = one bot.
"""

from __future__ import annotations

import importlib
import pkgutil
import random
from typing import Dict, List, Tuple, Type

from mindreader.game import History, Move


class Bot:
    name = "Unnamed Bot"
    emoji = "🤖"
    description = "A mysterious bot."
    win_taunts: List[str] = ["Too easy!", "I saw that coming."]
    lose_taunts: List[str] = ["Lucky guess...", "Hmm, interesting."]

    def predict(self, history: History) -> Tuple[Move, float]:
        """Guess the opponent's NEXT move.

        history: past rounds as (opponent_move, my_move), oldest first.
        Return (guessed_move, confidence) where confidence is between 0.0 and 1.0.
        The game then plays whatever beats your guess.
        """
        raise NotImplementedError

    def taunt(self, won: bool) -> str:
        return random.choice(self.win_taunts if won else self.lose_taunts)


def _bot_id(cls: Type[Bot]) -> str:
    return cls.__module__.rsplit(".", 1)[-1]


def all_bots() -> Dict[str, Type[Bot]]:
    """Import every module in this package and return {bot_id: BotClass}, sorted by id."""
    for module in pkgutil.iter_modules(__path__):
        importlib.import_module(f"{__name__}.{module.name}")
    found = {_bot_id(cls): cls for cls in Bot.__subclasses__()}
    return dict(sorted(found.items()))
