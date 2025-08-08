# board io import
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main keyboard object
KeyDeck = KMKKeyboard()

# macro extention initialization
macros = Macros()
KeyDeck.modules.append(macros)

# Pin definitions
PINS = [board.D7, board.D8, board.D10, board.D9, board.D3, board.D2, board.D1, board.D0]

# Tell kmk we are not using a key matrix
KeyDeck.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
KeyDeck.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8]
]

# Start kmk!
if __name__ == '__main__':
    KeyDeck.go()