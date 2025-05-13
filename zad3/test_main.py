import unittest
from main import generate_non_decreasing_sequences

class TestNonDecreasingSequences(unittest.TestCase):
    def test_zero_or_negative(self):
        self.assertEqual(generate_non_decreasing_sequences(0), [])
        self.assertEqual(generate_non_decreasing_sequences(-1), [])
    
    def test_one(self):
        self.assertEqual(generate_non_decreasing_sequences(1), [[1]])
    
    def test_two(self):
        expected = [[1, 1], [2]]
        self.assertEqual(generate_non_decreasing_sequences(2), expected)
    
    def test_three(self):
        expected = [[1, 1, 1], [1, 2], [3]]
        self.assertEqual(generate_non_decreasing_sequences(3), expected)
    
    def test_four(self):
        expected = [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]]
        self.assertEqual(generate_non_decreasing_sequences(4), expected)
    
    def test_five(self):
        expected = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 4], [2, 3], [5]]
        self.assertEqual(generate_non_decreasing_sequences(5), expected)
    
    def test_sequence_properties(self):
        n = 6
        sequences = generate_non_decreasing_sequences(n)
        
        for seq in sequences:
            self.assertEqual(sum(seq), n)
            for i in range(len(seq) - 1):
                self.assertLessEqual(seq[i], seq[i + 1])
            for num in seq:
                self.assertGreater(num, 0)

if __name__ == '__main__':
    unittest.main()
