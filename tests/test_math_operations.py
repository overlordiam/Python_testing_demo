import unittest
from app.math_operations import MathHelper


class TestMathOperations(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = MathHelper()
        print("started")

    def tearDown(self) -> None:
        del self.obj
        print("finished")

    def test_add(self):
        self.assertEqual(self.obj.add(1, 2), 3)
        self.assertEqual(self.obj.add(-2, 3), 1)
        self.assertEqual(self.obj.add(0, 0), 0)
        self.assertEqual(self.obj.add(1.5, 2.5), 4.0)
        self.assertEqual(self.obj.add(-2, -3), -5)

    def test_divide(self):
        with self.assertRaises(ValueError):
            self.obj.divide(1, 0)

        self.assertEqual(self.obj.divide(4, 2), 2.0)
        self.assertEqual(self.obj.divide(5, 2), 2.5)

    def test_is_even(self):
        self.assertTrue(self.obj.is_even(4))
        self.assertFalse(self.obj.is_even(3))
        self.assertTrue(self.obj.is_even(0))
        self.assertTrue(self.obj.is_even(-4))

    def test_get_max(self):
        self.assertIsNone(self.obj.get_max([]))
        self.assertEqual(self.obj.get_max([1, 2, 3]), 3)


if __name__ == "__main__":
    unittest.main()
