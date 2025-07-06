import random
import time

from action.index import drag_card_to
from check.index import tower_status

# 敌方塔的位置
tower_loc = {
    "left": (103, 187),
    "right": (317, 187),
    "king": (220, 120)
}

# 桥头旁边、冲锋
dash_position = [(67, 397), (372, 394)]
# 桥头后面一点的，远程、法师、射手之类
vice_position = [(42, 480), (380, 470)]
# 大本两测、建筑类
room_inter_position = [(168, 579), (262, 575)]

# 兵种部署位置分析
def Deploy_troops(cards,stormtrooper,ranged_soldier,enemy,back_row):
    if not cards:
        time.sleep(1)
        print("⚠ 无可用卡牌出牌（全是未知卡牌）")
        return

    selected_card = random.choice(cards)
    card_name =selected_card["card_name"]
    print(selected_card)
    # 获取卡牌中心坐标
    x, y, w, h= selected_card["region"]
    center = (x + w // 2, y + h // 2)

    # 法术部署在敌方位置
    if card_name in enemy:
        # 查看没有的塔
        tower = tower_status()
        drag_card_to(center, tower_loc[tower])
    elif card_name in stormtrooper:
        drag_card_to(center, random.choice(dash_position))
    elif card_name in ranged_soldier:
        drag_card_to(center, random.choice(vice_position))
    elif card_name in back_row:
        drag_card_to(center, random.choice(room_inter_position))
    else:
        print("没有卡片、或者圣水了")

