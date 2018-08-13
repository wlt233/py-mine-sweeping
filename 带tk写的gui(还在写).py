### project 扫雷
import random
import math
import sys
import re
from tkinter import *
from tkinter import messagebox

x,y=15,15
maps=[]
total=15
fl=['233']*(x+2)


#生成地图
maps.append(fl)
for ytimes in range(0,y):
    xlist=['233']
    for xtimes in range(0,x):
        xlist.append(' ')
    xlist.append('233')
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
cslx,csly=[],[]    
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
        
#主程序GUI
root=Tk()
root.title("hello world")
root.resizable(True,True)
    #标题
Label(text='扫雷',bg='orange').grid(row=0,column=0,in_=root,sticky=E+W)
    #bitmap data
BITMAP_face=""" 
#define im_width 48
#define im_height 48 
static char im_bits[] = { 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0xFE, 0x7F, 0x00, 0x00, 0x00, 0x00, 0x0F, 0xF0, 0x00, 0x00, 
  0x00, 0xC0, 0x01, 0x80, 0x03, 0x00, 0x00, 0x30, 0x00, 0x00, 0x0C, 0x00, 
  0x00, 0x1C, 0x00, 0x00, 0x1C, 0x00, 0x00, 0x0C, 0x00, 0x00, 0x30, 0x00, 
  0x00, 0x03, 0x00, 0x00, 0xE0, 0x00, 0x00, 0x03, 0x00, 0x00, 0xC0, 0x00, 
  0x80, 0x01, 0x00, 0x00, 0x80, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x01, 
  0x40, 0x00, 0x00, 0x00, 0x00, 0x03, 0x40, 0x80, 0x03, 0x80, 0x03, 0x03, 
  0x60, 0xE0, 0x07, 0xE0, 0x07, 0x06, 0x30, 0xE0, 0x0F, 0xF0, 0x0F, 0x04, 
  0x30, 0xE0, 0x0F, 0xF0, 0x0F, 0x04, 0x30, 0xE0, 0x0F, 0xF0, 0x0F, 0x04, 
  0x10, 0xE0, 0x07, 0xE0, 0x07, 0x08, 0x10, 0xE0, 0x07, 0xE0, 0x07, 0x08, 
  0x10, 0x00, 0x00, 0x00, 0x00, 0x08, 0x10, 0x00, 0x00, 0x00, 0x00, 0x08, 
  0x10, 0x00, 0x00, 0x00, 0x00, 0x08, 0x10, 0x00, 0x00, 0x00, 0x00, 0x08, 
  0x10, 0x00, 0x00, 0x00, 0x00, 0x08, 0x10, 0x0C, 0x00, 0x00, 0x60, 0x08, 
  0x30, 0x0C, 0x00, 0x00, 0x30, 0x04, 0x30, 0x1C, 0x00, 0x00, 0x18, 0x04, 
  0x30, 0x18, 0x00, 0x00, 0x18, 0x04, 0x60, 0x70, 0x00, 0x00, 0x0E, 0x06, 
  0x40, 0x60, 0x00, 0x00, 0x07, 0x03, 0x40, 0xE0, 0x00, 0x80, 0x03, 0x03, 
  0x80, 0x81, 0x03, 0xC0, 0x80, 0x01, 0x80, 0x01, 0x0F, 0xF0, 0x80, 0x00, 
  0x00, 0x03, 0x3F, 0x7C, 0xC0, 0x00, 0x00, 0x06, 0xE0, 0x07, 0x60, 0x00, 
  0x00, 0x0C, 0x00, 0x00, 0x30, 0x00, 0x00, 0x1C, 0x00, 0x00, 0x1C, 0x00, 
  0x00, 0xE0, 0x00, 0x00, 0x07, 0x00, 0x00, 0xC0, 0x01, 0x80, 0x03, 0x00, 
  0x00, 0x00, 0x0F, 0xF0, 0x00, 0x00, 0x00, 0x00, 0xF0, 0x0F, 0x00, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, };
""" 
bmp_face= BitmapImage(data=BITMAP_face) 

    #工具栏界面
f_tool=Frame(root)
Label(text='bomb',width=10).grid(row=0,column=0,in_=f_tool)
Button(image=bmp_face,foreground="white").grid(row=0,column=1,in_=f_tool)
Label(text='time',width=10).grid(row=0,column=2,in_=f_tool)
f_tool.grid(row=1,column=0,in_=root)



    #游戏界面
f_game=Frame(root)
gb=['']*(x*y+1)

#定义左键函数 
def lk(event):
    global steps
    wid=str(event.widget)
    gid=int(re.findall("\d+",wid)[0])-1
    yid=gid%y
    if yid==0:
        yid=y
    xid=int((gid-yid)/y)+1 
    print(gid,xid,yid,'left',maps[yid][xid])
    
    #处理周围空格
    cs(xid,yid)    
    while len(cslx)!=0:
        cslxi,cslyi=cslx[0],csly[0]
        del cslx[0]
        del csly[0]
        cs(cslxi,cslyi)
    
    #输出函数块
    for gi in range(0,x*y):
        gi=gi+1
        yi=gi%y
        if yi==0:
            yi=y
        xi=int((gi-yi)/y)+1
        gb[gi]['text']=layer[yi][xi]
    
    #失败判断
    if maps[yid][xid]=='@':
        if steps!=0:
            print('lose')
            messagebox.showerror(title='Ooooooops', message='You Lose!')
        elif steps==0:
            print('first lose')
            messagebox.showerror(title='Ooooooops', message='You Are An Africian!')
    
    steps=steps+1
    
#定义右键函数    
def rk(event):
    wid=str(event.widget)
    gid=int(re.findall("\d+",wid)[0])-1
    yid=gid%y
    xid=gid//y+1
    print(xid,yid,'right')
    
#第一次输出
steps=0
for gi in range(0,x*y):
    gi=gi+1
    yi=gi%y
    if yi==0:
        yi=y
    xi=int((gi-yi)/y)+1
    gb[gi]=Button(text=layer[yi][xi],width=3,height=1,relief=SUNKEN)
    gb[gi].bind("<Button-1>", lk)
    gb[gi].bind("<Button-3>", rk)
    gb[gi].grid(row=yi,column=xi,in_=f_game)
    
f_game.grid(row=2,column=0,in_=root)


root.mainloop()

