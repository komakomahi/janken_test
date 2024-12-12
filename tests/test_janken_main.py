import unittest
from unittest.mock import patch
from source.janken_main import play_round, print_final_result

class TestJankenMain(unittest.TestCase):

    @patch('source.computer.computer_pon',return_value = 'グー')
    @patch('source.player.player_pon',return_value = 'パー')
    @patch('source.janken_judge.judge',return_value = 'player_win')
    def test_play_round1(self,mock_judge,mock_player,mock_computer):
        round_num, player_win, computer_win, result = play_round(1, 0, 0)
        self.assertEqual(round_num, 2)
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 0)
        self.assertEqual(result, 'player_win')
        
    @patch('source.computer.computer_pon',return_value = 'チョキ')
    @patch('source.player.player_pon',return_value = 'パー')
    @patch('source.janken_judge.judge',return_value = 'computer_win')
    def test_play_round2(self,mock_judge,mock_player,mock_computer):
        round_num, player_win, computer_win, result = play_round(2, 0, 0)
        self.assertEqual(round_num, 3)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 1)
        self.assertEqual(result, 'computer_win')
    
    @patch('source.computer.computer_pon',return_value = 'チョキ')
    @patch('source.player.player_pon',return_value = 'パー')
    @patch('source.janken_judge.judge',return_value = 'draw')
    def test_play_round3(self,mock_judge,mock_player,mock_computer):
        round_num, player_win, computer_win, result = play_round(1, 0, 0)
        self.assertEqual(round_num, 1)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 0)
        self.assertEqual(result, 'draw')
        
    
    def test_print_final_result(self):
        patterns = [
            (3,0,'あなたの総合勝利です！'),
            (2,1,'あなたの総合勝利です！'),
            (0,3,'コンピュータの総合勝利です！'),
            (1,2,'コンピュータの総合勝利です！'),
        ]
        
        for player_win, computer_win, result in patterns:
            with self.subTest():
                self.assertEqual(print_final_result(player_win,computer_win),result)
        
    