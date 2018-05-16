import math
import random
import var


class UtopiaState:
    def __init__(self):
        var.init()
        Time = 0  # 时间进程
        GodsHand = 0  # 上帝之手
        Events = [0, 0, 0, 0]  # 事件 触发区域 0未触发
        Stores = [0, 0, 0, 0, 0, 0]  # 零件 数量
        Construct = [0, 0, 0, 0, 0, 0]  # 部件 0未获得 1获得 2激活
        Tool = [0, 0, 0]  # 工具 0没用过 1使用过
        LegendaryTreasure = [0, 0, 0, 0, 0, 0]  # 传奇物品 0未拥有 1拥有

    def Clone(self):
        """ Create a deep clone of this game state.
        """
        pass

    def DoMove(self, move):
        """ Update a state by carrying out the given move.
            Must update playerJustMoved.
        """
        pass

    def GetMoves(self):
        """ Get all possible moves from this state.
        """
        pass

    def GetResult(self, playerjm):
        """ Get the game result from the viewpoint of playerjm.
        """
        pass

    def __repr__(self):
        """ Don't need this - but good style.
        """
        pass
