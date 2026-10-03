import os
import tempfile
import unittest
from email_extractor import extract_emails, extract_from_file


class TestEmailExtractor(unittest.TestCase):
    def test_basic(self):
        text = "Mail a@b.com and c.d@e.org."
        self.assertEqual(extract_emails(text), ["a@b.com", "c.d@e.org"])

    def test_duplicates_removed(self):
        self.assertEqual(extract_emails("x@y.com x@y.com"), ["x@y.com"])

    def test_invalid_ignored(self):
        self.assertEqual(extract_emails("not-an-email@, another@@bad, @nope.com"), [])

    def test_subdomain(self):
        self.assertEqual(extract_emails("john.doe99@mail.co.in"), ["john.doe99@mail.co.in"])

    def test_file_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "in.txt")
            out = os.path.join(tmp, "out.txt")
            with open(src, "w") as f:
                f.write("hi me@site.com bye me@site.com")
            self.assertEqual(extract_from_file(src, out), ["me@site.com"])
            with open(out) as f:
                self.assertEqual(f.read().strip(), "me@site.com")


if __name__ == "__main__":
    unittest.main()
