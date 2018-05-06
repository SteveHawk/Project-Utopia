import explore
import workroom
import utime
import life
import dice
import vars
import init


def main():
    print("开始游戏。\n-----------------------")
    init.init()
    while True:
        choice = int(input("你想探索还是回到工作室？（1, 2）"))
        if choice == 1:
            explore.explore()
        elif choice == 2:
            workroom.work()


main()
