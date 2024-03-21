# 导入turtle
import turtle
# 导入外部写的关卡模块
import level

# 创建窗口
ms = turtle.Screen()
# 设置初始尺寸
ms.setup(900, 650, 200, 0)

# 标题
ms.title('推箱子小游戏')

# 注册图片
# 背景图片
ms.register_shape('bc1.gif')
ms.register_shape('bc2.gif')
ms.register_shape('bc3.gif')
ms.register_shape('bc4.gif')
ms.register_shape('bc5.gif')

ms.register_shape('wall.gif')
ms.register_shape('o.gif')          # 正确箱子位置标识图片
ms.register_shape('p.gif')          # 小人
ms.register_shape('box.gif')        # 箱子
ms.register_shape('boxc.gif')       # 推到正确位置，箱子变色

# 默认背景图片1
ms.bgpic('bc1.gif')

ms.tracer(0)        #追踪 屏幕刷新

# 调用地图列表信息
levels = level.level_list()


# ------------------------------------------------------------------------画笔Pen（箱子移动）
#里面使用了move函数、show_win函数
class Pen(turtle.Turtle):   #继承海龟模块中的海龟类
    #每定义一个类就做属性的初始化
    def __init__(self, pic):
        super().__init__()
        self.shape(pic)     #形状
        self.penup()        #抬笔

    # 让人物和箱子移动
    def move(self, x, y, px, py):
        gox, goy = x+px, y+py
        # 人物
        if (gox, goy) in go_space:
            self.goto(gox, goy)
        #箱子 人
        if (gox+px, goy+py) in go_space and (gox, goy) in box_space:
            # 找到箱子开始推
            for i in box_list:
                if i.pos() == (gox, goy):               #前面有箱子:人要去的地方和设定箱子的位置一样
                    # 更新人物
                    go_space.append(i.pos())
                    # 移除海龟
                    box_space.remove(i.pos())

                    i.goto(gox+px, goy+py)              #移动箱子
                    self.goto(gox, goy)                 #人物移动

                    # 到新地方：移除人物
                    go_space.remove(i.pos())
                    # 更新箱子位置信息
                    box_space.append(i.pos())

                    # 判断箱子是否到达正确的位置
                    if i.pos() in correct_box_space:    # 正确箱子的位置
                        # 更新箱子的样式
                        i.shape('boxc.gif')
                    else:
                        # 不变
                        i.shape('box.gif')

                    # 判断推的箱子是否全部达到指定位置
                    if set(box_space) == set(correct_box_space):    #列表变成集合
                        text.show_win()                             #提示游戏赢了

                    

    # 定义移动：调用move（）方法
    def go_up(self):            #上
        self.move(self.xcor(), self.ycor(), 0, 50)
    def go_down(self):          #下
        self.move(self.xcor(), self.ycor(), 0, -50)
    def go_left(self):          #左
        self.move(self.xcor(), self.ycor(), -50, 0)
    def go_right(self):         #右
        self.move(self.xcor(), self.ycor(), 50, 0)
# ------------------------------------------------------------------------画笔Pen

# ------------------------------------------------------------------------开始画游戏Game
#里面使用了Pen函数
class Game():
    def paint(self):    #定义一个画的方法
        #地图是几行几列的（随便那行列都可以取出来）
        i_date = len(levels[num-1])         #行
        j_date = len(levels[num-1][0])      #列

        # 行
        for i in range(i_date):
            # 列
            for j in range(j_date):
                # 根据左上角坐标遍历
                x = -j_date*25+25+j*50 + sister_x
                y = i_date*25-25-i*50
                # O代表：箱子应该去的正确位置
                if levels[num-1][i][j] == 'O':
                    correct_box.goto(x, y)
                    correct_box.stamp()         #设置正确箱子的位置不需要移动，盖个章
                    go_space.append((x, y))
                    correct_box_space.append((x, y))
        for i in range(i_date):
            for j in range(j_date):
                #开始画的位置
                # 关卡：屏幕正中心为原点   8行8列的关卡每个方块大小是50    左上角坐标中心位置（-175，175）
                x = -j_date*25+25+j*50 + sister_x       #-175+j*50      x增加
                y = i_date*25-25-i*50                   #175-i*50       y减少

                # 空白：代表空白
                if levels[num-1][i][j] == ' ':
                    go_space.append((x, y))
                # X代表：墙的位置
                if levels[num-1][i][j] == 'X':
                    wall.goto(x, y)
                    # 墙不需要移动，盖个章
                    wall.stamp()
                # P代表：玩家所在的位置
                if levels[num-1][i][j] == 'P':
                    player.goto(x, y)
                    go_space.append((x, y))
                # B代表：现在箱子的位置
                if levels[num-1][i][j] == 'B':
                    box = Pen('box.gif')            #画箱子
                    box.goto(x, y)
                    box_list.append(box)
                    box_space.append((x, y))
# ------------------------------------------------------------------------开始画游戏Game

# ------------------------------------------------------------------------游戏提示信息ShowMessage
#含有 message函数 show_win函数
class ShowMessage(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor('blue')
        self.ht()       #隐藏海龟鼠标

    # 显示信息：第几关、重新开始、选择关卡
    def message(self):
        self.goto(0+sister_x, 290)
        self.write(f'第{num}关', align='center', font=('仿宋', 20, 'bold'))
        self.goto(0+sister_x, 270)
        self.write('重新开始本关请按回车键', align='center', font=('仿宋', 15, 'bold'))
        self.goto(0+sister_x, 250)
        self.write('选择关卡请按Q', align='center', font=('仿宋', 15, 'bold'))

    #提示游戏赢了
    def show_win(self):
        global num  #全局变量
        if num == len(levels):  #走到了最后一关
            num = 1
            self.goto(0, 0)
            self.write('你已全部过关', align='center', font=('黑体', 30, 'bold'))
            self.goto(0, -50)
            self.write('返回第一关轻按空格键', align='center', font=('黑体', 30, 'bold'))
        else:                   #继续自动进入下一关
            num = num+1
            self.goto(0, 0)
            self.write('恭喜过关', align='center', font=('黑体', 30, 'bold'))
            self.goto(0, -50)
            self.write('进入下一关请按空格键', align='center', font=('黑体', 30, 'bold'))
# ------------------------------------------------------------------------游戏提示信息ShowMessage

# ------------------------------------------------------------------------初始化init
#里面使用了message()
def init():
    # 清除文字的显示
    text.clear()
    # 清除墙
    wall.clear()
    # 清除正确位置的箱子
    correct_box.clear()
    # 清除箱子
    for i in box_list:
        i.ht()      #隐藏海龟
        del(i)      #删除海龟
    box_list.clear()
    # 清除箱子所在位置的坐标列表
    box_space.clear()
    # 清除人的列表
    go_space.clear()
    # 清除正确的箱子列表
    correct_box_space.clear()

    # 重新画
    game.paint()
    # 显示信息
    text.message()

    #每次切换不同的图片
    ms.bgpic(f'bc{num}.gif')
# ------------------------------------------------------------------------初始化init

# ------------------------------------------------------------------------键盘输入选择关卡choose
#里面使用了init函数
def choose():
    global num
    a = ms.numinput('选择关卡', '你的选择（请输入1-5）', 1)
    if a is None:
        a = num
    num = int(a)    #确定输入的关卡
    init()          #初始化
    ms.listen()     #屏幕监听
# ------------------------------------------------------------------------键盘输入选择关卡choose


# -----------------------------主程序-------------------------------------------#
sister_x = 225              #游戏地图显示的位置右移距离，给左边照片让出位置
num = 1                     #默认从第1关开始
correct_box_space = []      #正确的箱子列表（正确箱子位置标识图片）
box_list = []               #设置有箱子海龟的列表
box_space = []              #箱子移动所在位置的坐标列表
go_space = []               #人的列表

# 继承创建对象：使用Pen（）函数
wall = Pen('wall.gif')          # 画墙
correct_box = Pen('o.gif')      # 画箱子应该去的正确位置：O代表
player = Pen('p.gif')           # 画：玩家所在的位置P代表

#开始画游戏：使用Game()函数
game = Game()
game.paint()

#提示信息
text = ShowMessage()        # 创建对象
text.message()              # 调用message() 方法

#屏幕的监听  screen.onkey(函数,‘需要监听的键’)
ms.listen()
ms.onkey(player.go_up, 'Up')                #上
ms.onkey(player.go_down, 'Down')            #下
ms.onkey(player.go_left, 'Left')            #左
ms.onkey(player.go_right, 'Right')          #右
ms.onkey(init, 'Return')                    #回车 开始当前
ms.onkey(init, 'space')                     #空格 开始下一关
ms.onkey(choose, 'Q')                       #Q键退出

#每次追踪刷新之后，对屏幕进行更新
while True:
    ms.update()

# 主循环,持续加载
ms.mainloop()
# -----------------------------主程序-------------------------------------------#