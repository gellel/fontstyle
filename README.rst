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

.. role:: red
.. code-block:: python

    >>> fontstyle.apply('hello', 'bold')
    :red:`hello`
