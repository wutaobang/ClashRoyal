import numpy as np
import pyautogui




def getColorByAverage(loc,width,height):
    """
       获取屏幕上某一片区域内像素的平均 RGB 值
       :param loc: 区域左上角坐标 (x, y)
       :param width: 区域宽度
       :param height: 区域高度
       :return: 平均 (r, g, b)
       """
    x, y = loc
    # 截图区域
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    # 转换成 numpy 数组
    img_np = np.array(screenshot)
    # 去掉 alpha 通道（如果有）
    if img_np.shape[2] == 4:
        img_np = img_np[:, :, :3]
    # 计算平均值
    average_color = tuple(np.mean(img_np.reshape(-1, 3), axis=0).astype(int))
    return average_color