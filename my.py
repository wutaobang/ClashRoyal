import pyautogui
import time
import cv2
import numpy as np

# 识别卡牌区域
def find_card(card_template_path):
    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(card_template_path, 0)

    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.9:  # 阈值
        return max_loc
    return None

# 拖动卡牌
def play_card(card_path, drop_position):
    pos = find_card(card_path)
    if pos:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.dragTo(drop_position[0], drop_position[1], duration=0.5)

import pyautogui
import cv2
import numpy as np

def is_game_running(game_logo_path, threshold=0.9):
    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(game_logo_path, 0)
    if template is None:
        print(f"未找到游戏logo模板图：{game_logo_path}")
        return False

    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(res)
    return max_val >= threshold

# 使用示例
if not is_game_running("game_logo.png"):
    print("游戏界面未打开，请先启动游戏！")
    exit(1)  # 退出脚本
else:
    print("检测到游戏界面，开始自动操作。")

# # 主循环
# while True:
#     play_card("archer.png", (500, 700))  # 假设拖到某处
#     time.sleep(5)
