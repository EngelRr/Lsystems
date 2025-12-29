#https://www.pythontutorial.net/tkinter/tkinter-window/
#https://www.pythontutorial.net/tkinter/tkinter-canvas/

import tkinter as tk

root = tk.Tk()
root.title('Tkinter window demo')
#root.geometry('640x360+640+360') #widthxheight+startx+starty

#window creation
window_width = int(1920/2)
window_height = int(1080/2)

#get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

canvas = tk.Canvas(root, width = 640, height = 360, bg = 'white')
canvas.pack(anchor=tk.CENTER, expand=True)


root.mainloop()


