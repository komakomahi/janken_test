import unittest
from source.janken_judge import judge

class MyTestCase(unittest.TestCase):
   def test_computer(self):
       patterns = [
           ('グー', 'グー','draw'),
           ('グー', 'チョキ','computer_win'),
           ('グー', 'パー','player_win'),
           ('チョキ', 'グー','player_win'),
           ('チョキ', 'チョキ','draw'),
           ('チョキ', 'パー','computer_win'),
           ('パー', 'グー','computer_win'),
           ('パー', 'チョキ', 'player_win'),
           ('パー', 'パー', 'draw'),
       ]

       for computer_hand,player_hand,judge_hand in patterns:
           with self.subTest():
               self.assertEqual(judge(computer_hand, player_hand),judge_hand)
               