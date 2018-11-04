# -*- coding: utf-8 -*
"""
Created on Sun Oct 21 17:45:41 2018

@author: Anand
"""

import tkinter as t
from tkinter import ttk as tk
    
    
def save_file(e):
    print(text.get("1.0", 'end-1c'));
    a = text.get("1.0", 'end-1c');
    with open(e, 'w') as f:
        f.write(a);
        
def open_file(e):
    name = e
    print(name)
    s = t.Tk()
    try:
        with open(name) as f:
            k = f.read()
            show = t.Text(s)
            show.insert("end", k)
            show.pack()
        
    except Exception as e:
        print(e)
        message = t.Label(s, text="File does not exist")
        message.pack()
    s.mainloop()
        
        
def op():
    o = t.Tk();
    e = t.Entry(o);
    e.pack();
    b = tk.Button(o, text = "Open", command = lambda:open_file(e.get()))
    b.pack()
    o.mainloop();

def save():
    r2 = t.Tk();
    e = t.Entry(r2);
    e.pack();
    but = tk.Button(r2, text = "Save", command = lambda:save_file(e.get()));
    but.pack();
    r2.mainloop();

r = t.Tk()
text = t.Text(r);
text.pack();
save = tk.Button(r, text = "Save file", command = save);
save.pack();
op = tk.Button(r, text = "Open file", command = op);
op.pack();
r.mainloop()
