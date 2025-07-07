import random
import time

import pyautogui
from action.index import search, continue_game, resize_and_move_window
from check.index import  get_current_hand_cards
from deploytroops import Deploy_troops

if __name__ == "__main__":
    # 初始位置
    window_title = "雷电模拟器"
    resize_and_move_window(window_title)

    # 开始匹配,搜索对手
    pyautogui.click(226, 632)

    stormtrooper = ["Giant", "Lumber", "DarkPrince"]
    ranged_soldier = ["Wiz", "Minions", "SpearGobs", "Skarmy"]
    enemy = ["Barrel", "Rocket", "Fireball"]
    back_row = ["Tombstone"]

    while True:
        #是否搜索到对手
        running = search()

        if running :
            print("匹配到对手，开始分析卡片")

        while running :
            # 卡槽中的卡片
            cards = get_current_hand_cards((stormtrooper,ranged_soldier,enemy,back_row ))


            Deploy_troops(cards, stormtrooper,ranged_soldier,enemy,back_row )

            running = search()
            if not running:
                print("游戏结束，下一把")
                time.sleep(1)
                break

        # 查看是否继续、重新匹配
        continue_game()
        time.sleep(0.8)