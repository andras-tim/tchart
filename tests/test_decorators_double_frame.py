# -*- coding: UTF-8 -*-
# pylint: disable=misplaced-comparison-constant,redefined-outer-name,no-self-use

import pytest

from tchart.decorators import DoubleFrameDecorator


@pytest.mark.parametrize('lines,expected_lines', (
    (
        [
            u'0',
        ],
        [
            u'╔═╗',
            u'║0║',
            u'╚═╝',
        ],
    ),
    (
        [
            u'orange',
            u' kiwi ',
        ],
        [
            u'╔══════╗',
            u'║orange║',
            u'║ kiwi ║',
            u'╚══════╝',
        ],
    ),
))
def test_decorate(lines, expected_lines):
    decorator = DoubleFrameDecorator()
    assert decorator.decorate(lines=lines) == expected_lines
