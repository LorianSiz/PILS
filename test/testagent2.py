from ivy.std_api import *
from tkinter import Tk, Canvas
import queue

root = Tk();

class Agent2:

    def read_msg(self, *arg):
        print("From: " + str(arg[0]) + " --> " + arg[1])
        self.queue.put(arg[1])

    def __init__(self, _master):
        self.master = _master
        self.running = 1
        self.queue = queue.Queue()
        
        self.master.title("Writer")
        
        IvyInit("Writer")
        IvyStart()

        self.loop();

    def loop(self):
        while not self.queue.empty():
            current = self.queue.get()
            tab = current.split()
            print(tab)

            # func = getattr(Visualizer, tab[0])
            # func(self, tab[1])
            # if (tab[0] != "redraw") & (tab[0] != "erase"):
            #     self.list_actions.append(tab)

        print(IvySendMsg("Test -->123"))

        if not self.running:
            import sys
            sys.exit(1)

        self.master.after(5000, self.loop)

Agent2(root)
root.mainloop()
