
import unittest
import fcs

class TestFcs(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = fcs.fcs_text(text)
        self.assertEqual(result,'Python')
        
    def test_multiple_word(self):
        text = 'selvam pythonist'
        result = fcs.fcs_text(text)
        self.assertEqual(result,'Selvam Pythonist')

if __name__ == '__main__':
    unittest.main()
