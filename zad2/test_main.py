import unittest
from main import find_longest_max_sum_subsequence

class TestLongestMaxSumSubsequence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_longest_max_sum_subsequence([]), [])
    
    def test_single_element(self):
        self.assertEqual(find_longest_max_sum_subsequence([5]), [5])
        self.assertEqual(find_longest_max_sum_subsequence([-5]), [-5])
    
    def test_example_from_task(self):
        numbers = [2, -4, 6, 8, -10, 100, -6, 5]
        expected = [6, 8, -10, 100]
        self.assertEqual(find_longest_max_sum_subsequence(numbers), expected)
    
    def test_all_positive(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(find_longest_max_sum_subsequence(numbers), numbers)
    
    def test_all_negative(self):
        numbers = [-5, -4, -3, -2, -1]
        self.assertEqual(find_longest_max_sum_subsequence(numbers), [-1])
    
    def test_multiple_equal_sums(self):
        numbers = [1, 2, 3, -6, 1, 2, 3]
        self.assertEqual(find_longest_max_sum_subsequence(numbers), [1, 2, 3])
    
    def test_alternating_positive_negative(self):
        numbers = [1, -1, 1, -1, 1]
        self.assertEqual(find_longest_max_sum_subsequence(numbers), [1, -1, 1, -1, 1])
    
    def test_sequence_with_zeros(self):
        numbers = [0, 1, 2, 0, 3, 4, 0]
        self.assertEqual(find_longest_max_sum_subsequence(numbers), [0, 1, 2, 0, 3, 4, 0])

if __name__ == '__main__':
    unittest.main()
