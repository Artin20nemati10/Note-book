import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkfont
from tkinter import messagebox


window = tk.Tk()
window.title("NoteBook")
window.geometry("600x400")
text_font= tkfont.Font(family="Arial",size = 14 )

text_area= tk.Text(window, font=text_font)
text_area.pack(expand=True,fill="both")


def OpenFile():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open (file_path, "r",encoding="utf-8") as file:
            content= file.read()
            text_area.delete(1.0, tk.END) 
            text_area.insert(tk.END, content)

def SaveFile():
    file_path= filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path,"w",encoding="utf-8") as file:
            content=text_area.get(1.0, tk.END)
            file.write(content)
def increase_font():
    current_size = text_font["size"]
    text_font.configure(size=current_size + 2)

def dicrease_font():
    current_size = text_font["size"]
    text_font.configure(size=max(8, current_size - 2))

def open_size_window():


    try :
        start=text_area.index("sel.first")
        end=text_area.index("sel.last")
    except tk.TclError :
        messagebox.showerror("Error","Select an area")
        return
    

    popup= tk.Toplevel(window)
    popup.title("Font Size")
    popup.geometry("160x130")
    popup.resizable(False,False)

    label = tk.Label(popup, text="Enter your font size :")
    label.pack(pady=5)
    entry= tk.Entry(popup)
    entry.pack()
    def apply():
        try:
            Size=int(entry.get())
            if Size<8:
                raise ValueError
            
        except ValueError:
            messagebox.showerror("Error","Enter a float number")

        NewFont= tkfont.Font(family="Arial", size=Size)
        tagname=f"font_{Size}_{start.replace('.','_')}"
        text_area.tag_add(tagname,start,end)
        text_area.tag_configure(tagname, font=NewFont)
        popup.destroy()
    tk.Button(popup, text="agree",command=apply).pack(pady=4)
    



menu_bar= tk.Menu(window)

FileMenu= tk.Menu(menu_bar, tearoff=0)

FileMenu.add_command(label="Open File", command=OpenFile)

FileMenu.add_command(label="Save", command=SaveFile)

FileMenu.add_command(label="Exit", command=window.quit)

menu_bar.add_cascade(label="File", menu=FileMenu)

window.config(menu=menu_bar)
##################################

ViewMenu= tk.Menu(menu_bar, tearoff=0)

ViewMenu.add_command(label="Font Size", command=open_size_window)

ViewMenu.add_command(label="Font color", command=None)

ViewMenu.add_command(label="Font", command=None)

menu_bar.add_cascade(label="View", menu=ViewMenu)

window.config(menu=menu_bar)
window.mainloop()