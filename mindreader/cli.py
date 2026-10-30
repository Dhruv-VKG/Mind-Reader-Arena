"""Command line entry point: `mindreader play | bots | tournament`."""

from __future__ import annotations

import argparse
import itertools
import sys

from mindreader import display
from mindreader.bots import all_bots
from mindreader.game import Match, Move, run_duel


def cmd_play(args) -> None:
    bots = all_bots()
    if args.bot not in bots:
        sys.exit(f"Unknown bot '{args.bot}'. Try one of: {', '.join(bots)}")
    bot = bots[args.bot]()
    match = Match()

    display.banner()
    display.intro(bot, args.rounds)
    number = 1
    while number <= args.rounds:
        # The bot commits to its guess BEFORE you choose. No cheating!
        guess, confidence = bot.predict(match.history)
        try:
            text = input(f"Round {number}/{args.rounds}, your move: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if text.strip().lower() in ("q", "quit"):
            break
        player = Move.parse(text)
        if player is None:
            print(display.paint("  Please type r, p or s.", "yellow"))
            continue
        rnd = match.play_round(player, guess, confidence)
        display.show_round(number, bot, rnd, bot.taunt(won=rnd.result < 0) if rnd.result else "")
        number += 1

    if match.history:
        display.final_score(bot, match)


def cmd_bots(args) -> None:
    display.bot_list(all_bots())


def cmd_tournament(args) -> None:
    bots = all_bots()
    stats = {bot_id: [0, 0, 0] for bot_id in bots}  # wins, losses, ties
    for a, b in itertools.combinations(bots, 2):
        a_wins, b_wins, ties = run_duel(bots[a](), bots[b](), args.rounds)
        stats[a][0] += a_wins
        stats[a][1] += b_wins
        stats[a][2] += ties
        stats[b][0] += b_wins
        stats[b][1] += a_wins
        stats[b][2] += ties
    rows = [(bots[i].emoji, bots[i].name, *stats[i]) for i in bots]
    rows.sort(key=lambda row: (row[2] - row[3], row[2]), reverse=True)
    display.leaderboard(rows)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="mindreader", description="Rock-Paper-Scissors vs mind-reading bots.")
    sub = parser.add_subparsers(dest="command")

    play = sub.add_parser("play", help="play against a bot (default)")
    play.add_argument("--bot", default="markov", help="bot id, see `mindreader bots`")
    play.add_argument("--rounds", type=int, default=10)
    play.set_defaults(func=cmd_play)

    sub.add_parser("bots", help="list available bots").set_defaults(func=cmd_bots)

    tour = sub.add_parser("tournament", help="every bot vs every other bot")
    tour.add_argument("--rounds", type=int, default=100, help="rounds per duel")
    tour.set_defaults(func=cmd_tournament)

    args = parser.parse_args(argv)
    if args.command is None:
        args = parser.parse_args(["play"])
    args.func(args)


if __name__ == "__main__":
    main()
