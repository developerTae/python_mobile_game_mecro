import pyautogui as pag
import mss, cv2
import numpy as np
import helper

# bluestacks 좌표
# 아이콘 위치
left_icon_pos = {'left': 793, 'top': 725, 'width': 120, 'height': 120}
right_icon_pos = {'left': 1011, 'top': 719, 'width': 120, 'height': 120}

# 버튼 위치
left_button = [696, 856]
right_button = [1105, 826]

while True:

    with mss.mss() as sct:
        left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
        right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]
        helper.mecro(left_img, right_img, left_button, right_button)

# 아이콘 위치를 잘 구했는지 확인
# with mss.mss() as sct:
#     left_img = np.array(sct.grab(left_icon_pos))[:,:,:3]
#     right_img = np.array(sct.grab(right_icon_pos))[:,:,:3]
#
#     cv2.imshow('left_img',left_img)
#     cv2.imshow('right_img',right_img)
#     cv2.waitKey(0)
#
# while True:
#     x, y = pag.position()
#     position_str = 'X: ' + str(x) + 'Y: ' + str(y)
#     print(position_str)

# 마우스 좌표값 구하기
# import pyautogui as pag
#
# while True:
#     x, y = pag.position()
#     position_str = 'X: ' + str(x) + 'Y: ' + str(y)
#     print(position_str)


