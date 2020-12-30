from colorama import init, Fore, Back
import random

init()

class Colors:
    """

    """
    RESET = Fore.RESET
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    BLUE = Fore.BLUE
    WHITE = Fore.WHITE

    def getFore():
        COLORS = (
            Colors.RED, Colors.GREEN, Colors.YELLOW,
            Colors.CYAN, Colors.MAGENTA, Colors.BLUE, Colors.WHITE
        )
        return COLORS[random.randint(0, 6)]

    def getBack():
        COLORS_BG = (
            Back.RED, Back.GREEN, Back.YELLOW,
            Back.BLUE, Back.CYAN, Back.MAGENTA,
            Back.BLACK, Back.WHITE
        )
        return COLORS_BG[random.randint(0, 7)]
