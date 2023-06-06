import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, PACK


class Heading:
    style = Pack(direction=ROW, text_align=CENTER, padding=5, font_size=32)
