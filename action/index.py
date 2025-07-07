import time

import pyautogui
import pygetwindow as gw
from check.index import check_interface, check_game_end

def resize_and_move_window(window_title, target_width=480, target_height=820, target_left=0, target_top=0):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f"未找到窗口：{window_title}")
        return False

    win = windows[0]
    print(f"当前窗口位置和大小：({win.left}, {win.top}), {win.width}x{win.height}")

    # 调整大小
    win.resizeTo(target_width, target_height)
    time.sleep(0.5)  # 等待窗口调整完成

    # 移动到指定位置
    win.moveTo(target_left, target_top)
    time.sleep(0.5)  # 等待窗口移动完成

    print(f"已调整窗口到位置和大小：({win.left}, {win.top}), {win.width}x{win.height}")
    return True

def start_match():
    """点击按钮：开始游戏"""
    pyautogui.click(226, 632)  # 开始匹配

    # 查看有没有匹配到对手
    while not search():
        time.sleep(0.8)
    print("匹配成功")
    return True

def search():
    result = check_interface((180, 523, 82, 92), "start")
    return result

def continue_game():
    status = check_game_end()
    if status == "再来一局":
        pyautogui.click(152, 746)  # 开始匹配
        while search():
            time.sleep(1)
            break
    elif status == "确认":
        pyautogui.click(219, 745)

        while True:
            home = check_interface((6, 39, 425, 134),"home")
            if home:
                pyautogui.click(219, 645)
                while True:
                    time.sleep(5)
                    box = check_interface((24, 44, 397, 71), "box",0.6)
                    if box:
                        pyautogui.click(216, 702)
                    else:
                        break
            # else:
                # break
            time.sleep(2)

def drag_card_to(center, release_position, hold_time=0.05, move_time=0.3, delay_after=1):
    """
    拖动卡牌从中心位置到目标释放位置

    参数：
    - center: 卡牌中心坐标(x,y)
    - release_position: 释放位置坐标 (x, y)
    - hold_time: 按住鼠标后停留时间（默认 0.05 秒）
    - move_time: 拖动所需时间（默认 0.3 秒）
    - delay_after: 拖放结束后等待时间（默认 1 秒）
    """
    pyautogui.moveTo(center[0], center[1], duration=0.2)
    pyautogui.mouseDown()
    time.sleep(hold_time)

    pyautogui.moveTo(release_position[0], release_position[1], duration=move_time)
    time.sleep(0.05)
    pyautogui.mouseUp()

    time.sleep(delay_after)
