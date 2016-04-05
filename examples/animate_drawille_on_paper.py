import cursor
import os
import time
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tchart


t = tchart.Tchart(height=18, width=120,
                  renderer=tchart.renderers.DrawilleRenderer(),
                  decorators=[
                      tchart.decorators.PaperDecorator(),
                  ])


def print_n_reset(text):
    console_line_up = '\x1b[A'
    text += '\n'
    line_count = text.count('\n')
    text += console_line_up * line_count
    sys.stdout.write(text)
    sys.stdout.flush()


def main_loop():
    data = []

    while True:
        data.insert(0, random.randint(-100, 100))
        data = data[:100]
        lines = t.render(data)
        print_n_reset(u'\n'.join(lines))
        time.sleep(1)


def main():
    print('Press CTRL+C to abort animation')

    cursor.hide()
    try:
        main_loop()
    except KeyboardInterrupt:
        cursor.show()
        os.system('clear')


if __name__ == '__main__':
    main()
