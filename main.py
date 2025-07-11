import os
import random
import time

import pyautogui
from action.index import search, continue_game, resize_and_move_window
from check.index import get_current_hand_cards, check_interface
from deploytroops import Deploy_troops


# 初始化“最近发现卡片的时间”
last_card_found_time = time.time()


if __name__ == "__main__":
    # 初始位置
    window_title = "雷电模拟器"
    resize_and_move_window(window_title)

    # 开始匹配,搜索对手
    pyautogui.click(226, 632)

    stormtrooper = ["Giant", "BattleHealer","Lumber", "DarkPrince"]
    ranged_soldier = ["Wiz", "Minions", "SpearGobs", "Skarmy"]
    enemy = ["Barrel", "Rocket", "Fireball"]
    back_row = ["Tombstone"]

    while True:

        continue_ = check_interface((82, 704, 285, 82), "finish",0.7)
        openBox = check_interface((82, 704, 285, 82), "finish2",0.7)
        if continue_:
            # 再来一局
            pyautogui.click(152, 746)  # 开始匹配
        elif openBox:
            # 出去开箱子
            pyautogui.click(219, 745)

        # 检测他是不是箱子
        box = check_interface((24, 44, 397, 71), "box", 0.6)
        if box:
            pyautogui.click(216, 702)


        # 判断是不是首页
        home = check_interface((6, 39, 425, 134), "home")
        if home:
            pyautogui.click(219, 645)

       # 卡槽中的卡片,有就部署
        cards = get_current_hand_cards((stormtrooper,ranged_soldier,enemy,back_row ))
        if len(cards)>0:
            last_card_found_time = time.time()  # 更新时间戳
            Deploy_troops(cards, stormtrooper,ranged_soldier,enemy,back_row )
        else:
            # 当前时间 - 上次发现卡片时间
            idle_duration = time.time() - last_card_found_time

            # 超过 30 分钟 = 1800 秒
            if idle_duration > 1800:
                print("卡槽已空超过30分钟，准备关机...")
                os.system("shutdown /s /t 10")  # Windows关机，延迟10秒执行
                break  # 退出循环，防止多次关机命令

        time.sleep(0.8)