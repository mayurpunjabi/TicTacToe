from tkinter import *
import random

class TicTacToe:
    def __init__(self, frame):
        self.frame = frame
        self.frame.bind("<Button-1>", self.action)
        self.frame1 = Frame(self.frame)
        self.can = Canvas(self.frame, height=600, width=600, bg="#2fcfbf")
        self.can.grid(row=0,column=0)
        self.can.create_rectangle(0,0,602,200,fill="#f5f5f5",width=0)
        Label(self.frame, text="Tic", fg="red",bg="#f5f5f5",font=("Comic Sans MS",30)).place(x=220,y=20,anchor=N)
        Label(self.frame, text="Tac", fg="#00f000",bg="#f5f5f5",font=("Comic Sans MS",30)).place(x=300,y=20,anchor=N)
        Label(self.frame, text="Toe", fg="blue",bg="#f5f5f5",font=("Comic Sans MS",30)).place(x=380,y=20,anchor=N)
        self.dl = StringVar()
        self.dl.set("E")
        Radiobutton(self.frame, text="Easy", variable=self.dl, value="E",command=self.diff,bg="#f5f5f5",font=("Comic Sans MS",16)).place(x=90,y=110,anchor=CENTER)
        Radiobutton(self.frame, text="Medium", variable=self.dl, value="M",command=self.diff,bg="#f5f5f5",font=("Comic Sans MS",16)).place(x=195,y=110,anchor=CENTER)
        Radiobutton(self.frame, text="Hard", variable=self.dl, value="H",command=self.diff,bg="#f5f5f5",font=("Comic Sans MS",16)).place(x=300,y=110,anchor=CENTER)
        Radiobutton(self.frame, text="Play With A Friend", variable=self.dl, value="2P",command=self.diff,bg="#f5f5f5",font=("Comic Sans MS",16)).place(x=460,y=110,anchor=CENTER)
        self.Xbutton = Button(self.frame, text="X",fg="#5c5c5c",bg="white",font=("Arial", 20), width=8, bd=0,command=lambda:self.change("X",165,305))
        self.Xbutton.place(x=230,y=160,anchor=CENTER)
        self.Obutton = Button(self.frame, text="O",fg="#5c5c5c",bg="white",font=("Arial", 20),width=8, bd=0,command=lambda:self.preChange("O",305,165))
        self.Obutton.place(x=370,y=160,anchor=CENTER)
        Button(self.frame, text="Restart Game", fg="#2fcfbf",bg="white",font=("Courier",22),width=36,command=self.restart).place(x=300,y=605,anchor=S)
        self.restart()
    def restart(self):
        self.frame1.destroy()
        self.can.create_rectangle(0,200,602,550,fill="#2fcfbf",width=0)
        self.can.create_line(250,248,250,500,fill="purple",width=7)
        self.can.create_line(334,248,334,500,fill="purple",width=7)
        self.can.create_line(166,332,418,332,fill="purple",width=7)
        self.can.create_line(166,416,418,416,fill="purple",width=7)
        self.Xbutton.config(state=NORMAL)
        self.Obutton.config(state=NORMAL)
        self.xs = []
        self.os = []
        self.cpu = "O"
        self.change("X",165,305)
        self.drawPos = [[166,248], [250,248], [334,248], [166,332], [250,332], [334,332], [166,416], [250,416], [334,416]]
    def action(self, event):
        if event.x > 166 and event.x < 250 and event.y > 248 and event.y < 332:
            self.draw(166,248)
        elif event.x > 250 and event.x < 334 and event.y > 248 and event.y < 332:
            self.draw(250,248)
        elif event.x > 334 and event.x < 418 and event.y > 248 and event.y < 332:
            self.draw(334,248)
        elif event.x > 166 and event.x < 250 and event.y > 332 and event.y < 416:
            self.draw(166,332)
        elif event.x > 250 and event.x < 334 and event.y > 332 and event.y < 416:
            self.draw(250,332)
        elif event.x > 334 and event.x < 418 and event.y > 332 and event.y < 416:
            self.draw(334,332)
        elif event.x > 166 and event.x < 250 and event.y > 416 and event.y < 500:
            self.draw(166,416)
        elif event.x > 250 and event.x < 334 and event.y > 416 and event.y < 500:
            self.draw(250,416)
        elif event.x > 334 and event.x < 418 and event.y > 416 and event.y < 500:
            self.draw(334,416)
    def draw(self, x, y):
        if [x,y] in self.drawPos:
            self.drawPos.remove([x,y])
            if self.img == "O":
                self.can.create_oval(x+13,y+13,x+70,y+70,width=7,outline="white")
                self.os.append([x,y])
                if self.check(self.os):
                    self.frame.after(750,lambda:self.winner("O","white"))
                    return
                self.change("X",165,305)
            else:
                self.can.create_line(x+15,y+15,x+68,y+68,width=7,fill="#5c5c5c")
                self.can.create_line(x+15,y+68,x+68,y+15,width=7,fill="#5c5c5c")
                self.xs.append([x,y])
                if self.check(self.xs):
                    self.frame.after(750,lambda:self.winner("X","#5c5c5c"))
                    return
                self.change("O",305,165)

            if len(self.drawPos)==0:
                self.frame.after(750, self.Draw)
                return
            elif len(self.drawPos)==8:
                self.Xbutton.config(state=DISABLED)
                self.Obutton.config(state=DISABLED)
            if self.dl.get() != "2P" and self.img == self.cpu:
                if self.cpu == "O":
                    self.frame.after(500, lambda:self.CPU(self.os,self.xs))
                else:
                    self.frame.after(500, lambda:self.CPU(self.xs,self.os))
    def check(self,xy):
        x=[]
        y=[]
        for i in xy:
            x.append(i[0])
            if x.count(i[0])==3:
                return True
            y.append(i[1])
            if y.count(i[1])==3:
                return True
        a = [[166,248], [250,332], [334,416]]
        b = [[334,248], [250,332], [166,416]]
        if (a[0] in xy and a[1] in xy and a[2] in xy) or (b[0] in xy and b[1] in xy and b[2] in xy):
            return True
        else:
            return False
    def winner(self,w,c):
        self.frame1 = Frame(self.frame, height=300, width=300,bg="#2fcfbf")
        self.frame1.place(x=300, y=395, anchor=CENTER)
        self.can.create_rectangle(0,200,602,550,fill="#2fcfbf",width=0)
        self.label1 = Label(self.frame1,text=w,fg=c,bg="#2fcfbf",font=("Arial",150))
        self.label1.place(x=150,y=100,anchor=CENTER)
        self.label2 = Label(self.frame1,text="WINNER!",fg="#5c5c5c",bg="#2fcfbf",font=("Arial",50))
        self.label2.place(x=150,y=220,anchor=CENTER)
    def Draw(self):
        self.frame1 = Frame(self.frame, height=300, width=300,bg="#2fcfbf")
        self.frame1.place(x=300, y=395, anchor=CENTER)
        self.can.create_rectangle(0,200,602,550,fill="#2fcfbf",width=0)
        self.label1 = Label(self.frame1,text="X",fg="#5c5c5c",bg="#2fcfbf",font=("Arial",100))
        self.label1.place(x=100,y=100,anchor=CENTER)
        self.label2 = Label(self.frame1,text="O",fg="white",bg="#2fcfbf",font=("Arial",100))
        self.label2.place(x=200,y=100,anchor=CENTER)
        self.label3 = Label(self.frame1,text="DRAW",fg="#5c5c5c",bg="#2fcfbf",font=("Arial",50))
        self.label3.place(x=150,y=220,anchor=CENTER)
    def diff(self):
        self.restart()
        if self.dl.get() == "2P":
            self.Xbutton.config(state=DISABLED)
            self.Obutton.config(state=DISABLED)
    def preChange(self, xo, x1, x2):
        self.cpu = "X"
        self.CPU(self.xs, self.os)
        self.change(xo, x1, x2)
    def change(self, xo, x1, x2):
        self.img = xo
        self.can.create_line(x1,190,x1+130,190,fill="#2fcfbf",width=3)
        self.can.create_line(x2,190,x2+130,190,fill="#f5f5f5",width=3)
    def CPU(self, xo1, xo2):
        xy = random.choice(self.drawPos)
        if self.dl.get() == "M":
            if len(self.overCheck(xo1)):
                xy = self.overCheck(xo1)
            elif len(self.overCheck(xo2)):
                xy = self.overCheck(xo2)
            elif len(xo1) == 0:
                self.pos = self.drawPos.copy()
                if [250, 332] in self.pos:
                    self.pos.remove([250,332])
                xy = random.choice(self.pos)
            else:
                xy = random.choice(self.drawPos)

        elif self.dl.get() == "H":
            if self.img == "O":
                if len(self.overCheck(xo1)):
                    xy = self.overCheck(xo1)
                elif len(self.overCheck(xo2)):
                    xy = self.overCheck(xo2)
                elif len(xo1)==0:
                    if [250,332] in self.drawPos:
                        xy = [250,332]
                    else:
                        xy = [334,248]
                else:
                    if len(xo1)==1 and (([166,248] in self.xs and [334,416] in self.xs) or ([334,248] in self.xs and [166,416] in self.xs)):
                        xy = [166,332]
                    elif [334,416] in self.drawPos:
                        xy = [334,416]
                    else:
                        xy = random.choice(self.drawPos)
            else:
                if len(self.overCheck(xo1)):
                    xy = self.overCheck(xo1)
                elif len(self.overCheck(xo2)):
                    xy = self.overCheck(xo2)
                elif len(xo1)==0:
                    xy = [334,248]
                elif len(xo1)==1:
                    if [166,248] in self.os or [334,416] in self.os:
                        xy = [166,416]
                    elif [250,248] in self.os or [334,332] in self.os:
                        xy = [250,332]
                    elif [166,332] in self.os:
                        xy = [166,248]
                    elif [250,416] in self.os:
                        xy = [334,416]
                    elif [250,332] in self.os:
                        xy = [166,332]
                    elif [166,416] in self.os:
                        xy = [334,416]
                else:
                    if [334,416] in self.drawPos:
                        xy = [334,416]
                    else:
                        xy = random.choice(self.drawPos)
                
        self.draw(xy[0],xy[1])
    def overCheck(self, xy):
            x=[]
            y=[]
            for i in xy:
                x.append(i[0])
                if x.count(i[0])==2:
                    for j in [248,332,416]:
                        if [i[0],j] in self.drawPos:
                            return [i[0],j]
                y.append(i[1])
                if y.count(i[1])==2:
                    for j in [166,250,334]:
                        if [j,i[1]] in self.drawPos:
                            return [j,i[1]]

            a = [[166,248], [250,332], [334,416]]
            b = [[334,248], [250,332], [166,416]]
            if (a[0] in xy and a[1] in xy and a[2] in self.drawPos):
                return a[2]
            elif (a[1] in xy and a[2] in xy and a[0] in self.drawPos):
                return a[0]
            elif (a[0] in xy and a[2] in xy and a[1] in self.drawPos):
                return a[1]
            elif (b[0] in xy and b[1] in xy and b[2] in self.drawPos):
                return b[2]
            elif (b[1] in xy and b[2] in xy and b[0] in self.drawPos):
                return b[0]
            elif (b[0] in xy and b[2] in xy and b[1] in self.drawPos):
                return b[1]
            else:
                return []

root = Tk()
root.title("Tic Tac Toe")
root.resizable(0,0)
TicTacToe(root)
root.mainloop()
