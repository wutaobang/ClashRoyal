import cv2
import numpy as np
import pyautogui

# 比较器
def check_interface(region,template,threshold=0.8):
    screenshot = pyautogui.screenshot(region=region)
    screen_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(f"./picture/interface/{template}.png", 0)

    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(res)

    if max_val>=threshold:
        return True
    else:
        return False

# 检查游戏是否结束
def check_game_end():
    template1 = cv2.imread(r".\picture\interface\finish.png", 0)
    template2 = cv2.imread(r".\picture\interface\finish2.png", 0)
    screenshot = pyautogui.screenshot(region=(82, 704, 285, 82))
    screen_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)

    # 匹配 template1
    res1 = cv2.matchTemplate(screen_gray, template1, cv2.TM_CCOEFF_NORMED)
    _, max_val1, _, _ = cv2.minMaxLoc(res1)

    # 匹配 template2
    res2 = cv2.matchTemplate(screen_gray, template2, cv2.TM_CCOEFF_NORMED)
    _, max_val2, _, _ = cv2.minMaxLoc(res2)

    if max_val1 > 0.7 :
        return "再来一局"
    elif max_val2 > 0.7:
        return "确认"

    return False

# 查看塔的状态
def tower_status():
    left = check_interface((87,187,41,33),"ruins",0.7)
    right = check_interface((317, 187, 41, 33), "ruins",0.7)
    if right and not left:
        return "king"
    elif left and not right:
        return "king"
    elif left and right:
        return "king"
    else:
        return "left"

# 比较卡牌，分析是那张卡片
def match_card(screenshot_img,card_templates=None, templates_dir="./picture/deck/", threshold=0.6):
    """对一张卡牌截图，匹配并返回匹配到的卡牌名"""
    if card_templates is None:
        card_templates = ["Wiz", "Minions", "Barrel", "Giant","DarkPrince",
                          "SpearGobs", "Rocket", "Fireball", "Lumber",
                          "Skarmy", "Tombstone"]

    # 转为 OpenCV 格式
    img = cv2.cvtColor(np.array(screenshot_img), cv2.COLOR_RGB2GRAY)
    best_match = None
    best_score = 0

    for template_name in card_templates:
        template_path = templates_dir + template_name+".png"
        template = cv2.imread(template_path, 0)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)

        if max_val > best_score:
            best_score = max_val
            best_match = template_name

    if best_score >= threshold:
        return best_match
    else:
        return "未知卡牌"

# 卡槽的卡牌
def get_current_hand_cards(groups=None,card_regions=None):
    """识别当前手牌 4 张，返回卡牌文件名列表"""
    if card_regions is None:
        card_regions = [
            (101, 689, 72, 89),
            (183, 689, 72, 89),
            (267, 689, 72, 89),
            (350, 689, 72, 89)
        ]

    hand_cards = []

    # 自动展开多个数组组合成一个大数组
    card_templates = []
    for group in groups:
        card_templates.extend(group)

    for idx, region in enumerate(card_regions):
        img = pyautogui.screenshot(region=region)
        card_name = match_card(img,card_templates)

        if card_name !="未知卡牌":
            hand_cards.append({
                "card_name":card_name,
                "region":region
            })

    return hand_cards
