import unittest
from unittest.mock import patch

from foo_bar import bar, foo


class TestFooBar(unittest.TestCase):
    def test_bar(self):
        result = bar()
        self.assertEqual(result, "bar")

    @patch("foo_bar.bar")
    def test_foo(self, mock_bar):
        mock_bar.return_value = "mocked"
        result = foo()
        self.assertEqual(result, "Foo, mocked")
