import vars
import utime
import dice
import life
import init
import workroom


# 探索的search box游戏
def game():
    # 提示信息
    print("Search Box编号如下：\n"
          " 1 | 2 | 3 \n"
          " 4 | 5 | 6 \n")

    # 初始化search box记录列表 然后三次游戏
    sbox = [0, 0, 0, 0, 0, 0]
    for i in range(3):
        # 掷骰子2d6
        nums = dice.dice(2)
        print("第 {} 次掷得骰子: {}, {}".format(i + 1, nums[0], nums[1]))

        # 获取用户放置位置
        pos = input("放在哪两个位置？（输入两个数字 以空格隔开）\n").split(' ')
        a = int(pos[0])
        b = int(pos[1])

        # 更新sbox
        sbox[a - 1] = nums[0]
        sbox[b - 1] = nums[1]
        print("当前Search Box情况如下：\n"
              " {} | {} | {} \n"
              " {} | {} | {} \n".format(" " if sbox[0] == 0 else sbox[0],
                                        " " if sbox[1] == 0 else sbox[1],
                                        " " if sbox[2] == 0 else sbox[2],
                                        " " if sbox[3] == 0 else sbox[3],
                                        " " if sbox[4] == 0 else sbox[4],
                                        " " if sbox[5] == 0 else sbox[5]))  # 输出当前search box情况

    # 计算结果
    result = (sbox[0] * 100 + sbox[1] * 10 + sbox[2]) - (sbox[3] * 100 + sbox[4] * 10 + sbox[5])
    print("本轮游戏结果为：{}".format(result))
    return result


# 遭遇战
def combat(choice, result):
    # 确定级别
    level = 0
    if 100 <= result <= 199 and -100 <= result <= -1:
        level = 1
    elif 200 <= result <= 299 and -200 <= result <= -101:
        level = 2
    elif 300 <= result <= 399 and -300 <= result <= -201:
        level = 3
    elif 400 <= result <= 499 and -400 <= result <= -301:
        level = 4
    elif 500 <= result <= 555 and -555 <= result <= -401:
        level = 5

    # 游戏
    while True:
        nums = dice.dice(2)
        # 受到攻击
        print("投出两点为 {} 和 {} 。".format(nums[0], nums[1]))
        if vars.Monster[choice - 1][level - 1][0][nums[0] - 1] == 1 or vars.Monster[choice - 1][level - 1][0][
            nums[1] - 1] == 1:
            print("你收到了一点伤害。\n")
            life.life_minus(1)
        # 打死怪物
        if vars.Monster[choice - 1][level - 1][1][nums[0] - 1] == 1 or vars.Monster[choice - 1][level - 1][1][
            nums[1] - 1] == 1:
            print("你获得了胜利。\n")
            # 可能获得零件
            if dice.dice(1) < level:
                vars.Stores[vars.StoresMap[choice]] += 1
                print("你获得了一个零件。\n")
                if vars.Stores[vars.StoresMap[choice]] >= 4:
                    vars.Stores[vars.StoresMap[choice]] = 4
            break


# 处理游戏结果
def deal(result, choice):
    if result == 0:
        print("获得完美零解！")
        # 未获得神之部件
        if not vars.Construct[vars.ConstructMap[choice]]:
            print("test")
            vars.Construct[vars.ConstructMap[choice]] = True
            vars.Activate[vars.ConstructMap[choice]] = True
            vars.GodsHand += 5
            if vars.GodsHand >= 6:
                vars.GodsHand = 6
        # 已经获得神之部件
        else:
            vars.Stores[vars.StoresMap[choice]] += 2
            if vars.Stores[vars.StoresMap[choice]] >= 4:
                vars.Stores[vars.StoresMap[choice]] = 4
    elif 0 < result <= 10:
        print("获得一个神之部件。")
        vars.Construct[vars.ConstructMap[choice]] = True
    elif 11 <= result <= 99:
        print("获得一个道具。")
        vars.Stores[vars.StoresMap[choice]] += 1
        if vars.Stores[vars.StoresMap[choice]] >= 4:
            vars.Stores[vars.StoresMap[choice]] = 4
    else:
        print("你将遭遇一场战斗。\n")
        combat(choice, result)
    return


# 探索
def explore():
    # 预存各个地区的时日表
    daytrack = [[1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0],
                [1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0]]

    # 进行地区操作选择
    choice = int(input("探索哪个地方？\n"
                       "1. HaleBeard Peak\n"
                       "2. The Great Wilds\n"
                       "3. Root Strangled Marshes\n"
                       "4. GlassRock Canyon\n"
                       "5. Ruined City of The Ancients\n"
                       "6. The Fiery Maw\n"
                       "(1-6)? : "))
    for i in range(6):
        # 是否继续判断
        if i != 0:
            if input("是否继续探索？(y,n)") == 'n':
                break

        # 时日表判断
        if daytrack[choice - 1][i] == 1:
            utime.time_add()

        # 进行游戏
        deal(game(), choice)

    print("该地区探索已经结束。")
    return
