# -*- coding: UTF-8 -*-
# pylint: disable=misplaced-comparison-constant,redefined-outer-name,no-self-use

import pytest

from tchart.renderers import SharpRenderer


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
        [3],
        [
            u'#',
        ],
    ),
    (
        4, 1,
        range(4),
        [
            u' .x#',
        ],
    ),
    (
        4, 2,
        range(4),
        [
            u'    ',
            u' .x#',
        ],
    ),
    (
        4, 2,
        range(0, 7, 2),
        [
            u'  .#',
            u' x##',
        ],
    ),

))
def test_render(width, height, values, expected_lines):
    renderer = SharpRenderer()
    assert renderer.render(width=width, height=height, values=values) == expected_lines
