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
    
using multiple formats. 
separate styles using non alpha or using lists.

.. code-block:: python
    >>> fontstyle.apply('HELLO', 'bold/red')
    '\033[1m\033[91mHELLO\033[0m'
    
erasing certain formatting from entire string

.. code-block:: python
    >>> fontstyle.apply('\033[1m\033[91mHELLO\033[0m', 'red')
    '\033[5mHELLO\033[0m'
