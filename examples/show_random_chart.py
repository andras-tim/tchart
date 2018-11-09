#!/usr/bin/env python
import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tchart import Tchart  # noqa: E402


def main():
    t = Tchart(height=10, width=120)
    data = []

    for _ in range(random.randint(10, 100)):
        data.append(random.uniform(-100, 100))

    chart = t.render(data)
    print('\n'.join(chart))


if __name__ == '__main__':
    main()
