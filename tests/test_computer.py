import unittest
from unittest.mock import patch
from source.computer import computer_pon


class TestMyFunction(unittest.TestCase):
    @patch('random.choice', return_value = 'グー')
    def testcomputer(self, mock_input):
        self.assertEqual(computer_pon(), 'グー')
        
    @patch('random.choice', return_value='チョキ')
    def test_input_2(self, mock_input):
       self.assertEqual(computer_pon(), 'チョキ')  
       
    @patch('random.choice', return_value='パー')
    def test_input_3(self, mock_input):
       self.assertEqual(computer_pon(), 'パー')  
    


