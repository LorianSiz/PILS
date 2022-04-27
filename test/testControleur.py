from time import sleep
from ivy.std_api import *
from tkinter import Tk, Canvas
import queue

IvyInit("test")

class Controleur:

    def read_msg(self, *arg):
        print(self.name + " rec from: " + str(arg[0]) + " --> " + arg[1])
        self.queue.put(arg[1])


    def __init__(self, _name, _ip):
        self.name = _name
        self.ip = _ip
        self.running = 1
        self.queue = queue.Queue()

        IvyStart(self.ip)
        IvyBindMsg(self.read_msg, "Test -->(.*)")

        #self.loop()

    def loop(self):
        while not self.queue.empty():
            current = self.queue.get()
            tab = current.split()
            print(tab)

            # func = getattr(Visualizer, tab[0])
            # func(self, tab[1])
            # if (tab[0] != "redraw") & (tab[0] != "erase"):
            #     self.list_actions.append(tab)

        if not self.running:
            import sys
            sys.exit(1)

        sleep(100)


main1 = Controleur("ctrl1", "127.0.0.1:123")
main2 = Controleur("ctrl2", "127.0.0.1:124")

