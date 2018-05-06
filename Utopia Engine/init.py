import vars


def init():
    vars.HitPoints = 0
    vars.Time = 0
    vars.MaxTime = 22
    vars.GodsHand = 0
    vars.TimeTrack = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 2, 2, 3, 2, 2, 3, 2, 2]
    vars.Events = {'Active-Monsters': 0, 'Fleeting-Visions': 0, 'Good-Fortune': 0, 'Foul-Weather': 0}
    vars.Stores = {'Lead': 0, 'Quartz': 0, 'Silica': 0, 'Gum': 0, 'Wax': 0, 'Silver': 0}
    vars.ToolBelt = {'Dowsing-Rod': False, 'Paralysis-Wand': False, 'Focus-Charm': False}
    vars.Construct = {'Seal-of-Balance': False, 'Hermetic-Mirror': False, 'Void-Gate': False,
                      'Golden-Chassis': False, 'Scrying-lens': False, 'Crystal-Battery': False}
    vars.Activate = {'Seal-of-Balance': False, 'Hermetic-Mirror': False, 'Void-Gate': False,
                     'Golden-Chassis': False, 'Scrying-lens': False, 'Crystal-Battery': False}
    vars.StoresMap = {1: 'Lead', 2: 'Quartz', 3: 'Silica', 4: 'Gum', 5: 'Wax', 6: 'Silver'}
    vars.ConstructMap = {1: 'Seal-of-Balance', 2: 'Hermetic-Mirror', 3: 'Void-Gate',
                         4: 'Golden-Chassis', 5: 'Scrying-lens', 6: 'Crystal-Battery'}
    vars.Monster = [  # 1. HaleBeard Peak
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
