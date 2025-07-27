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

is_saved=True

#############################################
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

def on_text(event=None):
    global is_saved
    is_saved=False

def file_saved():
    global is_saved
    is_saved= True

def fgcol():
        try:
            start= text_area.index("sel.first")
            end=text_area.index("sel.last") 
        except:
            messagebox.showerror("Error","Select an area")
            return
            
        popup= tk.Toplevel(window)
        popup.title("Font Color")
        popup.geometry("130x690")
        popup.resizable(False,False)
        label = tk.Label(popup, text="Enter your font color :")
        label.pack(pady=5)


        def color_select(color):
            tagname= f"color_{color}"
            text_area.tag_add(tagname, start, end)
            text_area.tag_configure(tagname, foreground=color)
            popup.destroy()
        tk.Button(popup, text="Black",bg="black",fg="White", command=lambda:color_select("black")).pack(pady=2)

        tk.Button(popup, text="white",bg="white",fg="black", command=lambda:color_select("white")).pack(pady=2)

        tk.Button(popup, text="Red",bg="red", command=lambda:color_select("red")).pack(pady=2)
        
        tk.Button(popup, text="Blue",bg="blue", command=lambda:color_select("blue")).pack(pady=2)
        
        tk.Button(popup, text="Green",bg="green", command=lambda:color_select("green")).pack(pady=2)
        
        tk.Button(popup, text="Yellow",bg="yellow", command=lambda:color_select("yellow")).pack(pady=2)
        
        tk.Button(popup, text="Pink",bg="Pink", command=lambda:color_select("pink")).pack(pady=2)
        
        tk.Button(popup, text="Purple",bg="Purple", command=lambda:color_select("purple")).pack(pady=2)
        
        tk.Button(popup, text="Orange",bg="Orange", command=lambda:color_select("orange")).pack(pady=2)
        
        tk.Button(popup, text="Cyan",bg="Cyan", command=lambda:color_select("cyan")).pack(pady=2)
        
        tk.Button(popup, text="Gold",bg="Gold", command=lambda:color_select("gold")).pack(pady=2)
        
        tk.Button(popup, text="gray",bg="gray", command=lambda:color_select("gray")).pack(pady=2)
        
        tk.Button(popup, text="SkyBlue",bg="SkyBlue", command=lambda:color_select("skyblue")).pack(pady=2)
        
        tk.Button(popup, text="Brown",bg="Brown", command=lambda:color_select("brown")).pack(pady=2)
        
        tk.Button(popup, text="Lime",bg="Lime", command=lambda:color_select("lime")).pack(pady=2)
        
        tk.Button(popup, text="silver",bg="silver", command=lambda:color_select("silver")).pack(pady=2)
        
        tk.Button(popup, text="Maroon",bg="Maroon", command=lambda:color_select("maroon")).pack(pady=2)
        
        tk.Button(popup, text="Navy",bg="Navy", command=lambda:color_select("navy")).pack(pady=2)
        
        tk.Button(popup, text="Olive",bg="Olive", command=lambda:color_select("olive")).pack(pady=2)
        
        tk.Button(popup, text="Violet",bg="Violet", command=lambda:color_select("violet")).pack(pady=2)
        
        tk.Button(popup, text="Turquoise",bg="Turquoise", command=lambda:color_select("turquoise")).pack(pady=2)
        
        tk.Button(popup, text="Indigo",bg="Indigo", command=lambda:color_select("indigo")).pack(pady=2)

def bgcol():
        try:
            start= text_area.index("sel.first")
            end=text_area.index("sel.last") 
        except:
            messagebox.showerror("Error","Select an area")
            return
        popup= tk.Toplevel(window)
        popup.title("Font Color")
        popup.geometry("130x670")
        popup.resizable(False,False)
        label = tk.Label(popup, text="Enter your font color :")
        label.pack(pady=5)


        def color_select(color):
            tagname= f"color_{color}"
            text_area.tag_add(tagname, start, end)
            text_area.tag_configure(tagname, background=color)
            popup.destroy()
        tk.Button(popup, text="Black",bg="black",fg="White", command=lambda:color_select("black")).pack(pady=2)

        tk.Button(popup, text="white",bg="white",fg="black", command=lambda:color_select("white")).pack(pady=2)

        tk.Button(popup, text="Red",bg="red", command=lambda:color_select("red")).pack(pady=2)
        
        tk.Button(popup, text="Blue",bg="blue", command=lambda:color_select("blue")).pack(pady=2)
        
        tk.Button(popup, text="Green",bg="green", command=lambda:color_select("green")).pack(pady=2)
        
        tk.Button(popup, text="Yellow",bg="yellow", command=lambda:color_select("yellow")).pack(pady=2)
        
        tk.Button(popup, text="Pink",bg="Pink", command=lambda:color_select("pink")).pack(pady=2)
        
        tk.Button(popup, text="Purple",bg="Purple", command=lambda:color_select("purple")).pack(pady=2)
        
        tk.Button(popup, text="Orange",bg="Orange", command=lambda:color_select("orange")).pack(pady=2)
        
        tk.Button(popup, text="Cyan",bg="Cyan", command=lambda:color_select("cyan")).pack(pady=2)
        
        tk.Button(popup, text="Gold",bg="Gold", command=lambda:color_select("gold")).pack(pady=2)
        
        tk.Button(popup, text="gray",bg="gray", command=lambda:color_select("gray")).pack(pady=2)
        
        tk.Button(popup, text="SkyBlue",bg="SkyBlue", command=lambda:color_select("skyblue")).pack(pady=2)
        
        tk.Button(popup, text="Brown",bg="Brown", command=lambda:color_select("brown")).pack(pady=2)
        
        tk.Button(popup, text="Lime",bg="Lime", command=lambda:color_select("lime")).pack(pady=2)
        
        tk.Button(popup, text="silver",bg="silver", command=lambda:color_select("silver")).pack(pady=2)
        
        tk.Button(popup, text="Maroon",bg="Maroon", command=lambda:color_select("maroon")).pack(pady=2)
        
        tk.Button(popup, text="Navy",bg="Navy", command=lambda:color_select("navy")).pack(pady=2)
        
        tk.Button(popup, text="Olive",bg="Olive", command=lambda:color_select("olive")).pack(pady=2)
        
        tk.Button(popup, text="Violet",bg="Violet", command=lambda:color_select("violet")).pack(pady=2)
        
        tk.Button(popup, text="Turquoise",bg="Turquoise", command=lambda:color_select("turquoise")).pack(pady=2)
        
        tk.Button(popup, text="Indigo",bg="Indigo", command=lambda:color_select("indigo")).pack(pady=2)

def Font():
        try:
            start= text_area.index("sel.first")
            end=text_area.index("sel.last") 
        except:
            messagebox.showerror("Error","Select an area")
            return
        popup= tk.Toplevel(window)
        popup.title("Font")
        popup.geometry("130x420")
        popup.resizable(False,False)
        label = tk.Label(popup, text="Enter your font :")
        label.pack(pady=5)


        def font_select(font):
            tagname= f"color_{font}"
            text_area.tag_add(tagname, start, end)
            text_area.tag_configure(tagname, font=font)
            popup.destroy()
        tk.Button(popup, text="Arial", command=lambda:font_select("Arial")).pack(pady=2)
        tk.Button(popup, text="Times", command=lambda:font_select("Times")).pack(pady=2)
        tk.Button(popup, text="Courier", command=lambda:font_select("Courier")).pack(pady=2)
        tk.Button(popup, text="Comic", command=lambda:font_select("Comic")).pack(pady=2)
        tk.Button(popup, text="Calibari", command=lambda:font_select("Calibari")).pack(pady=2)
        tk.Button(popup, text="Cambria", command=lambda:font_select("Cambria")).pack(pady=2)
        tk.Button(popup, text="Impact", command=lambda:font_select("Impact")).pack(pady=2)
        tk.Button(popup, text="Lucida", command=lambda:font_select("lucida")).pack(pady=2)
        tk.Button(popup, text="Georgia", command=lambda:font_select("Georgia")).pack(pady=2)
        tk.Button(popup, text="Trabuchet", command=lambda:font_select("Trabuchet")).pack(pady=2)
        tk.Button(popup, text="Papyrus", command=lambda:font_select("Papyrus")).pack(pady=2)
        tk.Button(popup, text="Jokerman", command=lambda:font_select("Jokerman")).pack(pady=2)
        tk.Button(popup, text="Chiller", command=lambda:font_select("Chiller")).pack(pady=2)

def on_exit():
    if not is_saved:
        answer= messagebox.showerror("Attention : Your file doesn't saved","Do you want to save it?")

        if answer :
            SaveFile()
            window.destroy()
        elif answer is None:
            return
        else:
            window.destroy()
    else:
        window.destroy()
##############################################
menu_bar= tk.Menu(window)

FileMenu= tk.Menu(menu_bar, tearoff=0)

FileMenu.add_command(label="Open File", command=OpenFile)

FileMenu.add_command(label="Save", command=SaveFile)

FileMenu.add_command(label="Exit", command=on_exit)

menu_bar.add_cascade(label="File", menu=FileMenu)

window.config(menu=menu_bar)
##################################

ViewMenu= tk.Menu(menu_bar, tearoff=0)

ViewMenu.add_command(label="Font Size", command=open_size_window)

ViewMenu.add_command(label="Font fg color", command=fgcol)

ViewMenu.add_command(label="Font bg color", command=bgcol)

ViewMenu.add_command(label="Font", command=Font)

menu_bar.add_cascade(label="View", menu=ViewMenu)

text_area.bind("<Key>", on_text)

window.config(menu=menu_bar)

window.mainloop()