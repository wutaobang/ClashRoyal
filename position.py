import pyautogui
import time

print("请把鼠标移动到你想获取坐标的位置，3秒后开始打印坐标，按Ctrl+C退出")

time.sleep(3)

# try:
    # while True:
x, y = pyautogui.position()
print(f"当前鼠标坐标：({x}, {y})", end='\r')
        # time.sleep(0.1)
# except KeyboardInterrupt:
#     print("\n程序结束")
