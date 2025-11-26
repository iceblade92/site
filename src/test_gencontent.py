import unittest

from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_h1(self):
        markdown = "test\n# Hello\nWorld"
        title = extract_title(markdown)
        self.assertEqual(title, "Hello")

    def test_no_h1_raises(self):
        markdown = "test\n## Hello\nWorld"
        with self.assertRaises(Exception):
            extract_title(markdown)