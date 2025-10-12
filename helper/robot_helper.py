import tkinter as tk

from helper.virtual_display import ensure_virtual_display, stop_virtual_display


class SimulationWindow:
    """Container for the Tkinter root window used in simulations."""

    def __init__(self):
        self._display = ensure_virtual_display()
        self.root = tk.Tk()
        self.should_stop = False

    def close(self) -> None:
        """Destroy the Tk window and release the virtual display if needed."""
        if self.root.winfo_exists():
            self.root.destroy()
        if self._display is not None:
            stop_virtual_display()

    def __del__(self) -> None:  # pragma: no cover - best effort cleanup
        try:
            self.close()
        except Exception:
            pass


def initialize_canvas(window):
    window.resizable(False, False)
    canvas = tk.Canvas(window, width=1000, height=1000)
    canvas.pack()
    return canvas

def bot_clicked(x, y, registryActives, Bot):
    '''
    Bot is a class
    :param x:
    :param y:
    :param registryActives:
    :param Bot:
    :return:
    rpb purposely use the pass statement here. to be use in tutorial 8. see the pre-requisite section about the full code
    '''
    pass
