# gameSettings.py
# ##################

import terminalColors as tColors

# general options
SHIP = 'o'
BLANK = ' '
NEUTRAL_COLOR = tColors.ENDC

# screen options
HORIZ_MARGIN = 2
VERT_MARGIN = 1
STATUS_MARGIN = 1

# target options
TGT_HIT = 'x'
TGT_MISS = '-'
TGT_COLOR = tColors.FAIL
TGT_SHIP_HIT_COLOR = tColors.FAIL

# self options
SELF_HIT = 'x'
SELF_COLOR = tColors.OKGREEN
SELF_SHIP_HIT_COLOR = tColors.FAIL