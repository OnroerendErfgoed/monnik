Monnik
======

Monnik is a Python library that makes it easier to query and interact with the 
REST API's provided by `Agentschap Onroerend Erfgoed <https://www.onroerenderfgoed.be>`_, 
such as the `Inventaris Onroerend Erfgoed <https://inventaris.onroerenderfgoed.be>`_.

.. image:: https://app.travis-ci.com/onroerenderfgoed/monnik.svg?branch=master
    :target: https://app.travis-ci.com/onroerenderfgoed/monnik
.. image:: https://coveralls.io/repos/onroerenderfgoed/monnik/badge.svg?branch=master
        :target: https://coveralls.io/github/onroerenderfgoed/monnik?branch=master
.. image:: https://scrutinizer-ci.com/g/onroerenderfgoed/monnik/badges/quality-score.png?b=master
        :target: https://scrutinizer-ci.com/g/onroerenderfgoed/monnik/?branch=master

.. image:: https://readthedocs.org/projects/monnik/badge/?version=latest
        :target: https://readthedocs.org/projects/monnik/?badge=latest
.. image:: https://badge.fury.io/py/monnik.png
        :target: http://badge.fury.io/py/monnik

Building the docs
-----------------

More information about this library can be found in `docs`. The docs can be 
built using `Sphinx <http://sphinx-doc.org>`_.

Please make sure you have installed Sphinx in the same environment where 
Monnik is present.

.. code-block:: bash

    # activate your virtual env
    $ pip install -r requirements.txt
    $ python setup.py develop
    $ cd docs
    $ make html
