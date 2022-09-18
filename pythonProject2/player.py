# coding:utf-8
'''玩家主模块'''
import board
class Player(object):
    def __init__(self,name):
        #初始化玩家信息
        self.name = name
        self.score = 0
        self.chess = None
    def move(self,board):
        '''玩家落一个子到棋盘上'''
        index = int(input("请 %s 输入落子位置 %s :" % (self.name, board.moveble_list)))
        board.move_down(index,self.chess)
# if __name__ == '__main__':
#     player1 = Player("玩家1")
#     player1.chess = 'X'
    # print(player1.name)
    # print(player1.score)
    # print(player1.chess)

    #测试玩家落子功能
    # board = board.Board()
    # player1.move(board)
    # board.show_board()