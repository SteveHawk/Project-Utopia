import random
import vars


def dice(num, dicerange=6):
    random.seed()
    if num == 1:
        return random.randint(1, dicerange)
    else:
        return tuple(random.randint(1, dicerange) for i in range(num))
