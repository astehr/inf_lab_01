from tkinter import *
from tkinter import ttk

class Game(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry('600x600+1+1')
        self.resizable(width=False, height=False)
        self.set_ui()

    def set_ui(self):
        exit_but = ttk.Button(self, text='Exit',
                              command=self.app_exit)
        exit_but.place(x=510, y=550)

        frame = Frame(self, bg="grey",
                         height=500, width=500)

        canvas = Canvas(frame, width=500, height=500, bg='white')
        canvas.bind("<Button-1>", self.gun)
        frame.pack()
        self.objects(canvas)
        canvas.pack()

    def objects(self, c):
        x_1, y_1, x_2, y_2 = 100, 100, 200, 200
        for i in range(9):
            colour = 'purple'
            if i == 4 or i == 0 or i == 2:
                colour = 'white'
            c.create_rectangle(x_1, y_1, x_2, y_2,
                               fill=colour,
                               outline='black',
                               width=2,
                               activedash=(5, 4))
            if i != 2 and i !=5:
                x_1 += 100
                x_2 += 100
            elif i == 2:
                x_1, y_1, x_2, y_2 = 100, 200, 200, 300
            else:
                x_1, y_1, x_2, y_2 = 100, 300, 200, 400
        c.create_arc(
            100, 100, 300, 300,
            start=90,
            extent=90,
            fill='purple',
            outline='black',
            width=2,
            activedash=(5, 4))
        c.create_arc(
            300, 300, 500, 500,
            start=90,
            extent=90,
            fill='white',
            outline='black',
            width=2,
            activedash=(5, 4))
        points = [300, 100, 400, 200, 300, 200]
        c.create_polygon(
            points,
            outline='black',
            fill='purple',
            activedash=(5, 4))
    def gun(self, event):
        x, y = event.x, event.y
        #canvas = Canvas(self, width=20, height=20, bg='white')
        image = PhotoImage(file='Images/img.png')
        dat = ('red',) * 480
        panel = Label(self, image=image)
        panel.place(x=x, y=y)
        #canvas.create_image(x, y, image=image)


        print(x, y)

    def print_event(self, event):
        position = "(x={}, y={})".format(event.x, event.y)
        print(event.type, "event", position)

    def app_exit(self):
        self.destroy()

if __name__ == '__main__':
    root = Game()
    root.mainloop()
