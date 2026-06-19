# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def color_print(text: str, effect: str) -> None:
    print("{0}{1}{2}".format(effect,text,RESET))


color_print("Hello Blue",BLUE)
color_print("Hello Red",RED)
color_print("Hello Green",GREEN)
color_print("Hello Yellow",YELLOW)
color_print("Hello Magenta",MAGENTA)
color_print("Hello White",WHITE)
print("This is the test text")
