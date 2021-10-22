from builtins import list

import cv2
import numpy as np
from readAns import Ans


def getCornerPoints():
    pass


def sort(list_number):
    result = list()
    list_number_before_sort = list(list_number)
    for i in list_number:
        min_ = min(list_number_before_sort)
        list_number_before_sort.remove(min_)
        result.append(min_)
    result.reverse()
    return result


def get_list_max(list_area, list_approx):
    result = list()
    list_area_sorted = sort(list_area)

    # data = list()
    for i in range(3):
        index = list_area.index(list_area_sorted[i])
        result.append(list_approx[index])

    return result


def rectContour(contours):
    result = list()
    list_area = list()
    list_approx = list()
    for con in contours:
        area = cv2.contourArea(con)
        if area > 300:
            pori = cv2.arcLength(con, True)
            approx = list(cv2.approxPolyDP(con, pori * 0.02, True))
            if len(approx) == 4:
                list_area.append(area)
                list_approx.append(approx)

    result = get_list_max(list_area, list_approx)
    return result


def reoder(my_point):
    my_point = np.array(my_point).reshape(4, 2)
    add = my_point.sum(1)
    my_new_point_0 = my_point[np.argmin(add)]
    my_new_point_3 = my_point[np.argmax(add)]
    diff = np.diff(my_point, axis=1)
    my_new_point_1 = my_point[np.argmin(diff)]
    my_new_point_2 = my_point[np.argmax(diff)]
    return my_new_point_0, my_new_point_1, my_new_point_2, my_new_point_3


def splitBoxes(img, row, col):
    result = []
    r = np.vsplit(img, row)
    for i in r:
        c = np.hsplit(i, col)
        for box in c:
            result.append(box)

    return result


def showAns(img, myIndex, row, col):
    secW = int(img.shape[1] / col)
    secH = int(img.shape[0] / row / 2)

    x = 0
    y = 1
    while x <= 30 and y <= 30:
        myColor = (0, 255, 0)
        myAns = int(myIndex[x])
        cx = myAns * secW + secW // 2
        cy = x * secH + secH
        cv2.circle(img, (cx, cy), 20, myColor, cv2.FILLED)

        myAns = int(myIndex[y])
        cx = myAns * secW + secW // 2
        cy = y * secH
        cv2.circle(img, (cx, cy), 20, myColor, cv2.FILLED)

        x += 2
        y += 2
    return img


def cal_point(list_ans, md):
    ans = Ans('dapAN.xlsx')
    list_base = ans.readAns(md)
    for i in range(30):
        if i % 2 == 0:
            if list_base[i] == 'A':
                list_base[i] = 0
            if list_base[i] == 'B':
                list_base[i] = 1
            if list_base[i] == 'C':
                list_base[i] = 2
            if list_base[i] == 'D':
                list_base[i] = 3
        if i % 2 == 1:
            if list_base[i] == 'A':
                list_base[i] = 7
            if list_base[i] == 'B':
                list_base[i] = 8
            if list_base[i] == 'C':
                list_base[i] = 9
            if list_base[i] == 'D':
                list_base[i] = 10

    score = 0
    for i in range(30):
        if list_ans[i] == list_base[i]:
            score += 1

    point = score / 30 * 10
    return point