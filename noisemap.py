from tkinter import *
from math import *
import random
import time

root=Tk()
C=Canvas(root,bg="#ffffff",width=1400,height=750)
C.pack()

def connect(a,b):
    x1=C.coords(a)[0]
    x2=C.coords(b)[0]
    y1=C.coords(a)[1]
    y2=C.coords(b)[1]
    C.create_line(x2,y2,x1,y1,tag="draft")

def random_graytone(base):
    r=random.randint(-4,4)
    #return("#%02x%02x%02x"%(eval("0x"+base[1:3])+r,eval("0x"+base[3:5])+r,eval("0x"+base[5:7])+r))
    return("#%02x%02x%02x"%(eval("0x"+base[1:3])+random.randint(-3,3),eval("0x"+base[3:5])+random.randint(-3,3),eval("0x"+base[5:7])+random.randint(-3,3)))

def random_graytone_ex(base):
    r=random.randint(-14,14)
    return("#%02x%02x%02x"%(eval("0x"+base[1:3])+r,eval("0x"+base[3:5])+r,eval("0x"+base[5:7])+r))
    return("#%02x%02x%02x"%(eval("0x"+base[1:3])+random.randint(-3,3),eval("0x"+base[3:5])+random.randint(-3,3),eval("0x"+base[5:7])+random.randint(-3,3)))

def color_average(c):
    try:
        s=0
        for i in c:
            s+=eval("0x"+i[1:3])
        return("#%02x%02x%02x"%(round(s/len(c)),round(s/len(c)),round(s/len(c))))
    except:
        return "#000000"

def perlin_noisemap(width,start):
    d={}
    l=[]
    for i in range(width):
        for j in range(int(width/(140/75))):
            l=[]
            for k in range(3):
                for o in range(3):
                    if width*(i+(k-1))+(j+(o-1))in d:
                        l.append(width*(i+(k-1))+(j+(o-1)))
            if l:
                c=[]
                for k in l:
                    c.append(d[k]["color"])
                d[width*i+j]={"coords":[i,j],"color":random_graytone(color_average(c))}
                C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill=d[width*i+j]["color"],outline="")
            else:
                d[width*i+j]={"coords":[i,j],"color":start}
                C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill=d[width*i+j]["color"],outline="")
        C.update()

def spiral(num,n):
    m=[[0]*n for i in range(n)]
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    x,y,c=0,-1,1
    for i in range(n+n-1):
        for j in range((n+n-i)//2):
            x+=dx[i%4]
            y+=dy[i%4]
            m[x][y]=c
            c+=1
    for i in m:
        if num+1 in i:
            return [m.index(i),i.index(num+1)]

def idle_generation(width,start):
    for i in range(width):
        for j in range(int(width/(140/75))):
            C.create_rectangle(i*1400/width-(1400/(width*2)),j*1400/width-(1400/(width*2)),i*1400/width+(1400/(width*2)),j*1400/width+(1400/(width*2)),fill=start,outline="",tag="B"+str(i*1400+j))
    C.update()

def hightmap(width,start,layers):
    global d
    d={}
    for u in range(layers):
        for i in range(width):
            for j in range(int(width/(140/75))):
                l=[]
                for k in range(3):
                    for o in range(3):
                        if width*(i+(k-1))+(j+(o-1))in d:
                            l.append(width*(i+(k-1))+(j+(o-1)))
                if l:
                    c=[]
                    for k in l:
                        c.append(d[k]["color"])
                    d[width*i+j]={"coords":[i,j],"color":random_graytone(color_average(c))}
                    eval_terrain(d,i,j,width,start)
                    #eval_isomere(d,i,j,width,start)
                else:
                    d[width*i+j]={"coords":[i,j],"color":start}
                    eval_terrain(d,i,j,width,start)
                    #eval_isomere(d,i,j,width,start)
            C.update()

def qew(i,j,h,w):
    return i

def qew2(i,j,h,w):
    return j

def hightmap2(width,start,layers):
    global d
    d={}
    for u in range(layers):
        for i in range(width):
            if i%2:
                for j in range(int(width/(140/75))):
                    q=qew(i,j,int(width/(140/75)),width)
                    if j%2:
                        b=qew2(i,j,int(width/(140/75)),width)
                        l=[]
                        for k in range(3):
                            for o in range(3):
                                if width*((width//2-q//2)+(k-1))+((int(width/(140/75))//2-b//2)+(o-1))in d:
                                    l.append(width*((width//2-q//2)+(k-1))+((int(width/(140/75))//2-b//2)+(o-1)))
                        if l:
                            try:
                                c=[]
                                for k in l:
                                    c.append(d[k]["color"])
                                d[width*(width//2-q//2)+(int(width/(140/75))//2-b//2)]={"coords":[(width//2-q//2),(int(width/(140/75))//2-b//2)],"color":random_graytone(color_average(c))}
                                eval_terrain(d,(width//2-q//2),(int(width/(140/75))//2-b//2),width,start)
                            except Exception as a:
                                print(a)
                        else:
                            d[width*(width//2-q//2)+(int(width/(140/75))//2-b//2)]={"coords":[(width//2-q//2),(int(width/(140/75))//2-b//2)],"color":start}
                            eval_terrain(d,(width//2-q//2),(int(width/(140/75))//2-b//2),width,start)
                    else:
                        b=qew2(i,j,int(width/(140/75)),width)
                        l=[]
                        for k in range(3):
                            for o in range(3):
                                if width*((width//2-q//2)+(k-1))+((int(width/(140/75))//2+b//2)+(o-1))in d:
                                    l.append(width*((width//2-q//2)+(k-1))+((int(width/(140/75))//2+b//2)+(o-1)))
                        if l:
                            try:
                                c=[]
                                for k in l:
                                    c.append(d[k]["color"])
                                d[width*(width//2-q//2)+(int(width/(140/75))//2+b//2)]={"coords":[(width//2-q//2),(int(width/(140/75))//2+b//2)],"color":random_graytone(color_average(c))}
                                eval_terrain(d,(width//2-q//2),(int(width/(140/75))//2+b//2),width,start)
                            except Exception as a:
                                print(a)
                        else:
                            d[width*(width//2-q//2)+(int(width/(140/75))//2+b//2)]={"coords":[(width//2-q//2),(int(width/(140/75))//2+b//2)],"color":start}
                            eval_terrain(d,(width//2-q//2),(int(width/(140/75))//2+b//2),width,start)
                C.update()
            else:
                for j in range(int(width/(140/75))):
                    q=qew(i,j,int(width/(140/75)),width)
                    if j%2:
                        b=qew2(i,j,int(width/(140/75)),width)
                        l=[]
                        for k in range(3):
                            for o in range(3):
                                if width*((width//2+q//2)+(k-1))+((int(width/(140/75))//2-b//2)+(o-1))in d:
                                    l.append(width*((width//2+q//2)+(k-1))+((int(width/(140/75))//2-b//2)+(o-1)))
                        if l:
                            c=[]
                            for k in l:
                                c.append(d[k]["color"])
                            d[width*(width//2+q//2)+(int(width/(140/75))//2-b//2)]={"coords":[(width//2+q//2),(int(width/(140/75))//2-b//2)],"color":random_graytone(color_average(c))}
                            eval_terrain(d,(width//2+q//2),(int(width/(140/75))//2-b//2),width,start)
                        else:
                            d[width*(width//2+q//2)+(int(width/(140/75))//2-b//2)]={"coords":[(width//2+q//2),(int(width/(140/75))//2-b//2)],"color":start}
                            eval_terrain(d,(width//2+q//2),(int(width/(140/75))//2-b//2),width,start)
                    else:
                        b=qew2(i,j,int(width/(140/75)),width)
                        l=[]
                        for k in range(3):
                            for o in range(3):
                                if width*((width//2+q//2)+(k-1))+((int(width/(140/75))//2+b//2)+(o-1))in d:
                                    l.append(width*((width//2+q//2)+(k-1))+((int(width/(140/75))//2+b//2)+(o-1)))
                        if l:
                            c=[]
                            for k in l:
                                c.append(d[k]["color"])
                            d[width*(width//2+q//2)+(int(width/(140/75))//2+b//2)]={"coords":[(width//2+q//2),(int(width/(140/75))//2+b//2)],"color":random_graytone(color_average(c))}
                            eval_terrain(d,(width//2+q//2),(int(width/(140/75))//2+b//2),width,start)
                        else:
                            d[width*(width//2+q//2)+(int(width/(140/75))//2+b//2)]={"coords":[(width//2+q//2),(int(width/(140/75))//2+b//2)],"color":start}
                            eval_terrain(d,(width//2+q//2),(int(width/(140/75))//2+b//2),width,start)

                C.update()

def spiral_hightmap(width,start,layers):
    global d
    d={}
    for u in range(layers):
        for i2 in range(int(width/(140/75))):
            for j2 in range(int(width/(140/75))):
                i,j=spiral(i2*int(width/(140/75))+j2,int(width/(140/75)))
                l=[]
                for k in range(3):
                    for o in range(3):
                        if int(width/(140/75))*(i+(k-1))+(j+(o-1))in d:
                            l.append(int(width/(140/75))*(i+(k-1))+(j+(o-1)))
                if l:
                    c=[]
                    for k in l:
                        c.append(d[k]["color"])
                    d[width*i+j]={"coords":[i,j],"color":random_graytone(color_average(c))}
                    eval_terrain(d,i,j,width,start)
                else:
                    d[width*i+j]={"coords":[i,j],"color":start}
                    eval_terrain(d,i,j,width,start)
                C.update()

def eval_terrain(d,i,j,width,start):
    color=d[width*i+j]["color"]
    if f(color)>f(start):
        if f(color)-f(start)<20/2:
            C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#c2b280",outline="")
        elif f(color)-f(start)<110/6:
            C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#7cbc00",outline="")
        elif f(color)-f(start)<200/6:
            C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#228b22",outline="")
        elif f(color)-f(start)<220/5:
            C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#808487",outline="")
        else:
            C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#fffafa",outline="")
    else:
        if f(color)-f(start)>-5:
            C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#0087c1",outline="")
        elif f(color)-f(start)>-30:
            C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#0077be",outline="")
        else:
            C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#00579e",outline="")            

def eval_terrain2(d,i,j,width,start):
    color=d[width*i+j]["color"]
    if f(color)>f(start):
        if f(color)-f(start)<20/2:
            C.itemconfig("B"+str(width*i+j),fill="#c2b280")
        elif f(color)-f(start)<110/6:
            C.itemconfig("B"+str(width*i+j),fill="#7cbc00")
        elif f(color)-f(start)<200/6:
            C.itemconfig("B"+str(width*i+j),fill="#228b22")
        elif f(color)-f(start)<220/5:
            C.itemconfig("B"+str(width*i+j),fill="#808487")
        else:
            C.itemconfig("B"+str(width*i+j),fill="#fffafa")
    else:
        if f(color)-f(start)>-5:
            C.itemconfig("B"+str(width*i+j),fill="#0087c1")
        elif f(color)-f(start)>-30:
            C.itemconfig("B"+str(width*i+j),fill="#0077be")
        else:
            C.itemconfig("B"+str(width*i+j),fill="#00579e")

def eval_isomere(d,i,j,width,start):
    color=d[width*i+j]["color"]
    if f(color)%60<10:
        C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#880000",outline="")
    else:
        C.create_rectangle(d[width*i+j]["coords"][0]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width-(1400/(width*2)),d[width*i+j]["coords"][0]*1400/width+(1400/(width*2)),d[width*i+j]["coords"][1]*1400/width+(1400/(width*2)),fill="#444444",outline="")

def f(x):
    try:
        return eval("0x"+x[1:3])
    except:
        return 0

idle_generation(200,"#444444")
#perlin_noisemap(700,"#888888")
hightmap(500,"#444444",1)
s=0
for i in d:
    s+=1
print(s)

root.mainloop()
