# -*- coding: UTF-8 -*-
# pylint: disable=misplaced-comparison-constant,redefined-outer-name,no-self-use

import pytest

from tchart.renderers import BoxRenderer


@pytest.mark.parametrize('width,height,values,expected_lines', (
    (
        1, 1,
        [0],
        [
            u' ',
        ],
    ),
    (
        1, 1,
        [8],
        [
            u'█',
        ],
    ),
    (
        9, 1,
        range(9),
        [
            u' ▁▂▃▄▅▆▇█',
        ],
    ),
    (
        9, 2,
        range(9),
        [
            u'         ',
            u' ▁▂▃▄▅▆▇█',
        ],
    ),
    (
        10, 2,
        range(0, 17, 2),
        [
            u'     ▂▄▆█ ',
            u' ▂▄▆█████ ',
        ],
    ),

))
def test_render(width, height, values, expected_lines):
    renderer = BoxRenderer()
    assert renderer.render(width=width, height=height, values=values) == expected_lines


def test_does_not_raise_index_error():
    renderer = BoxRenderer()
    renderer.render(width=1, height=1, values=[8.1])
