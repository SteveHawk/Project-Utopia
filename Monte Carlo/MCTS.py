# This is a very simple implementation of the UCT Monte Carlo Tree Search algorithm in Python 2.7 (convert to Python3).
# The function UCT(rootstate, itermax, verbose = False) is towards the bottom of the code.
# It aims to have the clearest and simplest possible code, and for the sake of clarity, the code
# is orders of magnitude less efficient than it could be made, particularly by using a
# state.GetRandomMove() or state.DoRandomRollout() function.
#
# Example GameState classes for Nim, OXO and Othello are included to give some idea of how you
# can write your own GameState use UCT in your 2-player game. Change the game to be played in
# the UCTPlayGame() function at the bottom of the code.
#
# Written by Peter Cowling, Ed Powley, Daniel Whitehouse (University of York, UK) September 2012.
#
# Licence is granted to freely use and distribute for any sensible/legal purpose so long as this comment
# remains in any distributed code.
#
# For more information about Monte Carlo Tree Search check out our web site at www.mcts.ai

from math import *
import random
import dice
import copy
import itertools
import matplotlib.pyplot as plt
import multiprocessing
import time

excellent_edge = 0
great_edge = 10
good_edge = 99
dicenum = (2, 6)


class UtopiaState:
    """ A state of the game, i.e. the game board. These are the only functions which are
        absolutely necessary to implement UCT in any 2-player complete information deterministic
        zero-sum game, although they can be enhanced and made quicker, for example by using a
        GetRandomMove() function to generate a random move during rollout.
        By convention the players are numbered 1 and 2.
    """

    def __init__(self):
        self.size = 6
        self.row = 2
        self.column = 3
        self.board = [0 for i in range(self.size)]

    def Clone(self):
        """ Create a deep clone of this game state.
        """
        st = copy.deepcopy(self)
        return st

    def DoMove(self, move):
        """ Update a state by carrying out the given move.
            Move is in the form of ((val1, pos1), (val2, pos2), ... )
        """
        for mo in move:
            self.board[mo[1]] = mo[0]

    def GetMoves(self):
        """ Get all possible moves from this state.
        """
        # list all the moves
        vacancy = [i for i in range(self.size) if self.board[i] == 0]
        choice = dice.dice(dicenum[0], dicenum[1])
        vacancy_permuts = list(itertools.permutations(vacancy, dicenum[0]))
        ans = set()
        for per in vacancy_permuts:
            ans.add(tuple(map(lambda x, y: (x, y), choice, per)))
        # make sure unique
        ans = list(ans)
        return ans

    def GetResult(self):
        """ Get the game result.
        """
        # If haven't reach to the end, return false
        if self.GetMoves() != []:
            return False

        # Add up up-half and down-half numbers
        up = [0 for i in range(self.column)]
        down = [0 for i in range(self.column)]
        for i in range(self.row):
            for j in range(self.column):
                if (i < self.row / 2):
                    up[j] += self.board[i * self.column + j]
                else:
                    down[j] += self.board[i * self.column + j]

        # Add up these numbers under decimal
        result = 0
        for i, j in zip(up, down):
            result *= 10
            result += i - j
        """ Method One """
        # if result == 0:
        #     return 0, 33
        # elif result < 0:
        #     result = abs(result) + 100
        # return result, 3 * (log(result, 0.5) + 10)
        """ Method Two """
        if result == excellent_edge:
            return result, 1.0
        elif excellent_edge < result <= great_edge:
            return result, 0.95
        elif great_edge < result <= good_edge:
            return result, 0.9
        else:
            return result, 0

    def __repr__(self):
        """ Show the state of the board.
        """
        s = ''
        for i in range(self.row):
            for j in range(self.column):
                s += str(self.board[i * self.column + j]) + ' '
                if j != self.column - 1:
                    s += '| '
            s += '\n'
        return s


class Node:
    """ A node in the game tree.
        Crashes if state not specified.
    """

    def __init__(self, move=None, parent=None, state=None):
        self.move = move  # the move that got us to this node - "None" for the root node
        self.parentNode = parent  # "None" for the root node
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = state.GetMoves()  # future child nodes

    def UCTSelectChild(self):
        """ Use the UCB1 formula to select a child node. Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits to vary the amount of
            exploration versus exploitation.
        """
        s = \
            sorted(self.childNodes,
                   key=lambda c: c.wins / (c.visits + 1) + sqrt(5 * log(self.visits) / (c.visits + 1)))[
                -1]
        return s

    def AddChild(self, m, s):
        """ Remove m from untriedMoves and add a new child node for this move.
            Return the added child node
        """
        n = Node(move=m, parent=self, state=s)
        try:
            self.untriedMoves.remove(m)
        except:
            pass
        self.childNodes.append(n)
        return n

    def Update(self, result):
        """ Update this node - one additional visit and result additional wins.
        """
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(
            self.untriedMoves) + "]"

    def TreeToString(self, indent):
        s = self.IndentString(indent) + str(self)
        for c in self.childNodes:
            s += c.TreeToString(indent + 1)
        return s

    def IndentString(self, indent):
        s = "\n"
        for i in range(1, indent + 1):
            s += "| "
        return s

    def ChildrenToString(self):
        s = ""
        for c in self.childNodes:
            s += str(c) + "\n"
        return s


def UCT(rootstate, timemax, timestamp, verbose=False):
    """ Conduct a UCT search for itermax iterations starting from rootstate.
        Return the best move from the rootstate.
        Assumes 2 alternating players (player 1 starts), with game results in the range [0.0, 1.0]."""

    rootnode = Node(state=rootstate)

    def search():
        while (time.time() - timestamp <= timemax):
            # Clone
            node = rootnode
            state = rootstate.Clone()

            # Select
            while node.untriedMoves == [] and node.childNodes != []:  # node is fully expanded and non-terminal
                node = node.UCTSelectChild()
                state.DoMove(node.move)

            # Expand
            if node.untriedMoves != []:  # if we can expand (i.e. state/node is non-terminal)
                try:
                    m = random.choice(node.untriedMoves)
                except:
                    break
                state.DoMove(m)
                node = node.AddChild(m, state)  # add child and descend tree

            # Rollout - this can often be made orders of magnitude quicker using a state.GetRandomMove() function
            while state.GetMoves() != []:  # while state is non-terminal
                state.DoMove(random.choice(state.GetMoves()))

            # Backpropagate
            while node != None:  # backpropagate from the expanded node and work back to the root node
                node.Update(state.GetResult()[1])  # state is terminal. Update node with result
                node = node.parentNode

    search()

    # 试图进行多线程 依旧在尝试中 目前还没有成功

    # t1 = multiprocessing.Process(target=search, name="Tree_Search_Thread1")
    # t2 = multiprocessing.Process(target=search, name="Tree_Search_Thread2")
    # t3 = multiprocessing.Process(target=search, name="Tree_Search_Thread3")
    # t4 = multiprocessing.Process(target=search, name="Tree_Search_Thread4")
    # t5 = multiprocessing.Process(target=search, name="Tree_Search_Thread5")

    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()

    # Output some information about the tree - can be omitted
    if (verbose):
        print(rootnode.TreeToString(0))
    else:
        pass
        # print(rootnode.ChildrenToString())

    return sorted(rootnode.childNodes, key=lambda c: c.visits)[-1].move  # return the move that was most visited


def UCTPlayGame():
    """ Play a sample game between two UCT players where each player gets a different number
        of UCT iterations (= simulations = tree nodes).
    """
    state = UtopiaState()
    while (state.GetMoves() != []):
        print(str(state))
        m = UCT(rootstate=state, timemax=0.1, timestamp=time.time(),
                verbose=False)  # play with values for itermax and verbose = True
        print("Best Move: " + str(m) + "\n")
        state.DoMove(m)
    print(str(state))
    result = state.GetResult()
    print(result)
    return result[0]


def test():
    """ To run multiple times of the game.
    """
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
        result = UCTPlayGame()
        if result == excellent_edge:
            perfect += 1
        elif excellent_edge < result <= great_edge:
            great += 1
        elif great_edge < result <= good_edge:
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
