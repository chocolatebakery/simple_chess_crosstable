import sys
import pandas as pd
from tabulate import tabulate
from collections import defaultdict

def add_Score(total, games, result, white, black):
    if (result == '1-0'):
        if not white in total:
            total[white] = 1
        else:
            total[white] += 1
        if not white in games:
            games[white] = [[black, 'W']]
        else:
            games[white].append([black, 'W'])
    if (result == '1/2-1/2'):
        if not white in total:
            total[white] = 0.5
        else:
            total[white] += 0.5
        if not black in total:
            total[black] = 0.5
        else:
            total[black] += 0.5
        if not white in games:
            games[white] = [[black, 'D']]
        else:
            games[white].append([black, 'D'])
    if (result == '0-1'):
        if not black in total:
            total_score[black] = 1
        else:
            total_score[black] += 1
        if not white in games:
            games[white] = [[black, 'L']]
        else:
            games[white].append([black, 'L'])

if (len(sys.argv) > 1):
    input_file = open(sys.argv[1])
    file = open(input_file.name, "r", encoding='utf-8')
    total_score = {}
    games_with_white = {}
    result=""
    white=""
    black=""
    with file as reading:
        for line in reading:
            if line.startswith('[White'):
                s = line
                white=s.split('"')[1::2]
            if line.startswith('[Black'):
                s = line
                black=s.split('"')[1::2]
            if line.startswith('[Result'):
                s = line
                result=s.split('"')[1::2]
                add_Score(total_score, games_with_white, result[0], white[0], black[0])
    file.close()
    sort_by_wins = dict(sorted(total_score.items(), key=lambda x:x[1], reverse=True))
    participants_list = list(sort_by_wins)
    indexed_participants_list = {k: v for v, k in enumerate(participants_list)}
    add_score_index = {}
    for participant in participants_list:
        participant_games = games_with_white[participant]
        for game in participant_games:
            opponent_idx = indexed_participants_list[game[0]]
            if not participant in add_score_index:
                add_score_index[participant] = [""] * len(indexed_participants_list)
                add_score_index[participant][opponent_idx] = game[1]
                participant_idx = indexed_participants_list[participant]
                add_score_index[participant][participant_idx] = "-"
            else:
                add_score_index[participant][opponent_idx]=add_score_index[participant][opponent_idx]+game[1]
    print(indexed_participants_list)
    print(add_score_index)
    pd.set_option('display.max_columns', None)
    final_table=pd.DataFrame(add_score_index, index=indexed_participants_list)
    with open("output.html", "a") as f:
        print(tabulate(final_table.transpose(), headers='keys', tablefmt='html'), file=f)
else:
    print("no PGN input")
    exit(0)
