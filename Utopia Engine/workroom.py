import init
import vars
import utime
import life
import dice


# 工作室工作
def work():
    choice = int(input("你想做什么？\n"
                       "1. 回血\n"
                       "2. 激活部件\n"
                       "3. 链接零件\n "))
    if choice == 1:
        recover()
    elif choice == 2:
        activate()
    elif choice == 3:
        activate()


# 回血
def recover():
    choice = int(input("你想回几滴血？"))
    life.life_add(choice)
    utime.time_add(choice)


# 激活
def activate():
    flag = False  # 是否有未激活的部件
    # 遍历六个部件 看有没有拥有且没激活的
    for i in range(6):
        if vars.Construct[vars.ConstructMap[i + 1]] and not vars.Activate[vars.ConstructMap[i + 1]]:  # 找到
            if not flag:  # 如果是第一个 就在前面加上提示语
                print("你想激活哪个神之部件？")
            flag = True
            print("{}. {}".format(i + 1, vars.ConstructMap[i + 1]))
    if flag == 0:  # 如果没有找到能激活的
        print("没有找到能激活的部件。")
        return
    else:
        choice = int(input())  # 用户选择
        print("即将激活 {} 。".format(vars.ConstructMap[choice]))

    # 开始游戏*2
    for i in range(2):
        # 编号说明
        print("第 {} 个激活通道的位置编号：".format(i + 1))
        print(" 1 | 2 | 3 \n"
              " 4 | 5 | 6 \n"
              "-----------\n"
              " * | * | * \n")

        # 开始游戏
        field = ['_', '_', '_', '_', '_', '_']
        result = ['*', '*', '*']
        tot = 0
        energy = 0
        while tot < 6:
            tot += 2
            # 掷骰子
            nums = dice.dice(2)
            place_choice = input("掷得骰子：{} 和 {} \n"
                                 "你想放在什么地方？（输入两个数字 以空格隔开）".format(nums[0], nums[1])).split(" ")
            field[int(place_choice[0]) - 1] = nums[0]
            field[int(place_choice[1]) - 1] = nums[1]

            # 更新结果
            if field[0] != '_' and field[3] != "_":
                result[0] = field[0] - field[3]
            if field[1] != '_' and field[4] != "_":
                result[1] = field[1] - field[4]
            if field[2] != '_' and field[5] != "_":
                result[2] = field[2] - field[5]

            # 输出情况
            print("当前激活通道的状况：\n"
                  + " {} | {} | {} \n".format(field[0], field[1], field[2])
                  + " {} | {} | {} \n".format(field[3], field[4], field[5])
                  + "-----------\n"
                  + " {} | {} | {} \n".format(result[0], result[1], result[2]))

            # 判断是否有特殊情况
            flag = False  # 是否出现过特殊现象
            for j in range(3):
                if result[j] == 0:
                    flag = True
                    print("第 {} 列出现零解。".format(j + 1))
                    tot -= 2
                    field[j] = field[j + 3] = '_'
                    result[j] = '*'
                elif type(result[j]) == int and result[j] < 0:
                    flag = True
                    print("第 {} 列出现负解。零件走火，伤害一点生命值。".format(j + 1))
                    life.life_minus(1)

            # 如果有特殊 就再输出一下
            if flag:
                print("当前激活通道的状况：\n"
                      + " {} | {} | {} \n".format(field[0], field[1], field[2])
                      + " {} | {} | {} \n".format(field[3], field[4], field[5])
                      + "-----------\n"
                      + " {} | {} | {} \n".format(result[0], result[1], result[2]))

        # 计算能量
        for j in range(3):
            if result[j] == 4:
                energy += 1
            elif result[j] == 5:
                energy += 2
        if energy >= 4:
            print("成功激活 {} 。另外获得 {} 点上帝之手能量。".format(vars.ConstructMap[choice], energy - 4))
            vars.Activate[vars.ConstructMap[choice]] = True
            vars.GodsHand += energy - 4
            break
        else:
            print("能量总量 {} ，能量不足，激活失败。".format(energy))
            if i == 0:
                print("耗费一天开启第二个激活通道。")
            elif i == 1:
                print("未成功激活。耗费一天时间强行激活。")
                vars.Activate[vars.ConstructMap[choice]] = True
            utime.time_add(1)


# 链接
def link():
    pass
