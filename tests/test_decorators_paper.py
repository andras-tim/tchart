# -*- coding: UTF-8 -*-
# pylint: disable=misplaced-comparison-constant,redefined-outer-name,no-self-use

import pytest

from tchart.decorators import PaperDecorator


@pytest.mark.parametrize('lines,expected_lines', (
    (
        [
            u'0',
        ],
        [
            u'       .---.  ',
            u'      /  .  \\ ',
            u'     |\\_/|   |',
            u'     |   |  /|',
            u'  .--------  |',
            u' /  .-.   0 / ',
            u'|       |--\'  ',
            u'\\       |     ',
            u' \\     /      ',
            u'  `---\'       ',
        ],
    ),
    (
        [
            u'orange kako banana',
            u' kiwi ',
            u'mango',
            u'pulp',
        ],
        [
            u'                        .---.  ',
            u'                       /  .  \\ ',
            u'                      |\\_/|   |',
            u'                      |   |  /|',
            u'  .-------------------------\' |',
            u' /  .-.   orange kako banana  |',
            u'|  /   \\   kiwi               |',
            u'| |\\_.  | mango               |',
            u'|\\|  | /| pulp               / ',
            u'|       |-------------------\'  ',
            u'\\       |                      ',
            u' \\     /                       ',
            u'  `---\'                        ',
        ],
    ),
))
def test_decorate(lines, expected_lines):
    decorator = PaperDecorator()
    assert decorator.decorate(lines=lines) == expected_lines
