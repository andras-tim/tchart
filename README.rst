tchart
======

|PyPi| |Build| |DependencyStatus| |CodeQuality| |Coverage| |License|

Minimal chart renderer for fixed size canvas for Python.


Installation
------------

``pip install tchart``


Usage
-----

* simple way:

    .. code-block:: python

        from tchart import Tchart

        t = Tchart(height=10, width=80)

        data = [12.1, -2, 100]
        chart = t.render(data)

        print('\n'.join(chart))


* extended way:

    .. code-block:: python

        from tchart import Tchart
        from tchart.renderers import BoxRenderer
        from tchart.decorators import AxisDecorator

        t = Tchart(height=10, width=80, renderer=BoxRenderer(), decorators=[AxisDecorator(), ])

        data = [12.1, -2, 100]
        chart = t.render(data)

        print('\n'.join(chart))


Examples
--------

Please check the `examples <https://github.com/andras-tim/tchart/tree/master/examples>`__ directory.

* ``examples/show_all_renderers.py``
    |Renderers|

* ``examples/show_all_decorators.py``
    |Decorators|

* ``examples/show_stacked_decorators.py``
    |StackedDecorators|


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

.. |Renderers| image:: https://raw.githubusercontent.com/andras-tim/tchart/master/examples/screenshots/renderers.png
   :target: https://github.com/andras-tim/tchart/tree/master/examples
   :alt: Renderers
.. |Decorators| image:: https://raw.githubusercontent.com/andras-tim/tchart/master/examples/screenshots/decorators.png
   :target: https://github.com/andras-tim/tchart/tree/master/examples
   :alt: Decorators
.. |StackedDecorators| image:: https://raw.githubusercontent.com/andras-tim/tchart/master/examples/screenshots/stacked_decorators.png
   :target: https://github.com/andras-tim/tchart/tree/master/examples
   :alt: StackedDecorators
