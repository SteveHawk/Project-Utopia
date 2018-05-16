Life = 0
MaxTime = 0
TimeTrack = []
EventsMap = {}
StoresMap = {}
ConstructMap = {}
ToolMap = {}
LegendaryTreasuresMap = {}
Monster = []


def init():
    global Life  # 生命值
    global MaxTime  # 游戏最大时长
    global TimeTrack  # 时间表 0正常 1事件 2世界末日 3末日+事件
    global EventsMap  # 事件 对照表
    global StoresMap  # 零件 对照表
    global ConstructMap  # 部件 对照表
    global ToolMap  # 工具 对照表
    global Monster  # 各区域 各级别 怪兽攻击/命中数值 对照表
    global LegendaryTreasureMap  # 传奇物品 对照表

    Life = 6
    MaxTime = 22
    TimeTrack = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 2, 2, 3, 2, 2, 3, 2, 2]
    EventsMap = {0: 'Active-Monsters', 1: 'Fleeting-Visions', 2: 'Good-Fortune', 3: 'Foul-Weather'}
    StoresMap = {0: 'Lead', 1: 'Quartz', 2: 'Silica', 3: 'Gum', 4: 'Wax', 5: 'Silver'}
    ConstructMap = {0: 'Seal-of-Balance', 1: 'Hermetic-Mirror', 2: 'Void-Gate',
                    3: 'Golden-Chassis', 4: 'Scrying-lens', 5: 'Crystal-Battery'}
    ToolMap = {0: 'Dowsing-Rod', 1: 'Paralysis-Wand', 2: 'Focus-Charm'}
    LegendaryTreasureMap = {0: 'Ice Plate', 1: 'Bracelet of Ios', 2: 'Shimmering Moonlace',
                            3: 'Scale of The Infinity Wurm', 4: 'The Ancient Record', 5: 'The Molten Shard'}
    Monster = [  # 1. HaleBeard Peak
        [[[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1]]],
        # 2. The Great Wilds
        [[[1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1]]],
        # 3. Root Strangled Marshes
        [[[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1]]],
        # 4. GlassRock Canyon
        [[[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1]]],
        # 5. Ruined City of The Ancients
        [[[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1]]],
        # 6. The Fiery Maw
        [[[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1]],
         [[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1]],
         [[1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1]]]
    ]
