import unittest
from main import find_longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_longest_increasing_subsequence([]), [])
    
    def test_single_element(self):
        self.assertEqual(find_longest_increasing_subsequence([5]), [5])
    
    def test_example_from_task(self):
        numbers = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        expected = [10, 22, 33, 50, 60, 80]
        self.assertEqual(find_longest_increasing_subsequence(numbers), expected)
    
    def test_all_increasing(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(find_longest_increasing_subsequence(numbers), numbers)
    
    def test_all_decreasing(self):
        numbers = [5, 4, 3, 2, 1]
        self.assertEqual(find_longest_increasing_subsequence(numbers), [1])
    
    def test_duplicate_numbers(self):
        numbers = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(find_longest_increasing_subsequence(numbers), [1, 2, 3, 4, 5])
    
    def test_multiple_possible_subsequences(self):
        numbers = [1, 3, 2, 4, 3, 5]
        result = find_longest_increasing_subsequence(numbers)
        self.assertEqual(len(result), 5)
        for i in range(len(result) - 1):
            self.assertLess(result[i], result[i + 1])

if __name__ == '__main__':
    unittest.main()
