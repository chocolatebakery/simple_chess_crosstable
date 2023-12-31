# simple_chess_crosstable
Generate a simple chess crosstable from a PGN file

**Instructions:**

```
pip install -r requirements.txt
```

To execute,
make sure there's no output.html file, since it will just add extra lines to it.

**Usage:**

```
python generate_crosstables.py PGN_file_name.pgn
```

Open output.html file.

The table can be formatted manually with CSS.

It will sort every player based on the whole score (1 point per win, 0.5 per draw)
For each row, it will show the wins as white for each player

![example](https://github.com/chocolatebakery/simple_chess_crosstable/assets/103671842/ababe9d8-7b17-4fdc-8fd6-951d94bf1210)


As this example shows:
Ian Nepomniachtchi (the first place) had a 5 draws with white and 1 win. and 3 wins with black plus 4 draws
The L on Ding Liren (the second place) shows that he lost with white versus Ian Nepomniachtchi

Taken from [FIDE Website](https://ratings.fide.com/view_games.phtml?event=294151)
