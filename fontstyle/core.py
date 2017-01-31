# -*- coding: utf-8 -*-

#########################
### File requirements ###
#########################

### import future print function
from __future__ import print_function
### import regexp module
import re

###############################
### File import identifiers ###
###############################

__all__ = ['apply', 'erase', 'preserve', 'contains', 'patternize', 
	'normalize', 'strip', 'pretty', 'ugly', 'prettify', 
	'uglify', 'escapes', 'numbers', 'options', 'STYLES', 
	'COLORS', 'FORMATTING', 'BEAUTIFICATION', 'ESCAPES',
	'STRSTYLE', 'STRSET']

##################################
### Font formatting references ###
##################################

BLACK = '\033[30m'
BLUE = '\033[94m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
GREEN = '\033[92m'
PURPLE = '\033[95m'
RED = '\033[91m'
YELLOW = '\033[93m'
WHITE = '\033[37m'

BLACK_BG = '\033[40m'
RED_BG = '\033[41m'
GREEN_BG = '\033[42m'
YELLOW_BG = '\033[43m'
BLUE_BG = '\033[44m'
PURPLE_BG = '\033[45m'
CYAN_BG = '\033[46m'
WHITE_BG = '\033[47m'

BOLD = '\033[1m'
FAINT = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
INVERSE = '\033[7m'
HIDDEN = '\033[8m'
STRIKE = '\033[9m'
END = '\033[0m'

COLORS_FG = {
	'BLACK': BLACK,
	'BLUE': BLUE, 
	'CYAN': CYAN, 
	'DARKCYAN': DARKCYAN, 
	'GREEN': GREEN, 
	'PURPLE': PURPLE, 
	'RED': RED,
	'YELLOW': YELLOW, 
	'WHITE': WHITE }

COLORS_BG = {
	'BLACK_BG': BLACK_BG,
	'BLUE_BG': BLUE_BG, 
	'CYAN_BG': CYAN_BG, 
	'GREEN_BG': GREEN_BG, 
	'PURPLE_BG': PURPLE_BG, 
	'RED_BG': RED_BG,
	'YELLOW_BG': YELLOW_BG, 
	'WHITE_BG': WHITE_BG }

COLORS = dict(COLORS_FG, 
	**COLORS_BG)

FORMATTING = {
	'BLINK': BLINK,
	'BOLD': BOLD,
	'FAINT': FAINT,
	'HIDDEN': HIDDEN,
	'ITALIC': ITALIC,
	'INVERSE': INVERSE,
	'STRIKE': STRIKE,
	'UNDERLINE': UNDERLINE,
	'END': END }

STYLES = dict(COLORS, 
	**FORMATTING)

#############################
### Font regex references ###
#############################

BEAUTIFICATION = r'\{[^\{]+\}\([^\(]+\)'
ESCAPES = r'\x1b[^m]*m'
STRSTYLE = r'\((.*?)\)'
STRSET = r'\{(.*?)\}'

#############################
### Main module functions ###
#############################

def apply (string = 'HELLO', formatting = 'BLUE/INVERSE/BOLD/UNDERLINE'):
	"""Applies escaped style strings against argument string.
		
	Concatenates selected attribute escape sequence from styles dictionary. 
	Applied escaped sequence can be revealed through calling 'repr' function against returned string.
	Formatting is only applied if the attribute(s) are found in defined style dictionary.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.apply('hello!', ['BOLD', 'BLUE'] or 'BOLD/BLUE')

	'\033[1m\033[94mhello!\033[0m'
	"""

	# Named arguments #

	# @parameter: <string>, @type: <str>, @required: <false>
	# @description: Character string to receive formatting.

	# @parameter: <formatting>, @type: <str/list/tuple>, @required: <false>
	# @description: Sequence or string containing reference to key in styles dictionary.


	# Set formatting reference list.
	# String arguments are split using non-alpha characters.
	# Use a non-alpha character to denote a new argument.
	formatting = map(str, formatting) if type(formatting) in [list, tuple] else re.split(r'\W', str(formatting))

	# Concatenate escape sequence substring.
	# Join string if reference is found in styles dictionary.
	styles = ''.join([STYLES[i] for i in map(str.upper, formatting) if i in STYLES and i != 'END'])

	# @return: @type: <str>
	return styles + str(string) + END


def erase (string = '\033[91m\033[5mHELLO!\033[0m', formatting = 'RED/BLINK'):
	"""Removes specific escaped colour string from argument string.
		
	Substitutes attribute escape sequence with whitespace. 
	Remaining escaped sequence can be revealed through calling 'repr' function against returned string.
	Formatting is only removed if the attribute(s) are found in defined style dictionary.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.erase('\033[94mhello!\033[0m', ['BOLD', 'BLUE'] or 'BOLD/BLUE')

	'hello!'
	"""

	# Named arguments #

	# @parameter: <string>, @type: <str>, @required: <false>
	# @description: Character string containing formatting.

	# @parameter: <formatting>, @type: <str/list/tuple>, @required: <false>
	# @description: Sequence or string containing reference to key in styles dictionary.


	# Set formatting reference list.
	# String arguments are split using non-alpha characters.
	# Use a non-alpha character to denote a new argument.
	formatting = map(str, formatting) if type(formatting) in [list, tuple] else re.split(r'\W', str(formatting))

	# Set required attributes list. Create list from found formatting keys in styles dictionary.
	# Escape each attribute reference for use in regular expression.
	collections = [re.escape(STYLES[i]) for i in map(str.upper, formatting) if i in STYLES]

	# Substitute formatting in supplied string using empty string.
	string = re.sub(r'|'.join(collections), '', str(string)) 

	# Test substituted string contains any escaped strings.
	if re.match(ESCAPES, string): 
		# Test substituted string does not contain ending escape string.
		if not re.match(re.escape(END), string):
			# Concatenate ending escape string to prevent formatting leak.
			string = string + END
	# String does not contain any escaped formatting strings.
	else:
		# Substitute ending escape string using empty substring.
		string = re.sub(re.escape(END), '', string)

	# @return: @type: <str>
	return string


def preserve (string = '\033[91m\033[5mHELLO!\033[0m', formatting = 'BLINK'):
	"""Removes all escaped colour strings from argument string, except styles defined in parameters.
		
	Substitutes attribute escape sequence with whitespace. 
	Remaining escaped sequence can be revealed through calling 'repr' function against returned string.
	Formatting is only removed if the attribute(s) are found in defined style dictionary.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.preserve('\033[94mhello!\033[0m', ['BOLD', 'BLUE'] or 'BOLD/BLUE')

	'\033[94mhello!\033[0m'
	"""

	# Named arguments #

	# @parameter: <string>, @type: <str>, @required: <false>
	# @description: Character string containing formatting.

	# @parameter: <formatting>, @type: <str/list/tuple>, @required: <false>
	# @description: Sequence or string containing reference to key in styles dictionary.
	

	# Set formatting reference list.
	# String arguments are split using non-alpha characters.
	# Use a non-alpha character to denote a new argument.
	formatting = map(str, formatting) if type(formatting) in [list, tuple] else re.split(r'\W', str(formatting))

	# Set formatting references to uppercase.
	formatting = map(str.upper, formatting)

	# Set required attributes list. Create list from found formatting keys in styles dictionary.
	# Escape each attribute reference for use in regular expression.
	collections = [re.escape(STYLES[i]) for i in STYLES if i not in formatting]

	# Substitute formatting in supplied string using empty string.
	string = re.sub(r'|'.join(collections), '', str(string)) 
	
	# Test substituted string contains any escaped strings.
	if re.match(ESCAPES, string): 
		# Test substituted string does not contain ending escape string.
		if not re.match(re.escape(END), string):
			# Concatenate ending escape string to prevent formatting leak.
			string = string + END
	# String does not contain any escaped formatting strings.
	else:
		# Substitute ending escape string using empty substring.
		string = re.sub(re.escape(END), '', string)

	# @return: @type: <str>
	return string


def contains (string = '\033[91m\033[5mHELLO!\033[0m'):
	"""Finds escaped colour strings dictionary names.
		 
	Style name references are defined in styles dictionary.
	Ending style string is included in found styles.
	Non defined escape sequences are also found, but are not appended to returned list.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.contains('\033[91m\033[5mhello!\033[0m')

	['RED', 'BLINK', 'END']
	"""

	# Named arguments #

	# @parameter: <string>, @type: <str>, @required: <false>
	# @description: String containing formatting escape sequence.


	# Get defined keys from styles dictionary.
	# Used as returned value.
	keys = STYLES.keys()
	
	# Get defined key values from styles dictionary.
	# Used as expression comparison.
	values = STYLES.values()

	# Set regular expression for collecting formatting substrings.
	# Finds escaped strings within argument string.
	substrings = re.compile(ESCAPES, flags = re.MULTILINE|re.DOTALL)

	# Find substrings in string containing formatting.
	matches = substrings.findall(string)

	# @return: @type: <list>
	return [keys[values.index(i)] for i in matches]


def patternize (string = 'HELLO!', formatting = 'BLUE/BOLD'):
	"""Formats string to be matchable pattern for prett(y/ify).
	
	Substitutes empty strings as lambda referenes.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.patternize('hello!', ['BOLD', 'BLUE'] or 'BOLD/BLUE')

	'{hello!}(BOLD/BLUE)'
	"""

	# Named arguments #

	# @parameter: <string>, @type: <str>, @required: <false>
	# @description: Character string to be encased.

	# @parameter: <formatting>, @type: <str/list/tuple>, @required: <false>
	# @description: Sequence or string containing reference to key in styles dictionary.
	

	# Set string argument.
	string = str(string) if string is not None else '%s'

	# Set formatting reference list.
	# String arguments are split using non-alpha characters.
	# Use a non-alpha character to denote a new argument.
	formatting = map(str, formatting) if type(formatting) in [list, tuple] else re.split(r'\W', str(formatting))

	# Set formatting references to uppercase.
	# Filter empty items from sequence.
	formatting = filter(None, map(str.upper, formatting))

	# Join strings if list is not empty.
	# Use lambda string if empty.
	formatting = '/'.join(formatting) if bool(formatting) else '%s'

	# @return: @type: <str>
	return ''.join(['{', string, '}', '(', formatting, ')'])


def normalize (string = '{HELLO!}(BOLD/RED)'):
	"""Substitute beautification pattern substrings.
	
	Substrings containing formatting are not edited.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.normalize('{hello}(bold)')

	'hello'
	"""

	# Set string argument.
	string = str(string) if string is not None else '%s'

	# Set regular expression for collecting beautification substrings.
	# Finds strings between matching pattern {string}(styles).
	collections = re.compile(BEAUTIFICATION, flags = re.MULTILINE|re.DOTALL)

	# Set regular expression for collecting text requiring formatting.
	# Finds strings between matching pattern {substring}
	substrings = re.compile(STRSET, re.IGNORECASE)

	# Find substrings in string requiring formatting.
	matches = collections.findall(string)

	# Iterate over collected substrings from pattern for string.
	for i in range(0, len(matches)):
		# Find strings matching non-style substring regex.
		# Set expression group to joined string.
		substring = ''.join(substrings.findall(matches[i]) or [])
		# Substitute found substring with primary string.
		string = re.sub(re.escape(matches[i]), substring, string)

	# @return: @type: <str>
	return string


def strip (string = '{HELLO}(bold) \033[30mWORLD\033[0m'):
	"""Substitutes all module beautification and formatting.

	Substrings that do not match module patterns are not edited.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.strip('{hello}(bold) \033[30mworld\033[0m')

	'hello world'
	"""

	# Named arguments #

	# @parameter: <string>, @type: <str>, @required: <false>
	# @description: String requiring style formatting.
	

	# @return: @type: <str>
	return ugly(normalize(string))


def pretty (string = '{HELLO!}(BOLD/BLUE)'):
	"""Edits substrings in string contained in beautification syntax.

	Substrings containing formatting syntax are substituted.
	Unformatted or incorrect references are not removed from string.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.pretty('hello {world}(bold,red)')

	'hello \033[1m\033[94mworld\033[0m'
	"""

	# Named arguments #

	# @parameter: <string>, @type: <str>, @required: <false>
	# @description: String requiring style formatting.
	

	# Set argument as string type.
	string = str(string)

	# Set regular expression for collecting beautification substrings.
	# Finds strings between matching pattern {string}(styles).
	collections = re.compile(BEAUTIFICATION, flags = re.MULTILINE|re.DOTALL)

	# Set regular expression for collecting text requiring formatting.
	# Finds strings between matching pattern {substring}
	substrings = re.compile(STRSET, re.IGNORECASE)

	# Set regular expression for collecting formatting substrings.
	# Finds strings between matching pattern (styles).
	formatting = re.compile(STRSTYLE, re.IGNORECASE)

	# Find substrings in string requiring formatting.
	matches = collections.findall(string)

	# Iterate over collected substrings from pattern for string.
	for i in range(0, len(matches)):
		# Find strings matching non-style substring regex.
		# Set expression group to joined string.
		substring = ''.join(substrings.findall(matches[i]) or [])
		# Find strings matching style formatting regex.
		# Set expression group to joined string.
		styles = ''.join(formatting.findall(matches[i] or []))
		# Substitute found substring with formatted substitution string.
		string = re.sub(re.escape(matches[i]), apply(substring, styles), string)

	# @return: @type: <str>
	return string


def ugly (string = '\033[1m\033[94mHELLO!\033[0m'):
	"""Cleans formatting escape sequences from string.

	Substrings encased in formatting are substituted.
	Escaped strings that are not style strings are not removed from string.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.ugly('\033[1m\033[94mhello\033[0m')

	'hello'
	"""
	
	# Named arguments #

	# @parameter: <string>, @type: <str>, @required: <false>
	# @description: String requiring style formatting.
	

	# Set argument as string type.
	string = str(string)

	# Set string substitution regex.
	# Substitutes multiple matches from supplied arguments.
	# Unsupported characters are redefined as empty strings.
	# Uses joined escaped strings from styles dictionary.
	substitution = re.compile(r'|'.join([re.escape(STYLES[i]) for i in STYLES]), flags = re.MULTILINE|re.DOTALL)

	# @return: @type: <str>
	return substitution.sub('', string)


def prettify (*args):
	"""Edits strings in argument sequence contained in beautification syntax.

	Substrings containing formatting syntax are substituted.
	Unformatted or incorrect references are not removed from string.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.prettify('hello {world}(bold,red)', ...)

	['hello \033[1m\033[94mworld\033[0m', ...]
	"""

	# Sequence arguments #

	# @parameter: <args>, @type: <tuple>, @required: <false>
	# @description: Strings requiring style formatting.
	

	# Set variable arguments sequence to mutable list.
	# Edit arguments to be string type.
	args = map(str, args)

	# Set regular expression for collecting beautification substrings.
	# Finds strings between matching pattern {string}(styles).
	collections = re.compile(BEAUTIFICATION, flags = re.MULTILINE|re.DOTALL)

	# Set regular expression for collecting text requiring formatting.
	# Finds strings between matching pattern {substring}
	substrings = re.compile(STRSET, re.IGNORECASE)

	# Set regular expression for collecting formatting substrings.
	# Finds strings between matching pattern (styles).
	formatting = re.compile(STRSTYLE, re.IGNORECASE)

	# Iterate over supplied argument sequence.
	for i in range(0, len(args)):
		# Find substrings in string requiring formatting.
		matches = collections.findall(args[i])
		# Iterate over collected substrings for string at index.
		for j in range(0, len(matches)):
			# Find strings matching non-style substring regex.
			# Set expression group to joined string.
			string = ''.join(substrings.findall(matches[j]) or [])
			# Find strings matching style formatting regex.
			# Set expression group to joined string.
			styles = ''.join(formatting.findall(matches[j] or []))
			# Substitute found substring with formatted substitution string.
			args[i] = re.sub(re.escape(matches[j]), apply(string, styles), args[i])
	
	# @return: @type: <list>
	return args


def uglify (*args):
	"""Edits strings to contain no formatting.

	Substrings encased in formatting are substituted.
	Escaped strings that are not style strings are not removed from string.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.ugly('\033[1m\033[94mhello\033[0m', ...)

	['hello']
	"""
	
	# Sequence arguments #

	# @parameter: <args>, @type: <tuple>, @required: <false>
	# @description: Strings requiring formatting.
	

	# Set string substitution regex.
	# Substitutes multiple matches from supplied arguments.
	# Unsupported characters are redefined as empty strings.
	# Uses joined escaped strings from styles dictionary.
	substitution = re.compile(r'|'.join([re.escape(STYLES[i]) for i in STYLES]), flags = re.MULTILINE|re.DOTALL)

	# @return: @type: <list>
	return [substitution.sub('', str(i)) for i in args]


def numbers (*args):
	"""Finds number reference for formatting option."""

	"""
	>>> import fontstyle
	>>> fontstyle.escapes('bold', 'red')
	
	[1, 91]
	"""

	# @parameter: <formatting>, @type: <tuple>, @required: <false>
	# @description: String containing reference to key in styles dictionary.
	

	# Set variable arguments sequence to mutable list.
	# Edit arguments to be string type.
	args = map(str, args)

	# @reutrn: @type: <list>
	return [int(re.search(r'\x1b([^m])*m', STYLES[i]).group(1)) for i in map(str.upper, args) if i in STYLES]


def escapes (*args):
	"""Finds escape sequences for formatting option.
	
	Careful, printing an item may cause your terminal to be formatted as per sequence.
	Safest to use repr(escapes('bold')[0]) to prevent overflow.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.escapes('bold', 'red')
	
	['\033[1m', '\033[91m']
	"""

	# @parameter: <formatting>, @type: <tuple>, @required: <false>
	# @description: String containing reference to key in styles dictionary.
	

	# Set variable arguments sequence to mutable list.
	# Edit arguments to be string type.
	args = map(str, args)

	# @reutrn: @type: <list
	return [STYLES[i] for i in map(str.upper, args) if i in STYLES]


def options ():
	"""Finds formatting string parameters.
	
	Selects keys from styles dictionary.
	"""

	"""
	>>> import fontstyle
	>>> fontstyle.options()

	'['BOLD',...]'
	"""

	# @return: @type: <list>
	return list(STYLES.keys())


def main (*args):
	"""Font module main function.
	
	Formats string using beautification handler.
	"""

	"""	
	$ python fontstyle.py '{H}(BOLD){I}(RED)'
	
	'\033[94mH\033[0m\033[96mI\033[0m'
	"""


	# Sequence arguments #

	# @parameter: <args>, @type: <tuple>, @required: <false>
	# @description: Strings requiring style formatting.


	# @return: @type: <None>
	print(' '.join(prettify(*args)))

															