#!/usr/bin/env python
import os
import random
import sys
from collections import OrderedDict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tchart import Tchart  # noqa: E402
from tchart.decorators import AxisDecorator, FrameDecorator, ThinFrameDecorator, DoubleFrameDecorator, \
                              PaperDecorator  # noqa: E402


DECORATORS = OrderedDict((
    ('AxisDecorator - default', AxisDecorator()),
    ('FrameDecorator', FrameDecorator()),
    ('DoubleFrameDecorator', DoubleFrameDecorator()),
    ('ThinFrameDecorator', ThinFrameDecorator()),
    ('PaperDecorator', PaperDecorator()),
))


def main():
    data = []
    for _ in range(random.randint(10, 100)):
        data.append(random.uniform(-100, 100))

    for title, decorator in DECORATORS.items():
        t = Tchart(height=14, width=80, decorators=[decorator])
        chart = '\n'.join(t.render(data))

        print(u'\n[ {title} ]\n{chart}\n'.format(title=title, chart=chart))


if __name__ == '__main__':
    main()
