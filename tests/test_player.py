  
import unittest
from unittest.mock import patch
from source.player import player_pon

class TestPlayerPon(unittest.TestCase):
 
    @patch('builtins.input', return_value='1')#1を不正に入力して、絶対グーしか出ないように
    def test_input_1(self, mock_input):
        self.assertEqual(player_pon(), 'グー')#player_pon()のreturnがグー＝グーだったらおｋ
      

    @patch('builtins.input', return_value='2')
    def test_input_2(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')
       
    @patch('builtins.input', return_value='3')
    def test_input_3(self, mock_input):
        self.assertEqual(player_pon(), 'パー')
    #不正な入力の後に有効な入力
    @patch('builtins.input', side_effect=['0', '4', '2'])
    def test_input4(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')

