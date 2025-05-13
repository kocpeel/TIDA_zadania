import unittest
from main import generate_permutations

class TestPermutations(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(generate_permutations(0), [])
        self.assertEqual(generate_permutations(-1), [])
        self.assertEqual(generate_permutations(27), [])
    
    def test_one_letter(self):
        self.assertEqual(generate_permutations(1), ['a'])
    
    def test_two_letters(self):
        expected = ['ab', 'ba']
        self.assertEqual(generate_permutations(2), expected)
    
    def test_three_letters(self):
        expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        self.assertEqual(generate_permutations(3), expected)
    
    def test_four_letters(self):
        result = generate_permutations(4)
        self.assertEqual(len(result), 24)
        self.assertEqual(result[0], 'abcd')
        self.assertEqual(result[-1], 'dcba')
    
    def test_permutation_properties(self):
        n = 5
        result = generate_permutations(n)
        
        self.assertEqual(len(result), 120)
        
        for perm in result:
            self.assertEqual(len(perm), n)
            self.assertEqual(len(set(perm)), n)
            self.assertTrue(all('a' <= c <= 'e' for c in perm))
        
        for i in range(len(result) - 1):
            self.assertLess(result[i], result[i + 1])

if __name__ == '__main__':
    unittest.main()
