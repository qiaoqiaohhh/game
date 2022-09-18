# coding:utf-8
'''游戏魔块'''
import board
import player
import random
class Game(object):
    def __init__(self):
        '''初始化游戏数据'''
        self.chess_board = board.Board()
        self.human = player.Player('玩家')
        self.computer = player.Player('电脑')
    def radom_player(self):
        '''随机确定玩家先后手顺序'''
        if random.randint(0,1) == 1: #随机生成一个0或者1的整数
            player = (self.human,self.computer)
        else:
            player = (self.computer,self.human)

        player[0].chess = 'X'
        player[1].chess = 'O'

        print('根据随机结果 %s 先行'% player[0].name)
        return player
    def play_around(self):
        '''一局游戏'''
        #显示棋盘
        #决定先手玩家
        while True:
            #下子方落子
            #显示棋盘
            #判断是否胜利
            #是否和局
            #交换落子坊
            pass
    #显示比分
if __name__ == '__main__':
    #测试游戏初始化
    game = Game()
    # print(game.chess_board.moveble_list)
    # print(game.human.name)
    # print(game.computer.name)
    print(game.radom_player()[0].name)