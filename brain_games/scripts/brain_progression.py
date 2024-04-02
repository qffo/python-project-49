#!/usr/bin/env python3

from brain_games.game_logic import start_game
from brain_games.games import brain_progression


def main():
    start_game(brain_progression)


if __name__ == '__main__':
    main()
