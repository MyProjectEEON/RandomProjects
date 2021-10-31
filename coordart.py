import tkinter
import random
import time

root=tkinter.Tk()
C=tkinter.Canvas(root,bg="#000000",width=22*91,height=22*91)
C.pack()
lt=[[-9,9],[9,9],[9,-9],[-9,-9],[-9,6],[6,6],[6,-6],[-6,-6],[-6,3],[3,3],[3,-3],[-3,-3],[-3,0],[0,0]]
dt={}
for i in lt:
    dt[lt.index(i)]=i
def create_ranged(x,y):
    C.create_oval(x-7,y-7,x+7,y+7,outline="#ffffff")
    C.create_line(x-8,y,x-3,y,fill="#ffffff")
    C.create_line(x+8,y,x+3,y,fill="#ffffff")
    C.create_line(x,y-3,x,y-8,fill="#ffffff")
    C.create_line(x,y+3,x,y+8,fill="#ffffff")
def create_mortar(x,y):
    C.create_line(x-5,y+7,x+5,y+7)
    C.create_line(x+5,y+7,x+8,y-2,fill="#ffffff")
    C.create_line(x+8,y-2,x+5,y+2,fill="#ffffff")
    C.create_line(x+5,y+2,x+4,y-7,fill="#ffffff")
    C.create_line(x+4,y-7,x+1,y+1,fill="#ffffff")
    C.create_line(x+1,y+1,x-1,y-8,fill="#ffffff")
    C.create_line(x-1,y-8,x-3,y+1,fill="#ffffff")
    C.create_line(x-3,y+1,x-6,y-4,fill="#ffffff")
    C.create_line(x-6,y-4,x-5,y+7,fill="#ffffff")
def create_bubble(x,y):
    C.create_oval(x-8,y-8,x+8,y+8,outline="#ffffff")
    C.create_oval(x-6,y-6,x+6,y+6,outline="#ffffff")
    C.create_oval(x-5,y-5,x+7,y+7,fill="#000000",outline="#ffffff")
def create_melee(x,y):
    C.create_line(x-9,y+7,x-7,y+9,fill="#ffffff")
    C.create_line(x-3,y+5,x-7,y+9,fill="#ffffff")
    C.create_line(x-3,y+5,x,y+7,fill="#ffffff")
    C.create_line(x+2,y+5,x,y+7,fill="#ffffff")
    C.create_line(x+2,y+5,x-1,y+3,fill="#ffffff")
    C.create_line(x-1,y+3,x+9,y-7,fill="#ffffff")
    C.create_line(x+9,y-7,x+9,y-9,fill="#ffffff")
    C.create_line(x+9,y-9,x+7,y-9,fill="#ffffff")
    C.create_line(x-3,y+1,x+7,y-9,fill="#ffffff")
    C.create_line(x-5,y-2,x-3,y+1,fill="#ffffff")
    C.create_line(x-5,y-2,x-7,y,fill="#ffffff")
    C.create_line(x-5,y+3,x-9,y+7,fill="#ffffff")
    C.create_line(x-5,y+3,x-7,y,fill="#ffffff")
def create_minion(x,y):
    C.create_oval(x-9,y+9,x+1,y-1,outline="#ffffff")
    C.create_oval(x+2,y-2,x+8,y-8,outline="#ffffff")
def create_stream(x,y):
    C.create_line(x-3,y-9,x-3,y+9,fill="#ffffff")
    C.create_line(x+3,y-9,x+3,y+9,fill="#ffffff")
    C.create_line(x-1,y-10,x-1,y+10,fill="#ffffff")
    C.create_line(x+1,y-10,x+1,y+10,fill="#ffffff")
def create_whip(x,y):
    C.create_oval(x-5,y,x+5,y+9,outline="#ffffff")
    C.create_oval(x-5,y,x+5,y-9,outline="#ffffff")
    C.create_rectangle(x-9,y,x-1,y+8,fill="#000000",outline="#ffffff")
    C.create_rectangle(x+9,y,x+1,y-7,fill="#000000",outline="#ffffff")
def create_shockwave(x,y):
    C.create_oval(x-8,y-8,x+8,y+8,outline="#ffffff")
    C.create_oval(x-5,y-5,x+5,y+5,outline="#ffffff")
    C.create_oval(x-2,y-2,x+2,y+2,outline="#ffffff")
def create_dash(x,y):
    C.create_line(x-6,y+7,x-6,y+7-4,fill="#ffffff")
    C.create_line(x,y+7-8,x-6,y+7-4,fill="#ffffff")
    C.create_line(x,y+7-8,x+6,y+7-4,fill="#ffffff")
    C.create_line(x+6,y+7,x+6,y+7-4,fill="#ffffff")
    C.create_line(x,y+7-4,x-6,y+7,fill="#ffffff")
    C.create_line(x,y+7-4,x+6,y+7,fill="#ffffff")
    C.create_line(x-6,y+7-7,x-6,y+7-7-4,fill="#ffffff")
    C.create_line(x,y+7-7-8,x-6,y+7-7-4,fill="#ffffff")
    C.create_line(x,y+7-7-8,x+6,y+7-7-4,fill="#ffffff")
    C.create_line(x+6,y+7-7,x+6,y+7-7-4,fill="#ffffff")
    C.create_line(x,y+7-7-4,x-6,y+7-7,fill="#ffffff")
    C.create_line(x,y+7-7-4,x+6,y+7-7,fill="#ffffff")
def create_connector(x,y):
    C.create_polygon(x+2,y-5,x+5,y-2,x-2,y+5,x-5,y+2,fill="#000000",outline="#ffffff")
    C.create_rectangle(x+2,y-2,x+8,y-8,fill="#000000",outline="#ffffff")
    C.create_rectangle(x-8,y+8,x-2,y+2,fill="#000000",outline="#ffffff")
def create_blockade(x,y):
    C.create_line(x,y,x,y+8,fill="#ffffff")
    C.create_line(x,y,x+7,y-3,fill="#ffffff")
    C.create_line(x,y,x-7,y-3,fill="#ffffff")
    C.create_line(x-7,y-3,x-7,y+5,fill="#ffffff")
    C.create_line(x+7,y-3,x+7,y+5,fill="#ffffff")
    C.create_line(x,y+8,x+7,y+5,fill="#ffffff")
    C.create_line(x,y+8,x-7,y+5,fill="#ffffff")
    C.create_line(x,y-6,x+7,y-3,fill="#ffffff")
    C.create_line(x,y-6,x-7,y-3,fill="#ffffff")
def create_teleport(x,y):
    global dt
    for i in dt:
        C.create_line(x+dt[i][0],y+dt[i][1],x+dt[i+1][0],y+dt[i+1][1],fill="#ffffff")
        if i==12:
            break
def create_invisible(x,y):
    C.create_oval(x-8,y-8,x+8,y+8,outline="#ffffff")
    C.create_polygon(x,y-10,x-1,y-4,x-9,y-9,x-4,y-1,x-10,y,x-4,y+1,x-9,y+9,x-1,y+4,x,y+10,x+1,y+4,x+9,y+9,x+4,y+1,x+10,y,x+4,y-1,x+9,y-9,x+1,y-4,x,y-10,fill="#000000",outline="#ffffff")
def create_invincible(x,y):
    C.create_line(x-7,y-7,x+7,y-7,fill="#ffffff")
    C.create_line(x-7,y-7,x-7,y-4,fill="#ffffff")
    C.create_line(x-7,y-4,x-6,y,fill="#ffffff")
    C.create_line(x-6,y,x-3,y+4,fill="#ffffff")
    C.create_line(x-3,y+4,x,y+7,fill="#ffffff")
    C.create_line(x+7,y-7,x+7,y-4,fill="#ffffff")
    C.create_line(x+7,y-4,x+6,y,fill="#ffffff")
    C.create_line(x+6,y,x+3,y+4,fill="#ffffff")
    C.create_line(x+3,y+4,x,y+7,fill="#ffffff")
def create_gravity(x,y):
    C.create_oval(x+1,y+1,x-1,y-1,outline="#ffffff")
    C.create_line(x+3,y,x+10,y,fill="#ffffff")
    C.create_line(x+3,y,x+6,y-3,fill="#ffffff")
    C.create_line(x+3,y,x+6,y+3,fill="#ffffff")
    C.create_line(x+6,y-3,x+6,y+3,fill="#ffffff")
    C.create_line(x-3,y,x-10,y,fill="#ffffff")
    C.create_line(x-3,y,x-6,y-3,fill="#ffffff")
    C.create_line(x-3,y,x-6,y+3,fill="#ffffff")
    C.create_line(x-+6,y-3,x-6,y+3,fill="#ffffff")
    C.create_line(x,y+3,x,y+10,fill="#ffffff")
    C.create_line(x,y+3,x-3,y+6,fill="#ffffff")
    C.create_line(x,y+3,x+3,y+6,fill="#ffffff")
    C.create_line(x-3,y+6,x+3,y+6,fill="#ffffff")
    C.create_line(x,y-3,x,y-10,fill="#ffffff")
    C.create_line(x,y-3,x-3,y-6,fill="#ffffff")
    C.create_line(x,y-3,x+3,y-6,fill="#ffffff")
    C.create_line(x-3,y-6,x+3,y-6,fill="#ffffff")
def create_time(x,y):
    C.create_polygon(x-5,y-3,x-8,y-6,x-6,y-8,x-3,y-5,fill="#000000",outline="#ffffff")
    C.create_polygon(x+5,y-3,x+8,y-6,x+6,y-8,x+3,y-5,fill="#000000",outline="#ffffff")
    C.create_oval(x+8,y+8,x-8,y-8,fill="#000000",outline="#ffffff")
    C.create_line(x,y+1,x-4,y-3,fill="#ffffff")
    C.create_line(x,y+1,x+1,y-7,fill="#ffffff")
    C.create_line(x-8,y,x-6,y,fill="#ffffff")
    C.create_line(x+8,y,x+6,y,fill="#ffffff")
    C.create_line(x,y-6,x,y-8,fill="#ffffff")
    C.create_line(x,y+6,x,y+8,fill="#ffffff")
def create_prison(x,y):
    C.create_rectangle(x+8,y+8,x-8,y-8,outline="#ffffff")
    C.create_line(x+5,y+8,x+5,y-8,fill="#ffffff")
    C.create_line(x+2,y+8,x+2,y-8,fill="#ffffff")
    C.create_line(x-2,y+8,x-2,y-8,fill="#ffffff")
    C.create_line(x-5,y+8,x-5,y-8,fill="#ffffff")
def create_turret(x,y):
    C.create_line(x+3,y+8,x+3,y-6,fill="#ffffff")
    C.create_line(x-3,y+8,x-3,y-6,fill="#ffffff")
    C.create_line(x-3,y+8,x+3,y+8,fill="#ffffff")
    C.create_line(x-6,y-5,x+6,y-5,fill="#ffffff")
    C.create_line(x-6,y-9,x-6,y-5,fill="#ffffff")
    C.create_line(x+2,y-9,x+2,y-7,fill="#ffffff")
    C.create_line(x-2,y-9,x-2,y-7,fill="#ffffff")
    C.create_line(x+6,y-9,x+6,y-5,fill="#ffffff")
    C.create_line(x+6,y-9,x+2,y-9,fill="#ffffff")
    C.create_line(x-6,y-9,x-2,y-9,fill="#ffffff")
    C.create_line(x+2,y-7,x-2,y-7,fill="#ffffff")
def create_fly(x,y):
    C.create_polygon(x-6,y-1,x,y-3,x+7,y-5,x+9,y-9,x+7,y-2,x+1,y+1,x+3,y,x+6,y+1,x+2,y+3,x+4,y+3,x+2,y+5,x+3,y+5,x,y+5,x-3,y+6,x-5,y+2,fill="#000000",outline="#ffffff")
def create_dodge(x,y):
    C.create_line(x-8,y-4,x+8,y-4,fill="#ffffff")
    C.create_line(x-8,y-4,x-4,y-1,fill="#ffffff")
    C.create_line(x-8,y-4,x-4,y-8,fill="#ffffff")
    C.create_line(x-4,y-1,x-4,y-8,fill="#ffffff")
    C.create_line(x+8,y+4,x-8,y+4,fill="#ffffff")
    C.create_line(x+8,y+4,x+4,y+1,fill="#ffffff")
    C.create_line(x+8,y+4,x+4,y+8,fill="#ffffff")
    C.create_line(x+4,y+1,x+4,y+8,fill="#ffffff")
def create_speed(x,y):
    C.create_polygon(x-3,y-9,x,y-9,x,y-4,x+3,y-6,x,y+7,x,y-1,x-3,y+1,fill="#000000",outline="#ffffff")
def create_health(x,y):
    C.create_polygon(x,y+8,x-8,y,x-9,y-2,x-8,y-5,x-6,y-6,x-4,y-7,x-2,y-6,x,y-4,x+2,y-6,x+4,y-7,x+6,y-6,x+8,y-5,x+9,y-2,x+8,y,fill="#000000",outline="#ffffff")
def create_regeneration(x,y):
    C.create_polygon(x+4,y-4+0.5*8,x+4-0.5*8,y-4,x+4-0.5*9,y-4-0.5*2,x+4-0.5*8,y-4-0.5*5,x+4-0.5*6,y-4-0.5*6,x+4-0.5*4,y-4-0.5*7,x+4-0.5*2,y-4-0.5*6,x+4,y-4-0.5*4,x+4+0.5*2,y-4-0.5*6,x+4+0.5*4,y-4-0.5*7,x+4+0.5*6,y-4-0.5*6,x+4+0.5*8,y-4-0.5*5,x+4+0.5*9,y-4-0.5*2,x+4+0.5*8,y-4,fill="#000000",outline="#ffffff")
    C.create_polygon(x-4,y+4+0.5*8,x-4-0.5*8,y+4,x-4-0.5*9,y+4-0.5*2,x-4-0.5*8,y+4-0.5*5,x-4-0.5*6,y+4-0.5*6,x-4-0.5*4,y+4-0.5*7,x-4-0.5*2,y+4-0.5*6,x-4,y+4-0.5*4,x-4+0.5*2,y+4-0.5*6,x-4+0.5*4,y+4-0.5*7,x-4+0.5*6,y+4-0.5*6,x-4+0.5*8,y+4-0.5*5,x-4+0.5*9,y+4-0.5*2,x-4+0.5*8,y+4,fill="#000000",outline="#ffffff")
def create_regenerationtime(x,y):
    C.create_polygon(x-5,y-3,x-8,y-6,x-6,y-8,x-3,y-5,fill="#000000",outline="#ffffff")
    C.create_polygon(x+5,y-3,x+8,y-6,x+6,y-8,x+3,y-5,fill="#000000",outline="#ffffff")
    C.create_oval(x+8,y+8,x-8,y-8,fill="#000000",outline="#ffffff")
    C.create_line(x-8,y,x-6,y,fill="#ffffff")
    C.create_line(x+8,y,x+6,y,fill="#ffffff")
    C.create_line(x,y-6,x,y-8,fill="#ffffff")
    C.create_line(x,y+6,x,y+8,fill="#ffffff")
    C.create_polygon(x,y+0.5*8,x-0.5*8,y,x-0.5*9,y-0.5*2,x-0.5*8,y-0.5*5,x-0.5*6,y-0.5*6,x-0.5*4,y-0.5*7,x-0.5*2,y-0.5*6,x,y-0.5*4,x+0.5*2,y-0.5*6,x+0.5*4,y-0.5*7,x+0.5*6,y-0.5*6,x+0.5*8,y-0.5*5,x+0.5*9,y-0.5*2,x+0.5*8,y,fill="#000000",outline="#ffffff")
def create_shield(x,y):
    C.create_rectangle(x-4,y-8,x+4,y+8,outline="#ffffff")
    C.create_line(x-4,y-8,x+1,y-6,fill="#ffffff")
    C.create_line(x+4,y-8,x-1,y-6,fill="#ffffff")
    C.create_arc(x,y+2,x+8,y-8,start=0,extent=90,style=tkinter.PIESLICE,outline="#ffffff")
    C.create_arc(x,y+2,x-8,y-8,start=90,extent=90,style=tkinter.PIESLICE,outline="#ffffff")
def create_damage(x,y):
    C.create_line(x-9,y+7,x-7,y+9,fill="#ffffff")
    C.create_line(x-3,y+5,x-7,y+9,fill="#ffffff")
    C.create_line(x-3,y+5,x,y+7,fill="#ffffff")
    C.create_line(x+2,y+5,x,y+7,fill="#ffffff")
    C.create_line(x+2,y+5,x-1,y+3,fill="#ffffff")
    C.create_line(x-1,y+3,x+9,y-7,fill="#ffffff")
    C.create_line(x+9,y-7,x+9,y-9,fill="#ffffff")
    C.create_line(x+9,y-9,x+7,y-9,fill="#ffffff")
    C.create_line(x-3,y+1,x+7,y-9,fill="#ffffff")
    C.create_line(x-5,y-2,x-3,y+1,fill="#ffffff")
    C.create_line(x-5,y-2,x-7,y,fill="#ffffff")
    C.create_line(x-5,y+3,x-9,y+7,fill="#ffffff")
    C.create_line(x-5,y+3,x-7,y,fill="#ffffff")
    C.create_line(x+9,y+7,x+7,y+9,fill="#ffffff")
    C.create_line(x+3,y+5,x+7,y+9,fill="#ffffff")
    C.create_line(x+3,y+5,x,y+7,fill="#ffffff")
    C.create_line(x-2,y+5,x,y+7,fill="#ffffff")
    C.create_line(x-2,y+5,x+1,y+3,fill="#ffffff")
    C.create_line(x+1,y+3,x-9,y-7,fill="#ffffff")
    C.create_line(x-9,y-7,x-9,y-9,fill="#ffffff")
    C.create_line(x-9,y-9,x-7,y-9,fill="#ffffff")
    C.create_line(x+3,y+1,x-7,y-9,fill="#ffffff")
    C.create_line(x+5,y-2,x+3,y+1,fill="#ffffff")
    C.create_line(x+5,y-2,x+7,y,fill="#ffffff")
    C.create_line(x+5,y+3,x+9,y+7,fill="#ffffff")
    C.create_line(x+5,y+3,x+7,y,fill="#ffffff")

l=["create_ranged","create_mortar","create_bubble","create_melee","create_minion","create_stream","create_whip",
   "create_shockwave","create_dash","create_connector","create_blockade","create_teleport","create_invisible",
   "create_invincible","create_gravity","create_time","create_prison","create_turret","create_fly","create_dodge",
   "create_speed","create_health","create_regeneration","create_regenerationtime","create_shield","create_damage"]
d={}
lock=random.randint(2,6)
for i in l:
    d[l.index(i)]=i
for i in range(90):
    for j in range(90):
        if lock or j==0:
            eval(d[random.randint(0,25)]+"("+str(j*22+22)+","+str(i*22+22)+")")
            if lock:
                lock-=1
        else:
            lock=random.randint(2,6)
#        time.sleep(0.1)
        if not random.randint(0,80):
            time.sleep(0.1)
        C.update()
root.mainloop()
