# Contributing to Mind Reader Arena

Welcome! 👋 If this is your first open source contribution, you're in the right place.

## The 5-step workflow

1. **Fork** this repo on GitHub, then clone your fork:
   ```bash
   git clone https://github.com/<you>/Mind-Reader-Arena.git
   cd Mind-Reader-Arena
   ```
2. **Branch** off for your change:
   ```bash
   git checkout -b add-copycat-bot
   ```
3. **Code**: pick an idea from [GOOD_FIRST_ISSUES.md](GOOD_FIRST_ISSUES.md).
4. **Test**:
   ```bash
   python3 -m unittest
   python3 -m mindreader play --bot <your_bot>
   ```
5. **Push & open a PR**:
   ```bash
   git add .
   git commit -m "Add Copycat bot"
   git push origin add-copycat-bot
   ```
   Then click "Compare & pull request" on GitHub. Say what you added and paste a sample game.

## Adding a bot (the most popular first PR)

Create **one new file** in `mindreader/bots/`. The file name becomes the bot's id. You don't need to register it anywhere: the game finds it automatically.

```python
# mindreader/bots/copycat.py
import random

from mindreader.bots import Bot
from mindreader.game import Move


class Copycat(Bot):
    name = "Copycat"
    emoji = "🐱"
    description = "Assumes you'll repeat whatever you just did."
    win_taunts = ["Meow. Predictable."]
    lose_taunts = ["Hiss!"]

    def predict(self, history):
        # history = [(opponent_move, my_move), ...], oldest first
        if not history:
            return random.choice(list(Move)), 1 / 3
        last_opponent_move = history[-1][0]
        return last_opponent_move, 0.5
```

The rules for `predict()`:
- Return **your guess of the opponent's next move**, plus a **confidence** from `0.0` to `1.0`.
- The game automatically plays the move that beats your guess.
- Handle an empty `history` (the first round).

`tests/test_bots.py` checks **every** bot automatically, including yours. If `python3 -m unittest` passes, you're good.

Then see how your bot ranks:
```bash
python3 -m mindreader tournament
```

## Ground rules

- Standard library only, so nobody has to `pip install` anything.
- Keep Python 3.9 compatible (no `match` statements).
- One idea per PR. Small PRs get merged fast.
- Be kind in reviews. Everyone here is learning. 💜
