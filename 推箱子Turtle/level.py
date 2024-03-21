# 关卡：屏幕正中心为原点

    # C代表：关卡的外部
    # X代表：墙的位置
    # O代表：箱子应该去的正确位置
    # B代表：现在箱子的位置
    # P代表：玩家所在的位置
    # 空白：代表空白

# 8行8列的关卡：每个方块大小是50
#     左上角坐标中心位置（-175，175）
def level_list():       #数列从0开show_win始存储信息的
    level_1 = [
        'CCXXXCCC',
        'CCXOXCCC',
        'CCX XXXX',
        'XXXB BOX',
        'XO BPXXX',
        'XXXXBXCC',
        'CCCXOXCC',
        'CCCXXXCC']
    level_2 = [
        'CXXXXCCC',
        'CX OXXXX',
        'XXO    X',
        'XOO XX X',
        'X B  B X',
        'XX BBXXX',
        'CXP  XCC',
        'CXXXXXCC']
    level_3 = [
        'CCXXXXXXCC',
        'CCX    XXX',
        'CCX B    X',
        'XXX B XX X',
        'XOOO B   X',
        'XOOOBXB XX',
        'XXXX X B X',
        'CCCX  P  X',
        'CCCXXXXXXX']
    level_4 = [
        'CCCXXXXXX',
        'XXXXO  PX',
        'X  BBB  X',
        'XOXXOXXOX',
        'X   B   X',
        'X  BOX XX',
        'XXXX   XC',
        'CCCXXXXXC']
    level_5 = [
        'CXXXXXXXC',
        'XX     XX',
        'X  BOB  X',
        'X BXOXB X',
        'XXOOPOO X',
        'X BXOXB X',
        'X  BOB  X',
        'X   X  XX',
        'XXXXXXXXC']

    # 关卡集合
    levels = []
    # 把关卡加入集合
    levels.append(level_1)
    levels.append(level_2)
    levels.append(level_3)
    levels.append(level_4)
    levels.append(level_5)

    # 返回列表
    return(levels)
