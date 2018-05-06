import vars


def life_check():
    if vars.HitPoints > 6:
        print("游戏结束，你死了。")
        exit()
    else:
        print("当前生命值为：{}".format(6 - vars.HitPoints))


def life_minus(num):
    vars.HitPoints += num
    life_check()


def life_add(num):
    while num > vars.HitPoints:
        num = int(input("血槽溢出...重新输个值？"))
    vars.HitPoints -= num
    life_check()
