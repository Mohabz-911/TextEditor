from tkinter import ttk
import tkinter as tk

root = tk.Tk()
style = ttk.Style(root)

# tell tcl where to find the awthemes packages
root.tk.eval("""
set base_theme_dir ./awthemes-10.4.0

package ifneeded awthemes 10.4.0 \
    [list source [file join $base_theme_dir awthemes.tcl]]
package ifneeded colorutils 4.8 \
    [list source [file join $base_theme_dir colorutils.tcl]]
package ifneeded awdark 7.12 \
    [list source [file join $base_theme_dir awdark.tcl]]
package ifneeded awlight 7.6 \
    [list source [file join $base_theme_dir awlight.tcl]]
""")
# load the awdark and awlight themes
root.tk.call("package", "require", 'awdark')
root.tk.call("package", "require", 'awlight')

print(style.theme_names())
# --> ('awlight', 'clam', 'alt', 'default', 'awdark', 'classic')

style.theme_use('awdark')

ttk.Button(root, text='Button').pack()
ttk.Checkbutton(root, text='Check Button').pack()
ttk.Radiobutton(root, text='Radio Button').pack()
root.configure(bg=style.lookup('TFrame', 'background'))
root.mainloop()