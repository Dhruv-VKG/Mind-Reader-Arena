# Good First Issues

Pick one, tell the organizers (or comment on the matching GitHub issue) so two people don't take the same one, and go!

## 🟢 Tiny (≈15 min)

- [ ] **New taunts**: give an existing bot more personality (`win_taunts` / `lose_taunts`).
- [ ] **Improve the README**: fix typos, add a GIF or screenshot of a real game.
- [ ] **Tie taunts**: bots say nothing on a tie. Add a `tie_taunts` list to `Bot` and use it in `cli.py`.

## 🟢 Easy: add a new bot (≈30 min, one new file)

- [ ] 🐱 **Copycat**: guesses you'll repeat your last move.
- [ ] 🔁 **Cycler**: guesses you'll go rock → paper → scissors in order.
- [ ] 😤 **Grudge Holder**: after losing a round, guesses you'll repeat your winning move.
- [ ] 🪞 **Mirror**: guesses you'll copy *the bot's* last move.
- [ ] 💤 **Lazy Larry**: always guesses rock ("everyone starts with rock").
- [ ] 🎲 Your own idea! Anything goes, as long as the tests pass.

## 🟡 Medium (≈1 hr)

- [ ] **`--seed` flag**: make games reproducible (`random.seed(...)`).
- [ ] **High scores**: save your best predictability score to `~/.mindreader.json` and show it at the end.
- [ ] **`stats` command**: after a game, show how often you threw each move as a mini bar chart.
- [ ] **Best-of mode**: `--best-of 5` ends the match when someone reaches 3 wins.
- [ ] **Rock-Paper-Scissors-Lizard-Spock** 🦎🖖: `--mode rpsls`. Hint: `BEATS` in `game.py` needs to map each move to *two* losers.

## 🔴 Stretch (for experienced folks)

- [ ] 🧠 **Ensemble bot**: runs all the other bots internally and trusts whichever has been right most often.
- [ ] 🤖 **LLM bot**: asks a language model to predict your move. It must be **opt-in**: only enabled when an API key env var is set, and skipped cleanly otherwise so tests still pass offline.
- [ ] ⚙️ **GitHub Actions CI**: run `python3 -m unittest` on every PR (Python 3.9 → 3.13).
- [ ] 📊 **Tournament heatmap**: show a bot-vs-bot win matrix instead of just totals.
