import numpy
import pytest

from tchart.decorators import ChartDecorator
from tchart.renderers import ChartRenderer
from tchart.tchart import Tchart


class FakeRenderer(ChartRenderer):
    def __init__(self, resolution_horizontal=1, resolution_vertical=1, render_results=None):
        self.render_calls = []
        self._resolution_horizontal = resolution_horizontal
        self._resolution_vertical = resolution_vertical
        self._render_results = render_results or ()

    @property
    def char_resolution_horizontal(self):
        return self._resolution_horizontal

    @property
    def char_resolution_vertical(self):
        return self._resolution_vertical

    def render(self, **kwargs):
        self.render_calls.append(kwargs)
        return self._render_results


class FakeDecorator(ChartDecorator):
    def __init__(self, width_left=0, width_top=0, width_right=0, width_bottom=0, decorator_results=None):
        self.decorate_calls = []
        self._width_left = width_left
        self._width_top = width_top
        self._width_right = width_right
        self._width_bottom = width_bottom
        self._decorator_results = decorator_results or ()

    @property
    def width_left(self):
        return self._width_left

    @property
    def width_top(self):
        return self._width_top

    @property
    def width_right(self):
        return self._width_right

    @property
    def width_bottom(self):
        return self._width_bottom

    def decorate(self, **kwargs):
        self.decorate_calls.append(kwargs)
        return self._decorator_results


def test_can_create_default_render_instance():
    assert Tchart()


@pytest.mark.parametrize('canvas_width,canvas_height', (
    (1, 1),
    (1, 100),
    (100, 1),
    (100, 100),
))
def test_size_is_equal_chart_size_wo_decorators_canvas(canvas_width, canvas_height):
    renderer = FakeRenderer()

    t = Tchart(canvas_width, canvas_height, renderer=renderer, decorators=None)

    assert t.canvas_width == canvas_width
    assert t.canvas_height == canvas_height
    assert t.chart_width == canvas_width
    assert t.chart_height == canvas_height


@pytest.mark.parametrize('canvas_size,expected_min_sizes', (
    ((0, 0), (1, 1)),
    ((1, 0), (1, 1)),
    ((0, 1), (1, 1)),
    ((-10, 1), (1, 1)),
    ((1, -10), (1, 1)),
    ((-10, -10), (1, 1)),
))
def test_too_small_canvas_size_wo_decorators(canvas_size, expected_min_sizes):
    min_width, min_height = expected_min_sizes

    with pytest.raises(ValueError) as excinfo:
        Tchart(*canvas_size, renderer=FakeRenderer(), decorators=None)

    expected_message = 'Bad dimension; min {min_width}x{min_height}'.format(min_width=min_width, min_height=min_height)
    assert str(excinfo.value) == expected_message


@pytest.mark.parametrize('decorators_withs,expected_chart_sizes', (
    (
        (),
        (100, 100),
    ),
    (
        (
            (),
        ),
        (100, 100),
    ),
    (
        (
            (1, 2, 3, 4),
        ),
        (96, 94),
    ),
    (
        (
            (1, 2, 3, 4),
            (5, 6, 7, 8),
        ),
        (84, 80),
    ),
    (
        (
            (1, 2, 3, 4),
            (1, 2, 3, 4),
            (1, 2, 3, 4),
            (1, 2, 3, 4),
            (1, 2, 3, 4),
        ),
        (80, 70),
    ),

))
def test_decorators_reduces_chart_size(decorators_withs, expected_chart_sizes):
    expected_chart_width, expected_chart_height = expected_chart_sizes

    decorators = [FakeDecorator(*decorator_withs) for decorator_withs in decorators_withs]

    t = Tchart(width=100, height=100, renderer=FakeRenderer(), decorators=decorators)

    assert t.chart_width == expected_chart_width
    assert t.chart_height == expected_chart_height


def sequence(count, step):
    """
    :type count: int
    :type step: int or float
    :rtype: list
    """
    return [step * i for i in range(count)]


@pytest.mark.parametrize('canvas_size,values,expected_normalized_values', (
    # shift_values
    ((11, 10), range(-5, 5), sequence(11, step=1.0)),
    ((11, 10), range(0, 10), sequence(11, step=1.0)),
    ((11, 10), range(20, 30), sequence(11, step=1.0)),

    # horizontal_scale_values
    ((11, 10), sequence(101, step=0.1), sequence(11, step=1.0)),
    ((101, 10), sequence(11, step=1.0), sequence(101, step=0.1)),

    # vertical_scale_values
    ((11, 10), sequence(101, step=1.0), sequence(11, step=1.0)),
    ((11, 10), sequence(3, step=1.0), sequence(11, step=1.0)),
    ((11, 100), sequence(11, step=1.0), sequence(11, step=10.0)),
))
def test_render_calls_renderer(canvas_size, values, expected_normalized_values):
    renderer = FakeRenderer()

    t = Tchart(*canvas_size, renderer=renderer, decorators=None)
    t.render(values=values)

    assert len(renderer.render_calls) == 1

    render_call = renderer.render_calls[0]
    assert set(render_call.keys()) == {'width', 'height', 'values'}
    assert (render_call['width'], render_call['height']) == canvas_size

    try:
        numpy.testing.assert_allclose(render_call['values'], expected_normalized_values)
    except AssertionError as e:
        raise e


@pytest.mark.parametrize('canvas_size,decorators_widths,expected_render_size', (
    # single decorator
    ((50, 50), [(0, 0, 0, 0)], (50, 50)),
    ((50, 50), [(1, 0, 0, 0)], (50 - 1, 50)),
    ((50, 50), [(0, 1, 0, 0)], (50, 50 - 1)),
    ((50, 50), [(0, 0, 1, 0)], (50 - 1, 50)),
    ((50, 50), [(0, 0, 0, 1)], (50, 50 - 1)),
    ((50, 50), [(1, 2, 3, 4)], (50 - 1 - 3, 50 - 2 - 4)),

    # multi-decorator
    ((50, 50), [(1, 2, 3, 4), (0, 0, 0, 0)], (46, 44)),
    ((50, 50), [(1, 2, 3, 4), (2, 3, 4, 5)], (40, 36)),
    ((50, 50), [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)], (32, 26)),
))
def test_renderer_reduces_render_size_by_decorators(canvas_size, decorators_widths, expected_render_size):
    renderer = FakeRenderer()
    decorators = [FakeDecorator(*widths) for widths in decorators_widths]

    t = Tchart(*canvas_size, renderer=renderer, decorators=decorators)
    t.render(values=[])

    render_call = renderer.render_calls[0]
    assert (render_call['width'], render_call['height']) == expected_render_size


def test_render_calls_decorator_chain():
    results_chain = [
        ('renderer-output', ),
        ('decorator1', ),
        ('decorator2', ),
        ('decorator3', ),
    ]

    renderer = FakeRenderer(render_results=results_chain[0])
    decorators = [FakeDecorator(decorator_results=result) for result in results_chain[1:]]

    t = Tchart(10, 10, renderer=renderer, decorators=decorators)
    t.render(values=[])

    for decorator, result in zip(decorators, results_chain):
        assert len(decorator.decorate_calls) == 1

        decorator_call = decorator.decorate_calls[0]
        assert set(decorator_call.keys()) == {'lines'}
        assert decorator_call['lines'] == result
