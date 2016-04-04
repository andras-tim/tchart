# -*- coding: UTF-8 -*-
# pylint: disable=misplaced-comparison-constant,redefined-outer-name,no-self-use

import pytest

from tchart.renderers import DrawilleRenderer


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
        [4],
        [
            u'⡇',
        ],
    ),
    (
        1, 1,
        [0, 4],
        [
            u'⢸',
        ],
    ),
    (
        1, 1,
        [4, 4],
        [
            u'⣿',
        ],
    ),
    (
        3, 1,
        range(5),
        [
            u'⢀⣴⡇',
        ],
    ),
    (
        3, 2,
        range(4),
        [
            u'   ',
            u'⢀⣴⠀',
        ],
    ),
    (
        3, 2,
        range(0, 9, 2),
        [
            u'⠀⢠⡇',
            u'⢠⣿⡇',
        ],
    ),

))
def test_render(width, height, values, expected_lines):
    renderer = DrawilleRenderer()
    assert renderer.render(width=width, height=height, values=values) == expected_lines
