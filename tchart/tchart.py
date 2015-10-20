# -*- coding: UTF-8 -*-
import numpy


class ChartRenderer:
    BORDER = {
        'vertical': '│',
        'horizontal': '─',
        'crossing': '┼'
    }
    BLOCK_VARIANTS = (
        ' ',
        '▁',
        '▂',
        '▃',
        '▄',
        '▅',
        '▆',
        '▇',
        '█',
    )

    def __init__(self, height: int=5, width: int=10):
        self._vertical_offset = len(self.BORDER['vertical'])
        self._horizontal_offset = len(self.BORDER['horizontal'])

        if height <= self._vertical_offset or width <= self._horizontal_offset:
            raise Exception('Bad dimension; min 2x2')

        self._chart_height = height
        self._chart_width = width

        self._height = height - self._vertical_offset
        self._width = width - self._horizontal_offset

        self._block_resolution = len(self.BLOCK_VARIANTS) - 1
        self._vertical_resolution = self._height * self._block_resolution
        self._horizontal_resolution = self._width

    def render(self, values: list) -> tuple:
        output_buffer = self._get_empty_buffer()
        if values:
            self._render_bars(values, output_buffer)
        return self._convert_buffer_to_tuple_of_lines(output_buffer)

    def _get_empty_buffer(self) -> list:
        buffer = []

        for i in range(self._height):
            buffer += [[self.BORDER['vertical']] + [self.BLOCK_VARIANTS[0]] * self._width]
        buffer += [[self.BORDER['crossing']] + [self.BORDER['horizontal']] * self._width]

        return buffer

    def _render_bars(self, values: list, output_buffer: list):
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

    def _block_writer(self, x: int, y: int, block_variant: int, output_buffer: list):
        output_buffer[self._height - 1 - y][x + self._horizontal_offset] = self.BLOCK_VARIANTS[block_variant]

    def _normalize_values(self, values: list) -> list:
        minimum = min(values)
        value_range = max(values) - minimum

        vertical_scale = 1
        if value_range:
            vertical_scale = self._vertical_resolution / value_range

        values = DataManipulation.shift_values(values, -minimum)
        values = DataManipulation.horizontal_scale_values(values, self._horizontal_resolution)
        values = DataManipulation.vertical_scale_values(values, vertical_scale)

        return values

    def _convert_buffer_to_tuple_of_lines(self, output_buffer: list) -> tuple:
        return tuple(''.join(row) for row in output_buffer)


class DataManipulation:
    @classmethod
    def shift_values(cls, values: list, shift: float) -> list:
        return [value + shift for value in values]

    @classmethod
    def horizontal_scale_values(cls, values: list, new_width: int) -> list:
        if len(values) >= new_width:
            return cls._horizontal_down_scale_values(values, new_width)
        return cls._horizontal_up_scale_values(values, new_width)

    @classmethod
    def _horizontal_down_scale_values(cls, values: list, new_width: int) -> list:
        if new_width == 0:
            return []

        result = []
        scale = new_width / len(values)

        source_x = 0
        while source_x < len(values):
            scale_sum = 0.0
            value_sum = 0
            value_count = 0

            while scale_sum < 1.0 and source_x < len(values):
                value_sum += values[source_x]
                value_count += 1
                source_x += 1
                scale_sum += scale

            result.append(value_sum / value_count)

        return result

    @classmethod
    def _horizontal_up_scale_values(cls, values: list, new_width: int) -> list:
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
    def vertical_scale_values(cls, values: list, scale: float) -> list:
        return [value * scale for value in values]
