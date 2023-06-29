from tkinter import *
import tkinter as tk
import os


def main():

    def open_func():

        def load_func():
            y = choice.get()
            f = open(y, "r")
            content = f.read()
            note_pad.insert(INSERT, content)
            sw.destroy()

        sw = tk.Toplevel()
        sw.geometry("500x500")
        sw.title("Load File")

        files = os.listdir()
        for file in files:
            if os.path.isfile(file):
                label = tk.Label(sw, text=file)
                label.pack()

        choose = tk.Label(sw, text="Choose file to open (include file extension): ")
        choose.pack()

        choice = tk.Entry(sw)
        choice.pack()

        load = tk.Button(sw, text="Load", command=load_func)
        load.pack(pady=8)

        sw.mainloop()

    def save_func():

        data = note_pad.get("1.0", "end")

        sw = tk.Toplevel()
        sw.geometry("500x200")
        sw.title("save file")

        def name_file():
            global filename
            filename = name.get()
            f = open(filename, "w")
            f.write(data)
            sw.destroy()

        txt = tk.Label(sw, text="Enter a name for this file (include file extension): ")
        txt.pack()

        name = tk.Entry(sw)
        name.pack()

        submit = tk.Button(sw, text="save", command=name_file)
        submit.pack(pady=8)

        sw.mainloop()

    window = tk.Tk()
    window.geometry("730x800")
    window.title("Sn0w N0tes")

    save = tk.Button(window, text="save", command=save_func)
    save.grid(pady=5, row=0, column=0, sticky=W+E+N+S)

    openfile = tk.Button(window, text="open", command=open_func)
    openfile.grid(pady=5, row=0, column=1, sticky=W+E+N+S)

    note_pad = tk.Text(window, height=44, width=90)
    note_pad.grid(row=1, columnspan=2, sticky=W+E+N+S)

    window.mainloop()


if __name__ == '__main__':
    main()
