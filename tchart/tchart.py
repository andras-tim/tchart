# -*- coding: UTF-8 -*-

from __future__ import division
import numpy

from .renderers import BoxRenderer
from .decorators import AxisDecorator

DEFAULT_RENDERER = BoxRenderer()
DEFAULT_DECORATORS = (AxisDecorator(), )


class Tchart(object):
    def __init__(self, width=10, height=5, renderer=DEFAULT_RENDERER, decorators=DEFAULT_DECORATORS):
        """
        :param width: Canvas width
        :type width: int
        :param height: Canvas height
        :type height: int
        :type renderer: tchart.renderers.ChartRenderer
        :type decorators: tuple[tchart.decorators.ChartDecorator] or list[tchart.decorators.ChartDecorator] or None
        """
        self._canvas_width = width
        self._canvas_height = height
        self._chart_renderer = renderer
        self._decorators = decorators or ()

        margin_left = margin_top = margin_right = margin_bottom = 0
        if decorators:
            margin_left = sum([decorator.width_left for decorator in decorators])
            margin_top = sum([decorator.width_top for decorator in decorators])
            margin_right = sum([decorator.width_right for decorator in decorators])
            margin_bottom = sum([decorator.width_bottom for decorator in decorators])

        margin_horizontal = margin_left + margin_right
        margin_vertical = margin_top + margin_bottom

        self._chart_width = self._canvas_width - margin_horizontal
        self._chart_height = self._canvas_height - margin_vertical
        self._chart_resolution_horizontal = self._chart_width * self._chart_renderer.char_resolution_horizontal
        self._chart_resolution_vertical = self._chart_height * self._chart_renderer.char_resolution_vertical

        if self._chart_width < 1 or self._chart_height < 1:
            raise ValueError('Bad dimension; min {min_width}x{min_height}'.format(
                min_width=margin_horizontal + 1,
                min_height=margin_vertical + 1,
            ))

    def render(self, values):
        """
        :type values: list
        :rtype: tuple[str or unicode]
        """
        normalized_values = self._normalize_values(values)

        lines = self._chart_renderer.render(width=self._chart_width, height=self._chart_height,
                                            values=normalized_values)

        for decorator in self._decorators:
            lines = decorator.decorate(lines=lines)

        return lines

    @property
    def canvas_width(self):
        """
        :rtype: int
        """
        return self._canvas_width

    @property
    def canvas_height(self):
        """
        :rtype: int
        """
        return self._canvas_height

    @property
    def chart_width(self):
        """
        :rtype: int
        """
        return self._chart_width

    @property
    def chart_height(self):
        """
        :rtype: int
        """
        return self._chart_height

    def _normalize_values(self, values):
        """
        :type values: list
        :rtype: list
        """
        if not values:
            return []

        minimum = min(values)
        value_range = max(values) - minimum

        vertical_scale = 1
        if value_range > 1:
            vertical_scale = self._chart_resolution_vertical / value_range

        values = DataManipulation.shift_values(values, -minimum)
        values = DataManipulation.horizontal_scale_values(values, self._chart_resolution_horizontal)
        values = DataManipulation.vertical_scale_values(values, vertical_scale)

        return values


class DataManipulation(object):
    @classmethod
    def shift_values(cls, values, shift):
        """
        :type values: list
        :type shift: float
        :rtype: list
        """
        return [value + shift for value in values]

    @classmethod
    def horizontal_scale_values(cls, values, new_width):
        """
        :type values: list
        :type new_width: int
        :rtype: list
        """
        if new_width == 0:
            return []
        if new_width == 1:
            return [numpy.mean(values)]

        return cls._horizontal_scale_values_with_interpolation(values, new_width)

    @classmethod
    def _horizontal_scale_values_with_interpolation(cls, values, new_width):
        """
        :type values: list
        :type new_width: int
        :rtype: list
        """
        old_point_count = len(values)
        if old_point_count == new_width:
            return values

        new_x_partition_count = new_width - 1
        new_x_step_size = (old_point_count - 1) / new_x_partition_count

        new_x_points = [0] * new_width
        if new_x_step_size > 0:
            new_x_points = list(numpy.arange(0, old_point_count - 1, new_x_step_size))
            if len(new_x_points) < new_width:
                new_x_points += [old_point_count - 1]

        new_y_points = numpy.interp(new_x_points, xp=range(old_point_count), fp=values)

        return list(new_y_points)

    @classmethod
    def vertical_scale_values(cls, values, scale):
        """
        :type values: list
        :type scale: float
        :rtype: list
        """
        return [value * scale for value in values]
