#!/usr/bin/env python
import os
import random
import sys
from collections import OrderedDict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tchart import Tchart
from tchart.renderers import BoxRenderer, SharpRenderer


RENDERERS = OrderedDict((
    ('BoxRenderer - default', BoxRenderer()),
    ('SharpRenderer', SharpRenderer()),
))


def main():
    data = []
    for _ in range(random.randint(10, 100)):
        data.append(random.uniform(-100, 100))

    for title, renderer in RENDERERS.items():
        t = Tchart(height=8, width=80, renderer=renderer)
        chart = '\n'.join(t.render(data))

        print(u'\n[ {title} ]\n{chart}\n'.format(title=title, chart=chart))


if __name__ == '__main__':
    main()
