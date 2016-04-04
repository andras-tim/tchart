#!/usr/bin/env python
import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tchart import Tchart
from tchart.decorators import FrameDecorator, PaperDecorator


def main():
    data = []
    for _ in range(random.randint(10, 100)):
        data.append(random.uniform(-100, 100))

    t = Tchart(height=15, width=80, decorators=[FrameDecorator(), PaperDecorator()])
    chart = '\n'.join(t.render(data))

    print(u'\n[ {title} ]\n{chart}\n'.format(title='FrameDecorator in PaperDecorator', chart=chart))


if __name__ == '__main__':
    main()
