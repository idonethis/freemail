import unittest
from freemail import Freemail


class TestFreemail(unittest.TestCase):

    def test_disposable(self):
        self.assertIn("mailinator.com", Freemail.disposable)
        self.assertNotIn("flevour.net", Freemail.disposable)

    def test_free(self):
        self.assertIn("gmail.com", Freemail.free)
        self.assertNotIn("flevour.net", Freemail.free)

    def test_class(self):
        self.assertIn("mailinator.com", Freemail)
        self.assertIn("gmail.com", Freemail)
        self.assertNotIn("flevour.net", Freemail)


if __name__ == '__main__':
    unittest.main()
