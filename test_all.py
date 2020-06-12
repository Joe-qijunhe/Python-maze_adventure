"""
Usage: python3 test_all.py
"""

import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_player import run_tests as test_player
from test_cells import run_tests as test_cells

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_game()
test_grid()
test_parser()
test_player()
test_cells()

# Run the e2e script
subprocess.call(['./test_e2e.sh'])
