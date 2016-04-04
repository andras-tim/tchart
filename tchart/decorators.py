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
