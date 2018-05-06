import vars


def time_check():
    # 超时
    if vars.Time > vars.MaxTime:
        print("超时。游戏结束。")
        exit()

    # 骷髅头
    if vars.TimeTrack[vars.Time - 1] >= 2:
        if vars.GodsHand < 3:
            print("世界末日。游戏结束。")
            exit()
        else:
            vars.GodsHand -= 3

    # 事件
    if vars.TimeTrack[vars.Time - 1] == 1 or vars.TimeTrack[vars.Time - 1] == 3:
        pass

    print("时间进度：")
    print("|", end='')
    for i in range(vars.Time):
        print('#', end='')
    for i in range(vars.Time, vars.MaxTime):
        if vars.TimeTrack[i] >= 2:
            print('×', end='')
        else:
            print('▢', end='')
    print("|\n")


def time_add(num=1):
    vars.Time += num
    time_check()
