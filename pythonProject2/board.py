# coding:utf-8
'''棋盘模块
棋盘每一行三个元素可有o、x、  、三类填入。
'''
#显示棋盘提示信息。
#初始化模块
class Board(object):  #定义类
    def __init__(self): #初始化数据固定不需自己传
        self.board_data = [' ']*9 #记录每个位置棋子  [' ']*9  -->[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.moveble_list = list(range(9))  #剩余可放棋子的位子 。。生成可移动列表、、list(range(9)) ---> [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def show_board(self,is_show_index=False): #默认为false打印棋盘
        '''显示棋盘,如果is_show_index为true打印索引，为false打印棋子位子'''
        for i in (0,3,6):
            print('       |       |       ')
            if is_show_index:
                print('   %d   |   %d   |   %d   ' % (i, i + 1, i + 2))
            else:
                print(
                    '   %s   |   %s   |   %s   ' % (self.board_data[i], self.board_data[i + 1], self.board_data[i + 2]))

            print('       |       |       ')
            if i!=6:
                print('-'*23)
    def move_down(self,index,chess):
    #落下一颗棋子
    #检查下标是否在可落子的范围里
        if index not in self.moveble_list:
            print('%d 不能落子'%index)
            return
    #落子
        self.board_data[index] = chess
    #将下标移除
        self.moveble_list.remove(index)
if __name__ == '__main__': #测试模块初始化
    # #棋盘测试
     board=Board()#创建棋盘对象
    # #print(board.board_data)
    # #print(board.moveble_list)
    # #测试打印棋盘
    # board.show_board(True)
    # print('测试落子')
    # board.board_data[1] = 'X'
    # board.board_data[3] = '3'
    # board.show_board(False)
board.move_down(1,'X')
print(board,board.board_data)
print(board.moveble_list)
board.show_board()
