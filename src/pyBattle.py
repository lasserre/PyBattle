# main.py...
import sys

def startNewGame():
	print "starting new game..."

def joinGame():
	print "joining game..."

def exit():
	sys.exit()

# Program Constants
_menu_separator = "---------------------------"
_error_msg = "Please type the number for the action you wish to select."

# Menu Dictionary Format
#   index -> ( display text, onSelected() )
_menu = {
	1: ("Start a new game", startNewGame),
	2: ("Join an existing game", joinGame),
	3: ("Quit", lambda : exit)
}

# Returns the Game Menu as a String
def getGameMenuString():

	s = _menu_separator + "\n"
	s += "PyBattle Game Menu\n"
	s += _menu_separator + "\n"
	s += "\n"

	for k, v in _menu.iteritems():
		s += '{0}: {1}\n'.format(k, v[0])

	return s

# Runs the Game Menu. Returns 1 if invalid selection specified
def runGameMenu():

	# print menu
	print getGameMenuString()

	selStr = raw_input("Enter selection >>> ")
	sel = 0
	
	try:
		sel = int(selStr)
	except:
		print "Invalid selection '{0}'. {1}".format(selStr, _error_msg)
		return 1

	# handle selection
	if sel in _menu:
		_menu[sel][1]()
	else:
		print "No menu option '{0}'".format(sel)
		return 1

	return 0


def main():
	
	print "PyBattle - Limited Christmas Edition (c) 2015"

	while runGameMenu() == 1:
		print "\n\n"	# add some space...

	# print game menu
	# run server or client?


# run main...
main()