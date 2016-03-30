tchart
======

|PyPi| |Build| |DependencyStatus| |CodeQuality| |Coverage| |License|

Minimal chart renderer for fixed size canvas for Python.


Installation
------------

``pip install tchart``


Usage
-----

.. code-block:: python

    from tchart.tchart import ChartRenderer

    renderer_object = ChartRenderer(height=10, width=80)
    data = [12.1, -2, 100]

    chart_string = renderer_object.render(data)
    print(chart_string)


Examples
--------

Please check the `examples <https://github.com/andras-tim/tchart/tree/master/examples>`__ directory.

|Example1|

|Example2|

|Example3|


Bugs
----

Bugs or suggestions? Visit the `issue tracker <https://github.com/andras-tim/tchart/issues>`__.


.. |Build| image:: https://travis-ci.org/andras-tim/tchart.svg?branch=master
   :target: https://travis-ci.org/andras-tim/tchart
   :alt: Build Status
.. |DependencyStatus| image:: https://gemnasium.com/andras-tim/tchart.svg
   :target: https://gemnasium.com/andras-tim/tchart
   :alt: Dependency Status
.. |PyPi| image:: https://img.shields.io/pypi/dm/tchart.svg
   :target: https://pypi.python.org/pypi/tchart
   :alt: Python Package
.. |License| image:: https://img.shields.io/badge/license-GPL%203.0-blue.svg
   :target: https://github.com/andras-tim/tchart/blob/master/LICENSE
   :alt: License

.. |CodeQuality| image:: https://www.codacy.com/project/badge/345af34d2f3c432bb528a0fb48167d92
   :target: https://www.codacy.com/app/andras-tim/tchart
   :alt: Code Quality
.. |Coverage| image:: https://coveralls.io/repos/andras-tim/tchart/badge.svg?branch=master&service=github
   :target: https://coveralls.io/r/andras-tim/tchart?branch=master&service=github
   :alt: Test Coverage

.. |IssueStats| image:: https://img.shields.io/github/issues/andras-tim/tchart.svg
   :target: http://issuestats.com/github/andras-tim/tchart
   :alt: Issue Stats

.. |Example1| image:: https://raw.githubusercontent.com/andras-tim/tchart/master/examples/screenshots/random1.png
   :target: https://github.com/andras-tim/tchart/tree/master/examples
   :alt: Random chart
.. |Example2| image:: https://raw.githubusercontent.com/andras-tim/tchart/master/examples/screenshots/random2.png
   :target: https://github.com/andras-tim/tchart/tree/master/examples
   :alt: Random chart 2
.. |Example3| image:: https://raw.githubusercontent.com/andras-tim/tchart/master/examples/screenshots/random3.png
   :target: https://github.com/andras-tim/tchart/tree/master/examples
   :alt: Random chart 3
