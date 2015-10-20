#!/usr/bin/env python3
import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tchart.tchart import ChartRenderer


def main():
    r = ChartRenderer(height=10, width=120)
    data = []

    for i in range(random.randint(10, 100)):
        data.append(random.uniform(-100, 100))

    chart = r.render(data)
    print('\n'.join(chart))


if __name__ == '__main__':
    main()
