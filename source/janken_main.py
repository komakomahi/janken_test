# import player
# import computer
# import janken_judge

# def main():
#    player_win = 0
#    computer_win = 0

#    """3回戦のじゃんけんゲームを行う関数"""
#    # hands = ['グー', 'チョキ', 'パー']

#    round = 1
#    while round <= 3:
#        print(f"-----ラウンド {round} -----")
#        computer_hand = computer.computer_pon()
#        player_hand = player.player_pon()
#        result = janken_judge.judge(computer_hand,player_hand)

#        print(f"あなたの手:{player_hand}")
#        print(f"コンピューターンの手:{player_hand}")

#        print("")  
#        if result == 'draw':
#          print("あいこです！ 再度対決！")    
#        else:
#          round += 1 
#          if result == 'player_win':
#              player_win +=1
#              print("あなたの勝ちです！")
#          else:
#              computer_win +=1
#              print("コンピューターの勝ちです！")            
#        print("")

#    print("【最終結果】")
#    print(f"あなた:{player_win}勝")
#    print(f"コンピュータ:{computer_win}勝")
#    if player_win >= computer_win:
#      print("あなたの総合勝利です！")
#    else:
#       print("コンピュータの総合勝利です！")

# if __name__ == '__main__':
#    main()

from source import player
from source import computer
from source import janken_judge

def play_round(round_num, player_win, computer_win):
    print(f"-----ラウンド {round_num} -----")
    computer_hand = computer.computer_pon()
    player_hand = player.player_pon()
    result = janken_judge.judge(computer_hand, player_hand)

    print(f"あなたの手: {player_hand}")
    print(f"コンピューターの手: {computer_hand}")
    print("")

    if result == 'draw':
        print("あいこです！ 再度対決！")
    else:
        if result == 'player_win':
            player_win += 1
            print("あなたの勝ちです！")
        else:
            computer_win += 1
            print("コンピューターの勝ちです！")
        round_num += 1

    print("")
    return round_num, player_win, computer_win, result

def print_final_result(player_win, computer_win):
    print("【最終結果】")
    print(f"あなた: {player_win}勝")
    print(f"コンピュータ: {computer_win}勝")
    if player_win >= computer_win:
        print("あなたの総合勝利です！")
        return "あなたの総合勝利です！"
    else:
        print("コンピュータの総合勝利です！")
        return "コンピュータの総合勝利です！"

def main():
    player_win = 0
    computer_win = 0
    round_num = 1

    while round_num <= 3:
        round_num, player_win, computer_win, result = play_round(round_num, player_win, computer_win)

    print_final_result(player_win, computer_win)

if __name__ == '__main__':
    main()