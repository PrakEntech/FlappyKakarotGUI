from tkinter import *
from PIL import ImageTk,Image
import keyboard,random
root = Tk()
root.attributes("-fullscreen", False)
root.configure(bg='Black')
root.iconbitmap(None)
root.geometry("600x361")
root.resizable(height = 0, width = 0)
root.title('Flappy Kakarot')

def Do():
    def quitThis():
        if data[0]=='':data[0]=0
        if float(data[0])<b[3]:open('data/scores.jpg','w+').write(str(b[3]))
        else:pass
        label.destroy()
        ch.destroy()
        score.destroy()
        box[0][0].destroy()
        box[0][1].destroy()
        box[1][0].destroy()
        box[1][1].destroy()
        box[2][0].destroy()
        box[2][1].destroy()
        ending['text']='Final Score - '+str(b[3])
        ending.place(x=190,y=80)

    def Doit():
        b[2]+=1
        if b[2]==100:
            b[2]=0
            b[3]+=1
            score['text']='Score - '+str(b[3])
        if (coord[0] in range(boxPos[0][0][0],boxPos[0][0][0]+26) or
        coord[0]+53 in range(boxPos[0][0][0],boxPos[0][0][0]+26)) and (coord[1] in range(boxPos[0][0][1],boxPos[0][0][1]+boxPos[0][0][3]+1) or
                                                                       coord[1]+20 in range(boxPos[0][0][1],boxPos[0][0][1]+boxPos[0][0][3]+1)):
            quitThis()
        if (coord[0] in range(boxPos[0][1][0],boxPos[0][1][0]+26) or
        coord[0]+53 in range(boxPos[0][1][0],boxPos[0][1][0]+26)) and (coord[1] in range(boxPos[0][1][1],boxPos[0][1][1]+101) or
                                                                       coord[1]+20 in range(boxPos[0][1][1],boxPos[0][1][1]+101)):
            quitThis()

        if (coord[0] in range(boxPos[1][0][0],boxPos[1][0][0]+26) or
        coord[0]+53 in range(boxPos[1][0][0],boxPos[1][0][0]+26)) and (coord[1] in range(boxPos[1][0][1],boxPos[1][0][1]+boxPos[1][0][3]+1) or
                                                                       coord[1]+20 in range(boxPos[1][0][1],boxPos[1][0][1]+boxPos[1][0][3]+1)):
            quitThis()
        if (coord[0] in range(boxPos[1][1][0],boxPos[1][1][0]+26) or
        coord[0]+53 in range(boxPos[1][1][0],boxPos[1][1][0]+26)) and (coord[1] in range(boxPos[1][1][1],boxPos[1][1][1]+101) or
                                                                       coord[1]+20 in range(boxPos[1][1][1],boxPos[1][1][1]+101)):
            quitThis()

        if (coord[0] in range(boxPos[2][0][0],boxPos[2][0][0]+26) or
        coord[0]+53 in range(boxPos[2][0][0],boxPos[2][0][0]+26)) and (coord[1] in range(boxPos[2][0][1],boxPos[2][0][1]+boxPos[2][0][3]+1) or
                                                                       coord[1]+20 in range(boxPos[2][0][1],boxPos[2][0][1]+boxPos[2][0][3]+1)):
            quitThis()
        if (coord[0] in range(boxPos[2][1][0],boxPos[2][1][0]+26) or
        coord[0]+53 in range(boxPos[2][1][0],boxPos[2][1][0]+26)) and (coord[1] in range(boxPos[2][1][1],boxPos[2][1][1]+101) or
                                                                       coord[1]+20 in range(boxPos[2][1][1],boxPos[2][1][1]+101)):
            quitThis()

        coord[0],coord[1]=coord[0]+1,coord[1]+1
        if keyboard.is_pressed('w') or kp[0]==True:
            coord[1]-=3
            kp[0]=True
            b[0]+=1
            if b[0]==10:
                kp[0]=False
                b[0]=0
                b[1]=1
        if coord[0]==580:
            q=[None,None,None]
            coord[0]=0
            while (q[1]==q[2] and q[1]==q[0]):
                q[0],q[1],q[2]=random.randint(0,2),random.randint(0,2),random.randint(0,2)
            x=0
            for i in range(3):
                if i==0:x=100
                elif i==1:x=300
                else:x=500
                if q[i]==0:    
                    box[i][0].place(x=x,y=2,width=25, height=85)
                    box[i][1].place(x=x,y=137,width=25, height=100)
                    boxPos[i][0]=[x,2,25,85]
                    boxPos[i][1]=[x,137]
                if q[i]==1:
                    box[i][0].place(x=x,y=2,width=25, height=55)
                    box[i][1].place(x=x,y=112,width=25, height=100)
                    boxPos[i][0]=[x,2,25,55]
                    boxPos[i][1]=[x,112]
                if q[i]==2:
                    box[i][0].place(x=x,y=2,width=25, height=105)
                    box[i][1].place(x=x,y=157,width=25, height=100)
                    boxPos[i][0]=[x,2,25,105]
                    boxPos[i][1]=[x,157]
        ch.place(x=coord[0],y=coord[1],width=53, height=20)
        root.after(15, Doit)    
    root.geometry("600x200")
    label90.destroy()
    start90.destroy()
    exit90.destroy()
    hscores90.destroy()
    label = Label(root,image=photo)
    label.place(x=-2,y=0)
    b=[0,0,0,0]
    kp=[False]
    coord=[0,90]
    ch = Button(root,image=char,bg='#ffc800',borderwidth=0)
    ch.place(x=0,y=90,width=53, height=20)
    box=[[Label(root,image=bar,borderwidth=0),Label(root,image=bar,borderwidth=0)],
         [Label(root,image=bar,borderwidth=0),Label(root,image=bar,borderwidth=0)],
         [Label(root,image=bar,borderwidth=0),Label(root,image=bar,borderwidth=0)]]
    boxPos=[[[100,2,25,85],[100,137]],
            [[300,2,25,55],[300,112]],
            [[500,2,25,105],[500,157]]]
    box[0][0].place(x=100,y=2,width=25, height=85)
    box[0][1].place(x=100,y=137,width=25, height=100)
    box[1][0].place(x=300,y=2,width=25, height=55)
    box[1][1].place(x=300,y=112,width=25, height=100)
    box[2][0].place(x=500,y=2,width=25, height=105)
    box[2][1].place(x=500,y=157,width=25, height=100)
    score = Label(root,text='Score - ',fg = 'white',bg='Black',borderwidth=0,font = ("Calibri",10,"bold"))
    score.place(x=0,y=185)
    root.after(15, Doit)


#Button
char=PhotoImage(file = "data/goku.png")
bar=PhotoImage(file = "data/block.png")
photo = PhotoImage(file = "data/back.png")
photo2 = PhotoImage(file = "data/wall.png")
label90 = Label(root,image=photo2)
label90.place(x=-2,y=0)

start90 = Button(root,activebackground='#F96224',activeforeground='cyan',text='Start',fg = 'white',bg='#F96224',borderwidth=0,font = ("Calibri",20,"bold"),command=Do)
start90.place(x=70,y=100,width=68,height=22)

exit90 = Button(root,activebackground='#F96224',activeforeground='cyan',text='Quit',fg = 'white',bg='#F96224',borderwidth=0,font = ("Calibri",20,"bold"),command=exit)
exit90.place(x=140,y=100,width=68,height=25)
data=[open('data/scores.jpg','r').read()]
if data[0]=='':data[0]=0
hscores90 = Label(root,text='Highest Score - '+str(data[0]),fg = 'white',bg='#F85B21',borderwidth=0,font = ("Calibri",15,"bold"))
hscores90.place(x=73,y=130,height=22)

ending = Label(root,text='',fg = 'white',bg='Black',borderwidth=0,font = ("Calibri",30,"bold"))
root.mainloop()
