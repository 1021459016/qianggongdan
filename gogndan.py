import re
import cv2
import os
import pyperclip
import pyautogui
import time


def find_img(img, need_img=False, similarity=0.97):
    if need_img == True:
        im = pyautogui.screenshot()
        im.save('screen.png')
    screen = cv2.imread('./screen.png')
    joinMeeting = cv2.imread(img)
    result = cv2.matchTemplate(joinMeeting, screen, cv2.TM_CCOEFF_NORMED)
    pos_start = cv2.minMaxLoc(result)[3]  # 获取最相似点相似坐标
    The_most_similar_scores = cv2.minMaxLoc(result)[1]  # 获取相似度
    print('相似度：', The_most_similar_scores)
    if The_most_similar_scores > similarity:
        x = int(pos_start[0]) + int(joinMeeting.shape[1] / 2)
        y = int(pos_start[1]) + int(joinMeeting.shape[0] / 2)
        return x, y
    return False

# 发送消息


def send_msg(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

# 搜索输入框


def search_input():
    x, y = find_img('./input.png', similarity=0.5)
    pyautogui.click(x, y)
    # pyautogui.hotkey ('enter')

# def if_DEV():
#     if find_img('./SAS-W.png', need_img=True, similarity=0.5) != False:
#         return True
#     return False


while True:
    try:
        x, y = find_img('./msg.png', need_img=True)
        pyautogui.click(x, y)
        search_input()
        send_msg('1')
        time.sleep(3)
    except Exception as e:
        print('未发现新工单，3s后继续识别')
        time.sleep(3)
