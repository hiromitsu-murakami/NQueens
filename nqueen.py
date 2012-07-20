#!/usr/bin/env python
# -*- coding: utf-8 -*-

# N-Queens

import copy
import time

# 7x7作成
def make_matrix(n):
    matrix = []
    for x in range(n):
        array = []
        for y in range(n):
            array.append(True)
        matrix.append(array)
    return matrix

# クイーンの範囲を無効化
def add_hand(hands, matrix, qx, qy):
    hands.append([qx, qy])
    for (mx, array) in enumerate(matrix):
        for (my, b) in enumerate(array):
            if mx == qx:
                matrix[mx][my] = False
            if my == qy:
                matrix[mx][my] = False
            if (mx+my) == (qx+qy):
                matrix[mx][my] = False
            if (mx-my) == (qx-qy):
                matrix[mx][my] = False

# クイーンを置く（再帰）
def hand(hands, matrix, qx, found, n):
    for mx in range(qx, n):
        # 各行に必ず１つクイーンがなければN個に届かない
        if len(hands) < mx:
            return found
        
        for my in range(n):
            if matrix[mx][my]:
                alt_hands  = copy.deepcopy(hands)
                alt_matrix = copy.deepcopy(matrix)

                add_hand(alt_hands, alt_matrix, mx, my)
                found = hand(alt_hands, alt_matrix, mx+1, found, n)
    
    # N個あれば解のひとつ
    if len(hands) >= n:
        found += 1
        # print(hands)

    return found

# N-Queens
def queen_all(n):
    found  = 0
    hands  = []
    matrix = make_matrix(n)

    return hand(hands, matrix, 0, 0, n)

# 実行
n = 9
a = time.time()
found = queen_all(n)
b = time.time()
print('%.3f secs' % (b-a))
print('%d Queens' % (n))
print('%d All Patterns' % (found))
print('')
# print('(8:92 9:352 10:724 11:2680 12:14200)')
# print('')
