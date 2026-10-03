import os
import tempfile
import unittest
from jpg_mover import move_jpgs


class TestJpgMover(unittest.TestCase):
    def test_moves_only_jpgs(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ["a.jpg", "b.JPG", "c.jpeg", "d.png", "e.txt"]:
                open(os.path.join(tmp, name), "w").close()
            dest = os.path.join(tmp, "images")
            moved = move_jpgs(tmp, dest)
            self.assertEqual(moved, ["a.jpg", "b.JPG", "c.jpeg"])
            self.assertTrue(os.path.exists(os.path.join(tmp, "d.png")))
            self.assertEqual(len(os.listdir(dest)), 3)

    def test_name_clash_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = os.path.join(tmp, "images")
            os.makedirs(dest)
            open(os.path.join(dest, "a.jpg"), "w").close()
            open(os.path.join(tmp, "a.jpg"), "w").close()
            move_jpgs(tmp, dest)
            self.assertEqual(sorted(os.listdir(dest)), ["a.jpg", "a_1.jpg"])

    def test_missing_source(self):
        with self.assertRaises(FileNotFoundError):
            move_jpgs("/definitely/not/here", "/tmp/x")


if __name__ == "__main__":
    unittest.main()
