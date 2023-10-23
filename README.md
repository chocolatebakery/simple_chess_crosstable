# simple_chess_crosstable
Generate a simple chess crosstable from a PGN file

Instructions:
pip install -r requirements.txt

To execute,
make sure there's no output.html file, since it will just add extra lines to it.

usage:

python generate_crosstables.py PGN_file_name.pgn

Open output.html file.

The table can be formatted manually with CSS.

It will sort every player based on the whole score (1 point per win, 0.5 per draw)
For each row, it will show the wins as white for each player

