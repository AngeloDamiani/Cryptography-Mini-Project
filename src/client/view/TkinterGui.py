from tkinter import *
from tkinter.ttk import *

from . import Ui


class TkinterGui(Frame, Ui):
    def __init__(self):

        root = Tk()
        root.resizable(width=False, height=False)

        Frame.__init__(self, root)

        self.parent = root
        self.initUI()

    def initUI(self):
        self.parent.title("Chat")


        frame1 = Frame(self.parent, width=50)
        frame2 = Frame(self.parent, width=50, height=20)
        frame3 = Frame(self.parent, width=50)

        frame1.grid(pady=5, padx=5)
        frame2.grid(pady=5, padx=5)
        frame3.grid(padx=5, pady=5)


        lbl0 = Label(frame1, text="User", width=4)
        lbl0.pack(side=LEFT, padx=8)
        txt0 = Text(frame1, width=13, height=1)
        txt0.pack(side=LEFT)

        lbl1 = Label(frame2, text="Chat", width=4)
        lbl1.pack(side=LEFT, padx=8)
        txt1 = Text(frame2, height=20)
        txt1.pack(side=LEFT)
        txt1.config(state=DISABLED)


        txt2 = Text(frame3, width=13, height=2)
        txt2.pack(side=RIGHT)
        lbl2 = Label(frame3, text="Dest")
        lbl2.pack(side=RIGHT, padx=10)

        lbl3 = Label(frame3, text="Text", width=4)
        lbl3.pack(side=LEFT, padx=8)
        txt3 = Text(frame3, width=59, height=2)
        txt3.pack(side=LEFT)

        self.user = txt0
        self.dst = txt2
        self.chat = txt1
        self.text = txt3

        self.text.bind("<Tab>", self.focusOnDst)
        self.dst.bind("<Tab>", self.focusOnText)
        self.parent.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.text.bind('<Return>', self.send)
        self.dst.bind('<Return>', self.focusOnText)

    def start(self, user : "..model.Client"):
        self.user.delete("1.0", END)
        self.user.insert(INSERT, user.name)
        self.user.config(state=DISABLED)
        self.client = user
        self.parent.mainloop()

    def send(self, *args):
        msg = self.text.get("1.0",END)
        msg = msg.split("\n")[0]
        if msg != "":
            me = self.client.name
            dst = self.dst.get("1.0",END)
            dst= dst.split("\n")[0]
            self.text.delete("1.0", END)
            self.text.index(INSERT)
            self.printChat(msg,me)
            self.client.sendMessage(msg,dst)
        return "break"

    def printChat(self,msg,src):
        self.chat.config(state='normal')
        self.chat.insert(END,src+": "+msg+"\n")
        self.chat.config(state='disabled')

    def onClosing(self):
        self.client.stop()
        self.parent.destroy()

    def focusOnDst(self, *args):
        self.dst.focus_force()
        return "break"

    def focusOnText(self, *args):
        self.text.focus_force()
        return "break"





from ..model import Client