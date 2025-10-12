"""Utility helpers for running tkinter code in headless environments."""

from __future__ import annotations

import os
import threading
from contextlib import contextmanager
from typing import Iterator, Optional, Tuple

from pyvirtualdisplay import Display

_DisplaySize = Tuple[int, int]

_display_lock = threading.Lock()
_display_instance: Optional[Display] = None
_active_users: int = 0


def ensure_virtual_display(size: _DisplaySize = (1024, 768), **kwargs) -> Optional[Display]:
    """Ensure a virtual display is available for Tkinter."""
    global _display_instance, _active_users

    if os.environ.get("DISPLAY"):
        return None

    with _display_lock:
        if _display_instance is None:
            _display_instance = Display(visible=0, size=size, **kwargs)
            _display_instance.start()
        _active_users += 1
        return _display_instance


def stop_virtual_display() -> None:
    """Decrease the reference count and stop the virtual display when unused."""
    global _display_instance, _active_users

    if os.environ.get("DISPLAY"):
        return

    with _display_lock:
        if _display_instance is None:
            return

        _active_users = max(0, _active_users - 1)
        if _active_users == 0:
            _display_instance.stop()
            _display_instance = None


@contextmanager
def virtual_display(size: _DisplaySize = (1024, 768), **kwargs) -> Iterator[Optional[Display]]:
    """Context manager that automatically manages a virtual display lifecycle."""
    display = ensure_virtual_display(size=size, **kwargs)
    try:
        yield display
    finally:
        if display is not None:
            stop_virtual_display()
