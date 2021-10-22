from gettext import npgettext

import cv2
import numpy as np
from cv2 import cvtColor, imshow

from unit import *


def process_image():
    global img_show
    img = cv2.imread('16.jpg')
    img_temp = img.copy()
    img = cv2.resize(img, (660, 600))

    img_show = img.copy()
    img_blur = cv2.blur(img, (3, 3))
    img_process = cv2.Canny(img_blur, 30, 100)

    try:
        contours, hierarchy = cv2.findContours(img_process, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        big_contour = list()
        for i in rectContour(contours):
            big_contour.append(i)
        # xử lý phần tô đáp án
        cv2.drawContours(img_show, big_contour[0], -1, (0, 255, 0), 10)
        cv2.drawContours(img_show, big_contour[1], -1, (255, 0, 0), 10)
        cv2.drawContours(img_show, big_contour[2], -1, (0, 0, 255), 10)

        #xử lý đán án
        # căn ảnh từ 4 điểm
        big_contour[0] = reoder(big_contour[0])
        pt1 = np.float32(big_contour[0])
        pt2 = np.float32([[0, 0], [660, 0], [0, 1000], [660, 1000]])
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        img_1 = cv2.warpPerspective(img_show, matrix, (660, 1000))
        img_1_color = cv2.warpPerspective(img_show, matrix, (660, 1000))
        img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
        img_1 = cv2.resize(img_1, (660, 900))
        # img_1_color = cv2.resize(img_1_color, (660, 600))
        # # xử lý mshs
        big_contour[1] = reoder(big_contour[1])
        pt3 = np.float32(big_contour[1])
        pt4 = np.float32([[0, 0], [660, 0], [0, 1000], [660, 1000]])
        matrix = cv2.getPerspectiveTransform(pt3, pt4)
        img_2 = cv2.warpPerspective(img_show, matrix, (660, 1000))
        # ma de
        big_contour[2] = reoder(big_contour[2])
        pt5 = np.float32(big_contour[2])
        pt6 = np.float32([[0, 0], [660, 0], [0, 1000], [660, 1000]])
        matrix = cv2.getPerspectiveTransform(pt5, pt6)
        img_3 = cv2.warpPerspective(img_show, matrix, (660, 1000))

        # chọn ngưỡng màu
        img_1_1 = cv2.threshold(img_1, 100, 255, cv2.THRESH_BINARY_INV)[1]
        matrix_1 = splitBoxes(np.array(img_1_1), 15, 11)
        cv2.imwrite('img_1_1.png', img_1_1)
        C = 0
        R = 0
        myPixel_1_1 = np.zeros((15, 11))
        for i in matrix_1:
            total_ans = cv2.countNonZero(i)
            myPixel_1_1[R][C] = total_ans
            C += 1
            if (C > 10):
                C = 0
                R += 1

        myIndexL = []
        for x in range(0, 15):
            arr = myPixel_1_1[x]
            myIndexAns = [0, 0, 0, 0]
            for i in range(4):
                myIndexAns[i] = arr[i]
            for r1 in range(4):
                if myIndexAns[r1] == np.max(myIndexAns):
                    myIndexL.append(r1)
        #print(myIndexR)

        myIndexR = []
        for x in range(0, 15):
            arr = myPixel_1_1[x]
            myIndexAns = [0, 0, 0, 0]
            for i in range(7, 11):
                myIndexAns[i-8] = arr[i]
            for r1 in range(7, 11):
                if myIndexAns[r1-8] == np.max(myIndexAns):
                    myIndexR.append(r1)
        #print(myIndexL)
        myIndex = []
        for i in range(15):
            myIndex.append(myIndexL[i])
            myIndex.append(myIndexR[i])
        imgRowDra = np.zeros_like(img_1)
        imgRowDra = showAns(img_1, myIndex, 15, 11)

        # id
        big_contour[1] = reoder(big_contour[1])
        pt3 = np.float32(big_contour[1])
        pt4 = np.float32([[0, 0], [660, 0], [0, 1000], [660, 1000]])
        matrix = cv2.getPerspectiveTransform(pt3, pt4)
        img_2 = cv2.warpPerspective(img_show, matrix, (660, 1000))
        img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
        img_2 = cv2.resize(img_2, (720, 900))

        img_2_2 = cv2.threshold(img_2, 100, 255, cv2.THRESH_BINARY_INV)[1]
        matrix_2 = splitBoxes(np.array(img_2_2), 10, 8)

        tdC = 0
        tdR = 0
        my_piexel_id = np.zeros((10, 8))
        for img in matrix_2:
            total_id = cv2.countNonZero(img)
            my_piexel_id[tdR][tdC] = total_id
            tdC += 1
            if tdC == 8:
                tdR += 1
                tdC = 0
        my_piexel_id = np.transpose(my_piexel_id)
        my_index_id = []
        for i in range(8):
            arr = my_piexel_id[i]
            my_index_id_val = np.where(arr == np.amax(arr))
            my_index_id.append(list(my_index_id_val[0]))

        id_student = ''
        for i in range(8):
            id_student += str(my_index_id[i][0])
        # print(id_student)

        #ma de
        big_contour[2] = reoder(big_contour[2])
        pt5 = np.float32(big_contour[2])
        pt6 = np.float32([[0, 0], [660, 0], [0, 1000], [660, 1000]])
        matrix = cv2.getPerspectiveTransform(pt5, pt6)
        img_3 = cv2.warpPerspective(img_show, matrix, (660, 1000))
        img_3 = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)
        img_3 = cv2.resize(img_3, (270, 900))
        img_3_3 = cv2.threshold(img_3, 100, 255, cv2.THRESH_BINARY_INV)[1]
        matrix_3 = splitBoxes(np.array(img_3_3), 10, 3)

        tdC = 0
        tdR = 0
        my_piexel_md = np.zeros((10, 3))
        for img in matrix_3:
            total_md = cv2.countNonZero(img)
            my_piexel_md[tdR][tdC] = total_md
            tdC += 1
            if tdC == 3:
                tdR += 1
                tdC = 0
        my_piexel_md = np.transpose(my_piexel_md)
        my_index_md = []
        for i in range(3):
            arr = my_piexel_md[i]
            my_index_md_val = np.where(arr == np.amax(arr))
            my_index_md.append(list(my_index_md_val[0]))
        md = ''
        for i in range(3):
            md += str(my_index_md[i][0])
        sc = cal_point(myIndex, md)
        if sc > 2 and sc <= 3:
            sc = 3

        img_row_dra = np.zeros_like(img_1_color)
        img_show_2 = img_show.copy()
        img_row_dra = showAns(img_row_dra, myIndex, 15, 11)
        matrix_ques = cv2.getPerspectiveTransform(pt2, pt1)
        img_ques = cv2.warpPerspective(img_row_dra, matrix_ques, (660, 600))

        img_show = cv2.addWeighted(img_ques, 1, img_show, 1, 0)
        cv2.putText(img_show, f'MSSV: {id_student}', (100, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        cv2.putText(img_show, f'MD: {md}', (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)
        cv2.putText(img_show, str(sc), (100, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        # cv2.putText(img3, "MSSV:" + str(ma_so), (100, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    except:
        pass

    cv2.imwrite('process.png', img_show)

    cv2.imshow('img', img_show)
    cv2.waitKey(0)
    cv2.destroyWindow()

    # return id_student, md, sc


# process_image()
