constants
=========

fontstyles modules has a few referrential constants. these generally contain escape sequences for ansi formatting.

**fontstyle.COLORS**

*dictionary reference for colour escape sequences.*

.. code-block:: python

    >>> fontstyle.COLORS
    { 'BLACK': '\033[30m', ... }

**fontstyle.FORMATTING**

*dictionary reference for font weights and styling escape sequences.*

.. code-block:: python

    >>> fontstyle.FORMATTING
    { 'BLINK': '\033[5m', ... }

**fontstyle.STYLES**

*dictionary reference for both font colours and styling escape sequences.*

.. code-block:: python

    >>> fontstyle.STYLES
    { 'BLACK': '\033[30m', ..., 'BLINK': '\033[5m', ... }

**fontstyle.BEAUTIFICATION**

*regular expression pattern for substring formatting. used in 'pretty' and 'prettify'.*

.. code-block:: python

    >>> fontstyle.BEAUTIFICATION
    r'\{[^\{]+\}\([^\(]+\)'

**fontstyle.ESCAPES**

*regular expression pattern for finding ansi escape strings.*

.. code-block:: python

    >>> fontstyle.ESCAPES
    r'\x1b[^m]*m'

**fontstyle.STRSTYLE**

*regular expression pattern for finding formatting reference substrings.*

.. code-block:: python

    >>> fontstyle.STRSTYLE
    r'\((.*?)\)'

**fontstyle.STRSET**

*regular expression pattern for finding substrings requiring formatting.*

.. code-block:: python

    >>> fontstyle.STRSTYLE
    r'\((.*?)\)'


methods
=======

fontstyles module accepts empty arguments in listed api. use empty for example output.

**fontstyle.apply**

*adds formatting to the entire argument string.*

.. code-block:: python

    >>> fontstyle.apply('HELLO', 'bold')
    '\033[1mHELLO\033[0m'

*multiple formats can be supplied. split format references by non-alpha characters in strings. accepts sequences of strings.*

.. code-block:: python
    
    >>> fontstyle.apply('HELLO', 'bold/red')
    '\033[1m\033[91mHELLO\033[0m'

**fontstyle.erase**

*removes specific formatting from the entire argument string. split format references by non-alpha characters in strings. accepts sequences of strings.*

.. code-block:: python
    
    >>> fontstyle.erase('\033[1m\033[91mHELLO\033[0m', 'red')
    '\033[5mHELLO\033[0m'

**fontstyle.preserve**

*removes all formatting from the entire argument string, keeping only the supplied argument references. split format references by non-alpha characters in strings. accepts sequences of strings.*

.. code-block:: python
    
    >>> fontstyle.preserve('\033[1m\033[91mHELLO\033[0m', 'red')
    '\033[5mHELLO\033[0m'

**fontstyle.contains**

*finds assigned formatting for argument string.*

.. code-block:: python
    
    >>> fontstyle.preserve('\033[1m\033[91mHELLO\033[0m')
    ['BOLD', 'RED']
    
**fontstyle.patternize**

*adds 'beautification` syntax to argument string. syntax used in 'pretty' and 'prettify' function. split format references by non-alpha characters in strings. accepts sequences of strings.*

.. code-block:: python
    
    >>> fontstyle.patternize('HELLO', 'red')
    '{HELLO}(RED)'

*lambda substitutes are added if no arguments are provided.*

.. code-block:: python
    
    >>> fontstyle.patternize()
    '{%s}(%s)'

**fontstyle.normalize**

*removes all 'beautifcation' syntax from argument string.*

.. code-block:: python
    
    >>> fontstyle.normalize('{HELLO}(RED) \033[1m\033[91mWORLD\033[0m')
    'HELLO \033[1m\033[91mWORLD\033[0m'

**fontstyle.strip**

*removes all 'beautifcation' syntax and formatting from argument string.*

.. code-block:: python
    
    >>> fontstyle.strip('{HELLO}(RED) \033[1m\033[91mWORLD\033[0m')
    'HELLO WORLD'

**fontstyle.pretty**

*adds formatting to strings contained in 'beautifcation' syntax.*

.. code-block:: python
    
    >>> fontstyle.pretty('{HELLO}(RED)')
    '\033[91mWORLD\033[0m'

*`beautification` syntax can be repeated in the same string to create multiple instances of formatting.*

.. code-block:: python
    
    >>> fontstyle.pretty('{HELLO}(RED) this is an {EXAMPLE}(BLUE/BOLD)')
    '\033[91mWORLD\033[0m this is an \033[94m\033[1mEXAMPLE\033[0m'

**fontstyle.ugly**

*removes all formatting from argument string.*

.. code-block:: python
    
    >>> fontstyle.ugly('\033[91mHELLO\033[0m')
    'HELLO'
    
**fontstyle.prettify**

*adds formatting to arguments in args sequence contained in 'beautifcation' syntax.*

.. code-block:: python
    
    >>> fontstyle.prettify('{HELLO}(RED)', '{WORLD}(BLUE)', 'FOO')
    ['\033[91mHELLO\033[0m', '\033[94mWORLD\033[0m', 'FOO']
    
**fontstyle.uglify**

*removes formatting from arguments in args sequence.*

.. code-block:: python
    
    >>> fontstyle.uglify('\033[91mHELLO\033[0m', '\033[94mWORLD\033[0m')
    ['HELLO', 'WORLD']
 
 **fontstyle.numbers**

*finds integer value for supplied formatting reference.*

.. code-block:: python
    
    >>> fontstyle.numbers('BOLD', 'RED', ...)
    [1, 91]
 
 **fontstyle.escapes**

*finds string escape sequence for supplied formatting reference.*

.. code-block:: python
    
    >>> fontstyle.escapes('\033[91mHELLO\033[0m', '\033[94mWORLD\033[0m')
    ['HELLO', 'WORLD']

**fontstyle.options**

*creates list of formatting references.*

.. code-block:: python
    
    >>> fontstyle.options()
    ['BOLD', 'RED', ...]

