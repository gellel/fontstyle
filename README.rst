fontstyle
=========
Terminal strings can be hard to read. Add some formatting!

installation
------------

pip

.. code-block:: console
    
    $ pip install fontstyle --upgrade

git

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

adding formatting to entire string

.. code-block:: python

    >>> fontstyle.apply('HELLO', 'bold')
    '\033[1mHELLO\033[0m'

using multiple formatting

.. code-block:: python
    
    >>> fontstyle.apply('HELLO', 'bold/red')
    '\033[1m\033[91mHELLO\033[0m'
    
    >>> fontstyle.apply('HELLO', ['BOLD'])
     '\033[1mHELLO\033[0m'

