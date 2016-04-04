# -*- coding: UTF-8 -*-
# pylint: disable=misplaced-comparison-constant,redefined-outer-name,no-self-use

import pytest

from tchart.decorators import AxisDecorator


@pytest.mark.parametrize('lines,expected_lines', (
    (
        [
            u'0',
        ],
        [
            u'│0',
            u'┼─',
        ],
    ),
    (
        [
            u'orange',
            u' kiwi ',
        ],
        [
            u'│orange',
            u'│ kiwi ',
            u'┼──────',
        ],
    ),
))
def test_decorate(lines, expected_lines):
    decorator = AxisDecorator()
    assert decorator.decorate(lines=lines) == expected_lines
