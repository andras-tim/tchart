# -*- coding: UTF-8 -*-

from __future__ import division
import numpy


class ChartRenderer(object):
    BORDER = {
        'vertical': u'│',
        'horizontal': u'─',
        'crossing': u'┼'
    }
    BLOCK_VARIANTS = (
        u' ',
        u'▁',
        u'▂',
        u'▃',
        u'▄',
        u'▅',
        u'▆',
        u'▇',
        u'█',
    )

    def __init__(self, height=5, width=10):
        """
        :type height: int
        :type width: int
        """
        self._vertical_offset = len(self.BORDER['vertical'])
        self._horizontal_offset = len(self.BORDER['horizontal'])

        if height <= self._vertical_offset or width <= self._horizontal_offset:
            raise ValueError('Bad dimension; min 2x2')

        self._chart_height = height
        self._chart_width = width

        self._height = height - self._vertical_offset
        self._width = width - self._horizontal_offset

        self._block_resolution = len(self.BLOCK_VARIANTS) - 1
        self._vertical_resolution = self._height * self._block_resolution
        self._horizontal_resolution = self._width

    def render(self, values):
        """
        :type values: list
        :rtype: tuple[str or unicode]
        """
        output_buffer = self._get_empty_buffer()
        if values:
            self._render_bars(values, output_buffer)
        return self._convert_buffer_to_tuple_of_lines(output_buffer)

    def _get_empty_buffer(self):
        """
        :rtype: list[str or unicode]
        """
        buffer = []

        for i in range(self._height):
            buffer += [[self.BORDER['vertical']] + [self.BLOCK_VARIANTS[0]] * self._width]
        buffer += [[self.BORDER['crossing']] + [self.BORDER['horizontal']] * self._width]

        return buffer

    def _render_bars(self, values, output_buffer):
        """
        :type values: list
        :type output_buffer: list[str or unicode]
        """
        normalized_values = self._normalize_values(values)

        x = 0
        for value in normalized_values:
            y = 0
            while value > self._block_resolution:
                self._block_writer(x, y, self._block_resolution, output_buffer)
                value -= self._block_resolution
                y += 1
            if value > 0:
                self._block_writer(x, y, int(round(value, 0)), output_buffer)
            x += 1

    def _block_writer(self, x, y, block_variant, output_buffer):
        """
        :type x: int
        :type y: int
        :type block_variant: int
        :type output_buffer: list[str or unicode]
        """
        output_buffer[self._height - 1 - y][x + self._horizontal_offset] = self.BLOCK_VARIANTS[block_variant]

    def _normalize_values(self, values):
        """
        :type values: list
        :rtype: list
        """
        minimum = min(values)
        value_range = max(values) - minimum

        vertical_scale = 1
        if value_range:
            vertical_scale = self._vertical_resolution / value_range

        values = DataManipulation.shift_values(values, -minimum)
        values = DataManipulation.horizontal_scale_values(values, self._horizontal_resolution)
        values = DataManipulation.vertical_scale_values(values, vertical_scale)

        return values

    def _convert_buffer_to_tuple_of_lines(self, output_buffer):
        """
        :type output_buffer: list[str or unicode]
        :rtype: tuple
        """
        return tuple(u''.join(row) for row in output_buffer)


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
