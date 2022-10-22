import psutil                    # pip3 install pillow
from tkinter import *            # if need Administrator prems: pip3 install --user pillow
from PIL import Image, ImageTk

# GUI

window = Tk()
window.title("My CPU")

# Images

CPU_file = Image.open("CPU-icons8.png")
RAM_file = Image.open("RAM-icons8.png")
Disk_file = Image.open("Disk-icons8.png")

CPU_image = ImageTk.PhotoImage(CPU_file)
RAM_image = ImageTk.PhotoImage(RAM_file)
Disk_image = ImageTk.PhotoImage(Disk_file)

# Text

def update_numbers():
    CPU_see.set(str(psutil.cpu_percent()) + "%")
    RAM_see.set(str(psutil.virtual_memory().percent) + "%")
    Disk_see.set(str(psutil.disk_usage("/").used // 1000000000) + "GB /" + str(psutil.disk_usage("/").total // 1000000000) +'GB')
    # 1000000000 - 1 GB in bytes
    window.after(1000, update_numbers)

CPU_see = StringVar()
RAM_see = StringVar()
Disk_see = StringVar()

# Images output & text

Label(window, image=CPU_image).grid(row=0, column=0)
Label(window, image=RAM_image).grid(row=1, column=0)
Label(window, image=Disk_image).grid(row=2, column=0)
Label(window, textvariable=CPU_see, width=30, height=5).grid(row=0, column=1)
Label(window, textvariable=RAM_see, width=30, height=5).grid(row=1, column=1)
Label(window, textvariable=Disk_see, width=30, height=5).grid(row=2, column=1)

window.after(1000, update_numbers)

mainloop()
