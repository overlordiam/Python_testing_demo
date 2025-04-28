import unittest
from app.top_k_elements import TopKElements


class TestTopKElements(unittest.TestCase):
    def test_top_k_frequent_elements(self):
        nums = [1, 1, 1, 2, 2, 3]
        self.assertEqual(TopKElements().topKFrequent(nums, 2), [1, 2])


if __name__ == "__main__":
    unittest.main()
