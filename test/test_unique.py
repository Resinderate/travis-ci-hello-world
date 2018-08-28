import unittest

from src.unique import is_unique


class TestUnique(unittest.TestCase):

    def test_sparse(self):
        assert is_unique("dermatoglyphics")

    def test_dupes(self):
        assert not is_unique("ronan")

    def test_case_sensitive(self):
        assert is_unique("Unique")

    def test_invalid_test(self):
        assert is_unique("aaabbb")
