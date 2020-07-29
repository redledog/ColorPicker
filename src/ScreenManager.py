

class ScreenManager:

    def __init__(self):
        self.init_screen()

    def init_screen(self, widget, size, move):
        widget.size(size[0], size[1]);
        widget.move(move);