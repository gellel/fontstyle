fontstyle
=========
Terminal strings can be hard to read. Add some formatting!

installation
------------

pip install

.. code-block:: console
    
    $ pip install fontstyle --upgrade

git install

.. code-block:: console

    $ git clone https://github.com/gellel/fontstyle.git
    $ cd fontstyle
    $ python setup.py install
    

quick test
----------

.. code-block:: console

    $ python fontstyle '{hello world}(bold/red)'
    
usage
-----

**fontstyle.apply**

*adds formatting to the entire string.*

.. code-block:: python

    >>> fontstyle.apply('HELLO', 'bold')
    '\033[1mHELLO\033[0m'

*multiple formats can be supplied. split formats by non-alpha characters in strings. accepts sequences too.*

.. code-block:: python
    
    >>> fontstyle.apply('HELLO', 'bold/red')
    '\033[1m\033[91mHELLO\033[0m'

**fontstyle.erase**

*removes specific formatting from the entire string.*

.. code-block:: python
    
    >>> fontstyle.erase('\033[1m\033[91mHELLO\033[0m', 'red')
    '\033[5mHELLO\033[0m'

**fontstyle.preserve**

*removes all formatting from the entire string, keeping only the supplied argument references.*

.. code-block:: python
    
    >>> fontstyle.preserve('\033[1m\033[91mHELLO\033[0m', 'red')
    '\033[5mHELLO\033[0m'

**fontstyle.contains**

*finds assigned formatting for argument string.*

.. code-block:: python
    
    >>> fontstyle.preserve('\033[1m\033[91mHELLO\033[0m')
    ['BOLD', 'RED']
    
**fontstyle.patternize**

*adds 'beautification` syntax to argument string. syntax used in 'pretty' and 'prettify' function*

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
    
    >>> fontstyle.preserve('{HELLO}(RED) \033[1m\033[91mWORLD\033[0m')
    'HELLO \033[1m\033[91mWORLD\033[0m'

**fontstyle.strip**

*removes all 'beautifcation' syntax and formatting from argument string.*

.. code-block:: python
    
    >>> fontstyle.preserve('{HELLO}(RED) \033[1m\033[91mWORLD\033[0m')
    'HELLO WORLD'
    

    
