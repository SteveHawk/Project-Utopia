# 一个暴力 dfs 的搜索。用于和蒙特卡洛树的对比。

import dice
import math
import matplotlib.pyplot as plt
import itertools

# global variables
size = 6
row = 2
column = 3
dicenum = (2, 6)
global tot


def dfs(sbox, vis, count):
    if not count:
        global tot
        tot += 1
        up = [0 for i in range(column)]
        down = [0 for i in range(column)]
        for i in range(row):
            for j in range(column):
                if (i < row / 2):
                    up[j] += sbox[i * column + j]
                else:
                    down[j] += sbox[i * column + j]
        # Add up these numbers under decimal
        result = 0
        for i, j in zip(up, down):
            result *= 10
            result += i - j
        """ Method One """
        if result == 0:
            return 1.0
        elif 0 < result <= 10:
            return 0.95
        elif 10 < result <= 99:
            return 0.9
        else:
            return 0
        """ Method Two """
        # if result == 0:
        #     return 33
        # elif result < 0:
        #     result = abs(result) + 100
        # return 3 * (math.log(result, 0.5) + 10)
    poss = 0
    for i in range(size):
        if vis[i]:
            continue
        vis[i] = 1
        for j in range(1, dicenum[1] + 1):
            sbox[i] = j
            poss += dfs(sbox, vis, count - 1)
        sbox[i] = 0
        vis[i] = 0
    return poss


def treesearch(sbox, nums):
    resulttu = tuple()
    # 初始化vis列表 并且记录未放子的格子数值
    vis = [0 for i in range(size)]
    count = 0
    for i in range(size):
        if not sbox[i]:
            vis[i] = 0
            count += 1
        else:
            vis[i] = 1
    # 把所有的空余位置放于vacancy列表中
    vacancy = [i for i in range(size) if not vis[i]]
    bigpos = -1e5  # 最大值的那个位置
    # 所有可能的操作放在moves里，以((val1, pos1), (val2, pos2), ... ) 的形式
    vacancy_permutes = list(itertools.permutations(vacancy, dicenum[0]))
    moves = set()
    for per in vacancy_permutes:
        moves.add(tuple(map(lambda x, y: (x, y), nums, per)))
    moves = list(moves)
    for move in moves:
        flag = 0
        for pos in move:
            if vis[pos[1]]:
                flag = 1
                break
        else:
            for pos in move:
                vis[pos[1]] = 1
                sbox[pos[1]] = pos[0]
        if flag:
            continue
        count -= dicenum[0]
        poss = dfs(sbox, vis, count)
        count += dicenum[0]
        for pos in move:
            vis[pos[1]] = sbox[pos[1]] = 0
        if poss > bigpos:
            bigpos = poss
            resulttu = move
    return resulttu


def game():
    # 初始化search box记录列表 然后三次游戏
    sbox = [0 for i in range(size)]
    for i in range(int(size / dicenum[0])):
        # 掷骰子
        nums = dice.dice(dicenum[0], dicenum[1])
        global tot
        tot = 0
        resultTuple = treesearch(sbox, nums)
        print(tot)
        # 更新sbox
        for move in resultTuple:
            sbox[move[1]] = move[0]
        s = ''
        for i in range(row):
            for j in range(column):
                s += str(sbox[i * column + j]) + ' '
                if j != column - 1:
                    s += '| '
            s += '\n'
        print(s)

    # 计算结果
    up = [0 for i in range(column)]
    down = [0 for i in range(column)]
    for i in range(row):
        for j in range(column):
            if (i < row / 2):
                up[j] += sbox[i * column + j]
            else:
                down[j] += sbox[i * column + j]
    # Add up these numbers under decimal
    result = 0
    for i, j in zip(up, down):
        result *= 10
        result += i - j
    print("本轮游戏结果为：{}".format(result))
    return result


def test():
    times = 1000
    perfect = 0
    great = 0
    normal = 0
    fail = 0
    plt.axis([0, times, 0, 100])
    plt.ion()
    xax = []
    yax = []
    for i in range(1, times + 1):
        print("No. {} ".format(i))
        result = game()
        if result == 0:
            perfect += 1
        elif 0 < result <= 10:
            great += 1
        elif 11 <= result <= 99:
            normal += 1
        else:
            fail += 1
        print("perfect percentage: {}% \n"
              "great percentage: {}% \n"
              "normal percentage: {}% \n"
              "fail percentage: {}% ".format(100 * perfect / i, 100 * great / i, 100 * normal / i,
                                             100 * fail / i))
        xax.append(i)
        yax.append(100 - 100 * fail / i)
        plt.plot(xax, yax)
        plt.pause(0.01)
    print("perfect: {} , great: {} , normal: {} , fail: {} ".format(perfect, great, normal, fail))
    print("perfect percentage: {}% \n"
          "great percentage: {}% \n"
          "normal percentage: {}% \n"
          "fail percentage: {}% ".format(100 * perfect / times, 100 * great / times, 100 * normal / times,
                                         100 * fail / times))
    input("Wait for keyboard interrupt...")


if __name__ == "__main__":
    test()
