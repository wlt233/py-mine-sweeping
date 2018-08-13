### project 扫雷
import random
import math
import sys

#生成地图
x,y=10,10
maps=[]
total=15
fl=['!']*(x+2)
maps.append(fl)
for ytimes in range(0,y):
    xlist=['!']
    for xtimes in range(0,x):
        xlist.append(' ')
    xlist.append('!')
    maps.append(xlist)
maps.append(fl)

#布雷
for createbomb in range(0,total):
    radx=random.randint(0,x-1)+1
    rady=random.randint(0,y-1)+1
    maps[rady][radx]='@'

#初始化覆盖层
layer=[]
layer.append(fl)
for yly in range(0,y):
    ytp=['#']*(x+2)
    layer.append(ytp)  
layer.append(fl)

#定义计算周围雷数函数
def cb(cbx,cby):
    bomb=[]
    bomb.append(maps[cby-1][cbx-1])
    bomb.append(maps[cby-1][cbx])
    bomb.append(maps[cby-1][cbx+1])
    bomb.append(maps[cby][cbx-1])
    bomb.append(maps[cby][cbx+1])
    bomb.append(maps[cby+1][cbx-1])
    bomb.append(maps[cby+1][cbx])
    bomb.append(maps[cby+1][cbx+1])
    num=bomb.count('@')
    if num==0:
        maps[cby][cbx]=' '
    elif num!=0:
        maps[cby][cbx]=num

#定义判断周围空格函数
def css(csxx,csyy):
    if maps[csyy][csxx]==' 'and layer[csyy][csxx]=='#':
        cslx.append(csxx)
        csly.append(csyy)
    elif maps[csyy][csxx]!=(' ' and '@'):
        layer[csyy][csxx]=maps[csyy][csxx]
    
def cs(csx,csy):
    if maps[csy][csx]==' ' and layer[csy][csx]=='#' :
        css(csx-1,csy)
        css(csx+1,csy)
        css(csx,csy-1)
        css(csx,csy+1) 
        layer[csy][csx]=' '
    elif maps[csy][csx]!=' ':
        layer[csy][csx]=maps[csy][csx]
         
#定义输出函数
def pr(lists):
    print('  ',end='')
    for prxtp in range(0,x):
        print('',str(prxtp).zfill(2),end='')
    print('')
    for prtmy in range(0,y): 
        print(str(prtmy).zfill(2),end=' ')
        for prtmx in range(0,x):
            print(lists[prtmy+1][prtmx+1],end='  ')
        print('')

#定义计算未完成格数
def cu():
    cus,cul=0,[]
    for cuy in range(1,y+1):
        for cux in range(1,x+1):
            cul.append(layer[cuy][cux])
    cus=cul.count('#')
    print ('还剩%d个格子未完成'%cus)
    return cus
        
#处理地图
for chy in range(1,y+1):
    for chx in range(1,x+1):
        if maps[chy][chx]!='@':
            cb(chx,chy) 
        
#检查输出         
pr(maps)        
        
#主程序    
print('欢迎来到扫雷世界！\n本局共有',total,'个雷')
    #初始输出
pr(layer)

    
    #循环扫雷
while True:  
    selx=int(input('x?  '))+1
    sely=int(input('y?  '))+1

    #死亡判断
    if maps[sely][selx]=='@':
        print('You lose!')
        layer[sely][selx]='@'
        #死后提示
        pr(layer)
        sys.exit()    
    
    #处理周围空格
    cslx,csly=[],[]
    cs(selx,sely)    
    while len(cslx)!=0:
        cslxi,cslyi=cslx[0],csly[0]
        del cslx[0]
        del csly[0]
        cs(cslxi,cslyi)
    
    #胜利判断
    cus=cu()
    if cus==total:
        print('You win !')
        pr(maps)
        sys.exit() 
    
    #输出
    pr(layer)

