# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: PetCare
import sys

try:
    sys.stdout = _orig_stdout
    sys.stderr = _orig_stderr
except NameError:
    _orig_stdout = sys.stdout
    _orig_stderr = sys.stderr

ANSI = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bright_red': '\033[91m',
    'bright_green': '\033[92m',
    'bright_yellow': '\033[93m',
    'bright_blue': '\033[94m',
}

color_enabled = True

def colorize(text, color):
    if not color_enabled:
        return text
    return ANSI.get(color, '') + str(text) + ANSI['reset']

def success(msg):
    return colorize(msg, 'bright_green')

def warning(msg):
    return colorize(msg, 'bright_yellow')

def error(msg):
    return colorize(msg, 'bright_red')

def info(msg):
    return colorize(msg, 'blue')

def dimmed(msg):
    return colorize(msg, 'dim')

def header(text):
    return colorize(text, 'bright_white') + ANSI['bold']

def status_ok():
    return colorize('[OK]', 'bright_green')

def status_warn():
    return colorize('[!]', 'bright_yellow')

def status_err():
    return colorize('[X]', 'bright_red')
