# -*- coding: UTF-8 -*-
# pylint: disable=misplaced-comparison-constant,redefined-outer-name,no-self-use

import pytest
from tchart.tchart import ChartRenderer


class TestChartRenderer:
    def test_can_create_render_instance(self):
        assert ChartRenderer()

    def test_can_not_create_1x1_renderer(self):
        with pytest.raises(Exception) as excinfo:
            ChartRenderer(height=1, width=1)
        assert str(excinfo.value) == 'Bad dimension; min 2x2'

    def test_render_without_data(self):
        r = ChartRenderer(height=4, width=15)
        data = []

        assert r.render(data) == (
            '│              ',
            '│              ',
            '│              ',
            '┼──────────────',
        )

    def test_render_without_any_scaling_and_shifting(self):
        r = ChartRenderer(height=4, width=26)
        data = list(range(25))

        assert r.render(data) == (
            '│                 ▁▂▃▄▅▆▇█',
            '│         ▁▂▃▄▅▆▇█████████',
            '│ ▁▂▃▄▅▆▇█████████████████',
            '┼─────────────────────────',
        )

    def test_render_with_shifting(self):
        r = ChartRenderer(height=4, width=26)
        data = list(range(-10, 15))

        assert r.render(data) == (
            '│                 ▁▂▃▄▅▆▇█',
            '│         ▁▂▃▄▅▆▇█████████',
            '│ ▁▂▃▄▅▆▇█████████████████',
            '┼─────────────────────────',
        )

    def test_render_with_vertical_scaling(self):
        r = ChartRenderer(height=4, width=26)
        data = list(range(0, 49, 2))

        assert r.render(data) == (
            '│                 ▁▂▃▄▅▆▇█',
            '│         ▁▂▃▄▅▆▇█████████',
            '│ ▁▂▃▄▅▆▇█████████████████',
            '┼─────────────────────────',
        )

    def test_render_with_horizontal_down_scaling(self):
        r = ChartRenderer(height=2, width=10)
        data = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]

        assert r.render(data) == (
            '│ ▁▂▃▄▅▆▇█',
            '┼─────────',
        )

    def test_render_with_horizontal_up_scaling(self):
        r = ChartRenderer(height=2, width=10)
        data = [0, 2, 4, 6, 8]

        assert r.render(data) == (
            '│ ▁▂▃▄▅▆▇█',
            '┼─────────',
        )

    def test_render_with_scaling_shifting_required_options(self):
        r = ChartRenderer(height=4, width=36)
        data = list([33.96, 260.66, 237.62, 204.36, 170.0, -36.21, 190.35, 56.37, -275.9, 108.19, 99.38, 137.86, 204.57,
                     176.97, 83.8, 204.65, 117.37, 197.27, 43.71, 84.79])

        assert r.render(data) == (
            '│ ▄█▇▇▆▅▄  ▁▄▁    ▁▁▂▃▅▅▄▃ ▃▅▃▂▄▃   ',
            '│▆████████▃███▃  ████████████████▇▇█',
            '│██████████████▃▇███████████████████',
            '┼───────────────────────────────────',
        )

    def test_boundaries(self):
        for width in range(2, 50):
            r = ChartRenderer(height=2, width=width)

            for data_count in range(width * 2):
                data = [0] * data_count

                try:
                    r.render(data)
                except Exception as e:  # pylint: disable=broad-except
                    assert False, 'exception={!s}, width={}, data_count={}'.format(e, width, data_count)
