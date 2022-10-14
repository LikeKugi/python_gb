# Даны два массива из 20 однозначных чисел. В первом из них записано количество мячей,
# забитых футбольной командой в игре, во втором — количество пропущенных мячей в этой же игре.
# а) Для каждой проведенной игры  напечатать словесный результат: "выигрыш", "ничья" или "проигрыш".
# б) Определить  количество  выигрышей,  количество  ничьих  и  количество проигрышей данной команды.
# в) Общее число очков, набранных командой (за выигрыш дается 3 очка, за ничью — 1, за проигрыш — 0).
import numpy as np


def create_range(): return np.random.randint(0, 10, 20, dtype=np.int_)


def analyse_games(balls: dict, res: dict):
    for score, lost in balls.items():
        if score == lost:
            res['pair'] += 1
        elif score > lost:
            res['won'] += 1
        else:
            res['loose'] += 1
    return res


def print_results(res: dict):
    for result, counter in res.items():
        print(result, counter)
    scores = res['won'] * 3 + res['pair']
    print(f'total scores: {scores}')


def main():
    goals = create_range()
    missed = create_range()
    results = {'won': 0, 'loose': 0, 'pair': 0}
    games = dict(zip(goals, missed))
    analyse_games(games,results)
    print_results(results)


if __name__ == '__main__':
    main()
