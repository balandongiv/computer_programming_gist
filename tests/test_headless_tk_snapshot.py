import unittest
from pathlib import Path

import tkinter as tk
from PIL import ImageGrab

from helper.virtual_display import virtual_display


class HeadlessTkSnapshotTest(unittest.TestCase):
    def test_snapshot_saved(self) -> None:
        artifacts_dir = Path(__file__).parent / "artifacts"
        artifacts_dir.mkdir(parents=True, exist_ok=True)
        snapshot_path = artifacts_dir / "robot_snapshot.png"
        if snapshot_path.exists():
            snapshot_path.unlink()

        with virtual_display(size=(800, 600)):
            root = tk.Tk()
            root.title("Hello Codespaces GUI!")
            root.geometry("300x150+0+0")

            label = tk.Label(root, text="Hello Codespaces GUI!", font=("Arial", 16))
            label.pack(expand=True)

            root.update_idletasks()
            root.update()

            bbox = (
                root.winfo_rootx(),
                root.winfo_rooty(),
                root.winfo_rootx() + root.winfo_width(),
                root.winfo_rooty() + root.winfo_height(),
            )

            image = ImageGrab.grab(bbox=bbox)
            image.save(snapshot_path)

            root.destroy()

        self.assertTrue(snapshot_path.exists(), "Snapshot PNG was not created")
        self.assertGreater(snapshot_path.stat().st_size, 0, "Snapshot PNG is empty")


if __name__ == "__main__":
    unittest.main()
