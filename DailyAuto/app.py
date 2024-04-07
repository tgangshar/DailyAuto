import tkinter as tk
from tkinter import ttk

class AutomationApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window size to half of the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        # Configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # Configure style
        self.style = ttk.Style(self)
        self.style.theme_use('clam') # Set the theme to 'clam'
        self.style.configure('TButton', font=('Helvetica', 12), background='blue', foreground='white')

       # Create buttons
        button1 = ttk.Button(self, text="Button 1", style='TButton')
        button2 = ttk.Button(self, text="Button 2", style='TButton')
        button3 = ttk.Button(self, text="Button 3", style='TButton')

        # Place buttons in the middle column
        button1.grid(column=1, row=1, sticky=tk.N+tk.S+tk.E+tk.W)
        button2.grid(column=1, row=2, sticky=tk.N+tk.S+tk.E+tk.W)
        button3.grid(column=1, row=3, sticky=tk.N+tk.S+tk.E+tk.W)

if __name__ == "__main__":
    app = AutomationApp()
    app.mainloop()
