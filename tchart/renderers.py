# -*- coding: UTF-8 -*-


class ChartRenderer(object):
    @property
    def char_resolution_horizontal(self):
        """
        Horizontal data-resolution of one character

        :rtype: int
        """
        return 1

    @property
    def char_resolution_vertical(self):
        """
        Horizontal data-resolution of one character

        :rtype: int
        """
        return 1

    def render(self, width, height, values):
        """
        Render values to chart

        :type width: int
        :type height: int
        :param values: Scaled values for chart capacity
        :type values: list[int or float]
        :return: Rendered lines
        :rtype: list[str or unicode]
        """
        raise NotImplementedError


class BoxRenderer(ChartRenderer):
    BLOCKS = (
        u' ',  # 0
        u'▁',  # 1
        u'▂',  # 2
        u'▃',  # 3
        u'▄',  # 4
        u'▅',  # 5
        u'▆',  # 6
        u'▇',  # 7
        u'█',  # 8
    )

    @property
    def char_resolution_vertical(self):
        """
        :rtype: int
        """
        return len(self.BLOCKS) - 1

    def render(self, width, height, values):
        """
        :type width: int
        :type height: int
        :type values: list[int or float]
        :rtype: list[str or unicode]
        """

        output_buffer = [[self.BLOCKS[0]] * width for _ in range(height)]

        x = 0
        resolution = self.char_resolution_vertical
        for value in values:
            y = 0
            while value > resolution:
                self._block_writer(x, y, resolution, output_buffer)
                value -= resolution
                y += 1
            if value > 0:
                self._block_writer(x, y, int(round(value, 0)), output_buffer)
            x += 1

        return [u''.join(line) for line in reversed(output_buffer)]

    def _block_writer(self, x, y, block_variant, output_buffer):
        """
        :type x: int
        :type y: int
        :type block_variant: int
        :type output_buffer: list[list[str or unicode]]
        """
        output_buffer[y][x] = self.BLOCKS[block_variant]


class SharpRenderer(BoxRenderer):
    BLOCKS = (
        u' ',  # 0
        u'.',  # 1
        u'x',  # 2
        u'#',  # 3
    )


class DrawilleRenderer(ChartRenderer):
    @property
    def char_resolution_horizontal(self):
        return 2

    @property
    def char_resolution_vertical(self):
        return 4

    def render(self, width, height, values):
        """
        :type width: int
        :type height: int
        :type values: list[int or float]
        :rtype: list[str or unicode]
        """
        from drawille import Canvas

        vertical_chart_resolution = height * self.char_resolution_vertical
        horizontal_chart_resolution = width * self.char_resolution_horizontal

        canvas = Canvas()
        x = 0
        for value in values:
            for y in range(1, int(round(value, 0)) + 1):
                canvas.set(x, vertical_chart_resolution - y)
            x += 1

        rows = canvas.rows(min_x=0, min_y=0, max_x=horizontal_chart_resolution, max_y=vertical_chart_resolution)

        if not rows:
            rows = [u'' for _ in range(height)]

        for i, row in enumerate(rows):
            rows[i] = u'{0}'.format(row.ljust(width))

        return rows
