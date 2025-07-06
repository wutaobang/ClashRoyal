import random
import time

import pyautogui
from action.index import start_match, search, continue_game, drag_card_to, resize_and_move_window
from check.index import check_game_end, check_interface, tower_status, get_current_hand_cards
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



# dash_position = [(67, 397), (372, 394)]
# vice_position = [(42, 480), (380, 470)]
# room_inter_position = [(168, 579), (262, 575)]


# while True:
#     cards = get_current_hand_cards(
#         card_templates= ["Wiz", "Minions", "Barrel", "Giant","DarkPrince",
#                           "SpearGobs", "Rocket", "Fireball", "Lumber",
#                           "Skarmy", "Tombstone"])
#
#     # valid_cards = [card for card in cards if card["card_name"] != "未知卡牌"]
#     if not cards:
#         time.sleep(1)
#         print("⚠ 无可用卡牌出牌（全是未知卡牌）")
#
#     if cards:
#         selected_card = random.choice(cards)
#         # card_index = cards.index(selected_card)
#         # 获取卡牌中心坐标
#         x, y, w, h= selected_card["region"] #card_regions[card_index]
#          # = region
#         center = (x + w // 2, y + h // 2)
#
#         if selected_card in ["Barrel.png","Rocket.png", "Fireball.png"]:
#             print(selected_card)
#             # 查看没有的塔
#             tower = tower_status()
#             # print(selected_card,tower)
#             drag_card_to(center, tower_loc[tower])
#         elif selected_card in ["Guant.png","DarkPrince.png","Barrel.png"]:
#             print(selected_card)
#             drag_card_to(center, random.choice(dash_position))
#         elif selected_card in ["Wiz.png","SpearGobs.png","Minions.png","Skarmy.png"]:
#             print(selected_card)
#             drag_card_to(center, random.choice(vice_position))
#         elif selected_card in ["Tombstone.png"]:
#             print(selected_card)
#             drag_card_to(center, random.choice(room_inter_position))
#         else:
#             print("没有牌")
#     # 查看是否继续、重新匹配
#     continue_game()
#     time.sleep(0.8)
# release_position = (385, 400)
# resize_and_move_window(window_title = "雷电模拟器")
# if __name__ == "__main__":
#     # 替换成你模拟器或游戏窗口的标题关键字
#     if success:
#         print("窗口调整完成")
#         # press_match()
#         time.sleep(0.5)
#         while True:
#             cards = get_current_hand_cards()
#             valid_cards = [card for card in cards if card != "未知卡牌"]
#             if not valid_cards:
#                 time.sleep(3)
#                 print("⚠ 无可用卡牌出牌（全是未知卡牌）")
#                 if is_finish():
#                     print("结束")
#                     pyautogui.click(142, 752)  # 开始匹配
#                     while matching():
#                         time.sleep(2)
#                         break
#
#             else:
#                 selected_card = random.choice(valid_cards)
#                 print(selected_card)
#                 card_index = cards.index(selected_card)
#                 time.sleep(0.3)
#                 if selected_card == "Barrel.png" or "Fireball.png" in valid_cards:
#                     region = card_regions[card_index]
#                     # 获取卡牌中心坐标
#                     x, y, w, h = region
#                     center_x = x + w // 2
#                     center_y = y + h // 2
#                     time.sleep(0.05)
#                     pyautogui.moveTo(center_x, center_y, duration=0.2)
#                     pyautogui.mouseDown()
#                     b = [(105, 198), (330, 198)]
#                     release_position = random.choice(b)
#                     pyautogui.moveTo(release_position[0], release_position[1], duration=0.3)
#                     pyautogui.mouseUp()
#                     time.sleep(1)
#                     pyautogui.mouseUp()
#                 else:
#                     region = card_regions[card_index]
#                 # 获取卡牌中心坐标
#                     x, y, w, h = region
#                     center_x = x + w // 2
#                     center_y = y + h // 2
#                 # 执行点击（可加 pyautogui.mouseDown/Up 拖动）
#                 # 拖动出牌
#                     # 拖动出牌
#                     # pyautogui.moveTo(center_x, center_y, duration=0.2)
#                     # pyautogui.mouseDown()
#                     time.sleep(0.05)
#                     release_x = random.randint(54, 423)
#                     release_y = random.randint(342, 530)
#                     release_position = (release_x, release_y)
#                     # print(release_position)
#                     pyautogui.moveTo(center_x, center_y, duration=0.2)
#                     pyautogui.mouseDown()
#                     pyautogui.moveTo(release_position[0], release_position[1], duration=0.3)
#                     pyautogui.mouseUp()
#                     time.sleep(1)
#                     pyautogui.mouseUp()
#
#                 if is_finish():
#                     print("结束")
#                         # pyautogui.click(226, 632)  # 开始匹配
#                     while matching():
#                         time.sleep(0.8)
#                         break
#     else:
#         print("窗口调整失败")