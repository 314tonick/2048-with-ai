def invert_color(color: tuple):
    return [255 - i for i in color]


def set_value(prp, value):
    r = open('settings.txt').readlines()
    w = open('settings.txt', 'w')
    r[['THEME', 'BEST'].index(prp)] = repr(value) + '\n'

    w.write(''.join(r))
    w.close()


def get_values():
    global BEST
    global THEME
    THEME, BEST = [eval(value) for value in open('settings.txt').readlines()]


COLORS = {
    'DARK': {
        'bg': (0, 0, 0),
        'count_fg': (0, 255, 0),
        'best_fg': (255, 0, 0)
    },
}


COORD = {
    'count': (30, 25),
    'best': (30, 105),
    'restart': (405, 25),
    'settings': (405, 105),
    'field': (50, 50),
    'field_surface': (0, 175)
}
BEST = ...
THEME = ...
get_values()