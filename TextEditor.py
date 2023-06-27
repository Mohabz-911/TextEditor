import os
import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

class TextEditor:
    def __init__(self):
        self.root = tk.Tk()

        # Variable to store state of opened file
        self.isOpened = False
        self.filename = ''

        # Setting the window size and title
        self.root.geometry('800x500')
        self.root.title('Text Editor')
        self.root.iconbitmap('./assets/icons/white_bg.ico')

        # Text editing area
        self.textbox = tk.Text(self.root, height=500, width=800, font=('Cairo', 12), foreground='White', background='Black')
        self.textbox.pack()

        # Menu
        self.main_menu = tk.Menu(self.root)
        self.main_menu.add_command(label='Open', command=self.open_file)
        self.main_menu.add_command(label='Save', command=self.save_file)
        self.root.config(menu=self.main_menu)

        self.root.mainloop()

    # This function will be used to open
    # file in read mode and only Text files
    # will be opened
    def open_file(self):
        file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
        if file is not None:
            self.filename = file.name
            self.isOpened = True

            content = file.read()
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('insert', content)

            filename_without_ext = os.path.splitext(os.path.basename(self.filename))[0]
            self.root.title(filename_without_ext)
    
    # function to call when user press save button
    def save_file(self):
        if self.isOpened == False:
            files = [('Text Document', '*.txt')]
            self.filename = asksaveasfile(filetypes = files, defaultextension = files).name
            self.isOpened = True
        with open(self.filename, 'w') as f:
            f.write(self.textbox.get('1.0', tk.END))



if __name__ == '__main__':
    app = TextEditor()