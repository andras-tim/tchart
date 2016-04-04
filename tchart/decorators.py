class ChartDecorator(object):
    @property
    def width_left(self):
        """
        Required chart margin at left for decorate

        :rtype: int
        """
        return 0

    @property
    def width_top(self):
        """
        Required chart margin at top for decorate

        :rtype: int
        """
        return 0

    @property
    def width_right(self):
        """
        Required chart margin at right for decorate

        :rtype: int
        """
        return 0

    @property
    def width_bottom(self):
        """
        Required chart margin at bottom for decorate

        :rtype: int
        """
        return 0

    def decorate(self, lines):
        """
        Decorate the rendered data

        :param lines: Lines of rendered data
        :type lines: list[str or unicode]
        :return: Decorated lines
        :rtype: list[str or unicode]
        """
        raise NotImplementedError


class AxisDecorator(ChartDecorator):
    BORDER_VERTICAL = u'\U00002502'
    BORDER_HORIZONTAL = u'\U00002500'
    BORDER_CROSSING = u'\U0000253c'

    @property
    def width_left(self):
        return 1

    @property
    def width_bottom(self):
        return 1

    def decorate(self, lines):
        width = len(lines[0])

        decorated_lines = [
            u'{border}{data}'.format(
                border=AxisDecorator.BORDER_VERTICAL,
                data=line)
            for line in lines
        ]

        decorated_lines.append(
            u'{origin}{border}'.format(
                origin=AxisDecorator.BORDER_CROSSING,
                border=AxisDecorator.BORDER_HORIZONTAL * width)
        )

        return decorated_lines


class FrameDecorator(ChartDecorator):
    BORDER_VERTICAL = u'\U00002503'
    BORDER_HORIZONTAL = u'\U00002501'
    BORDER_CORNERS = (u'\U0000250f', u'\U00002513', u'\U00002517', u'\U0000251b')

    @property
    def width_left(self):
        return 1

    @property
    def width_top(self):
        return 1

    @property
    def width_right(self):
        return 1

    @property
    def width_bottom(self):
        return 1

    def decorate(self, lines):
        width = len(lines[0])

        decorated_lines = [
            u'{border}{data}{border}'.format(
                border=self.BORDER_VERTICAL,
                data=line)
            for line in lines
        ]

        decorated_lines.insert(
            0,
            u'{top_left}{border}{top_right}'.format(
                top_left=self.BORDER_CORNERS[0],
                top_right=self.BORDER_CORNERS[1],
                border=self.BORDER_HORIZONTAL * width
            )
        )

        decorated_lines.append(
            u'{bottom_left}{border}{bottom_right}'.format(
                bottom_left=self.BORDER_CORNERS[2],
                bottom_right=self.BORDER_CORNERS[3],
                border=self.BORDER_HORIZONTAL * width
            )
        )

        return decorated_lines


class DoubleFrameDecorator(FrameDecorator):
    BORDER_VERTICAL = u'\U00002551'
    BORDER_HORIZONTAL = u'\U00002550'
    BORDER_CORNERS = (u'\U00002554', u'\U00002557', u'\U0000255a', u'\U0000255d')


class ThinFrameDecorator(FrameDecorator):
    BORDER_VERTICAL = u'\U00002502'
    BORDER_HORIZONTAL = u'\U00002500'
    BORDER_CORNERS = (u'\U0000250c', u'\U00002510', u'\U00002514', u'\U00002518')


class PaperDecorator(ChartDecorator):
    TOP_LEFT = (
        u'          ',
        u'          ',
        u'          ',
        u'          ',
        u'  .-------',
        u' /  .-.   ',
        u'|  /   \\  ',
        u'| |\\_.  | ',
        u'|\\|  | /| ',
        u'| `---\' | ',
    )

    LEFT = u'|       | '

    BOTTOM_LEFT = (
        u'|       |-',
        u'\\       | ',
        u' \\     /  ',
        u'  `---\'   ',
    )

    TOP_BOTTOM = u'-'

    TOP_RIGHT = (
        u'  .---.  ',
        u' /  .  \\ ',
        u'|\\_/|   |',
        u'|   |  /|',
        u'------\' |',
    )

    RIGHT = u'  |'

    BOTTOM_RIGHT = (
        u'  |',
        u' / ',
        u'\'  ',
    )

    START_X = 10
    START_Y = 5
    RIGHT_SHIFT = 6

    @property
    def width_left(self):
        return 10

    @property
    def width_top(self):
        return 5

    @property
    def width_right(self):
        return 4

    @property
    def width_bottom(self):
        return 4

    def decorate(self, lines):
        lines_width = max([len(line) for line in lines])

        lines = [u'{0}{1}{2}'.format(self.LEFT, line.ljust(lines_width), self.RIGHT) for line in lines]
        border = u'{0}{1}{2}'.format(self.LEFT[:-1], self.TOP_BOTTOM * (lines_width + 2), self.RIGHT[1:])
        lines.insert(0, border)
        lines.append(border)

        decorated_lines = []
        self._merge(decorated_lines, 0, self.START_Y - 1, lines)
        self._merge(decorated_lines, 0, 0, self.TOP_LEFT)
        self._merge(decorated_lines, self.START_X + lines_width - self.RIGHT_SHIFT, 0, self.TOP_RIGHT)
        self._merge(decorated_lines, 0, self.START_Y + len(lines) - 2, self.BOTTOM_LEFT)
        self._merge(decorated_lines, self.START_X + lines_width, self.START_Y + len(lines) - 4, self.BOTTOM_RIGHT)

        return decorated_lines

    @classmethod
    def _merge(cls, lines, x, y, updater_lines):
        """
        :type lines: list[str or unicode] or tuple[str or unicode]
        :type x: int
        :type y: int
        :type updater_lines: list[str or unicode] or tuple[str or unicode]
        """
        update_height = len(updater_lines)
        update_width = max([len(line) for line in updater_lines])

        while len(lines) < y + update_height:
            lines.append('')

        for i, line in enumerate(lines):
            lines[i] = line.ljust(x + update_width, ' ')

        for i, update_line in zip(range(y, y + update_height), updater_lines):
            lines[i] = lines[i][:x] + update_line + lines[i][x + len(update_line):]
