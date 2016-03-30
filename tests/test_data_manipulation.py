# -*- coding: UTF-8 -*-
# pylint: disable=misplaced-comparison-constant,redefined-outer-name,no-self-use

from tchart.tchart import DataManipulation


class TestDataManipulation(object):
    def test_shift_values(self):
        shift = DataManipulation.shift_values

        assert shift([0, 1, 2], 0) == [0, 1, 2]
        assert shift([0, 1, 2], 1) == [1, 2, 3]
        assert shift([0, 1, 2], -1.0) == [-1, 0, 1]
        assert shift([0.0, 0.1, 0.2], 1) == [1.0, 1.1, 1.2]
        assert shift([0.0, 0.1, 0.2], 1.5) == [1.5, 1.6, 1.7]

    def test_horizontal_scale_values(self):
        h_scale = DataManipulation.horizontal_scale_values

        assert h_scale([0, 1, 2, 3, 4, 5], 5) == [0.0, 1.25, 2.5, 3.75, 5.0]
        assert h_scale([0, 1, 2, 3], 4) == [0, 1, 2, 3]
        assert h_scale([0, 1, 2, 3], 2) == [0, 3]
        assert h_scale([0, 1, 2, 3], 1) == [1.5]
        assert h_scale([0, 1, 2, 3], 0) == []

        assert h_scale([0, 1, 2, 3], 7) == [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
        assert h_scale([0, 1, 2, 3], 13) == [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]

    def test_vertical_scale_values(self):
        v_scale = DataManipulation.vertical_scale_values

        assert v_scale([0, 1, 2], 0) == [0, 0, 0]
        assert v_scale([0, 1, 2], 1) == [0, 1, 2]
        assert v_scale([0, 1, 2], 2) == [0, 2, 4]
        assert v_scale([0, 1, 2], 0.5) == [0, 0.5, 1]
