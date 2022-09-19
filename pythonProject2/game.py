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
        self.computer = player.AIPlayer('电脑')
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
        self.chess_board.show_board(True)
        #决定先手玩家
        current_player,next_player = self.radom_player()

        while True:
            #下子方落子
            current_player.move(self.chess_board)
            #显示棋盘
            self.chess_board.show_board()
            #判断是否胜利
            if self.chess_board.is_win(current_player.chess):
                current_player.score +=1
                print('%s 战胜了 %s' %(current_player,next_player))
                break
            #是否和局
            if self.chess_board.is_dogfall():
                break
            #交换落子坊
            current_player,next_player = next_player,current_player
        #显示比分
        print('[%s]对战[%s]比分是：%d:%d' %(current_player,
                                          next_player,
                                          current_player.score,
                                          next_player.score))
    def start(self):
        '''开启有戏，能够循环对局'''
        #开始游戏
        while True:
            self.play_around()
            #让用户选择是否再来一局
            is_continue = input('是否再来一盘（Y/N）：').upper()
            #判断是否退出游戏
            if is_continue != 'Y':
                break
            #重置棋盘数据
            self.chess_board.reset_board()
if __name__ == '__main__':
    #测试游戏初始化
    game = Game()
    # print(game.chess_board.moveble_list)
    # print(game.human.name)0
    # print(game.computer.name)
    # print(game.radom_player()[0].name)
    #测试游戏
    # game.play_around()
    game.start()