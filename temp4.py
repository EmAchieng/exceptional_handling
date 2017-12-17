from db import *

from tkinter import *

  

addCar('normal', 1500, 4, 4, 20);

addCar('normal', 2000, 4, 5, 20);

addCar('normal', 1500, 4, 4, 30);

addCar('normal', 2000, 4, 6, 50);

addCar('normal', 2000, 4, 7, 60);

addCar('sport', 2000, 4, 6, 50);

addCar('sport', 2000, 4, 7, 60);

  

window = Tk()

def proc_add():
    t = e1.get();
    c = e2.get();
    w = e3.get();
    s = e4.get();
    f = e5.get();

    
    










t1.insert(INSERT, "new "+t+ " "+c+"cc car with"+s+" seats is added")

addCar(t, int(c), int(w), int(s), int(f));

  

def proc_del():
    

    e1.delete(0, 'end');

    e2.delete(0, 'end');

    e3.delete(0, 'end');

    e4.delete(0, 'end');

    e5.delete(0, 'end');



def proc_search():

    t = e1.get();

cars = searchCar(t);

for c in cars:

    t1.insert(INSERT, c);

    t1.insert(INSERT, '\n')

  

  

f1 = Frame(window);

l1=Label(f1, text="type", width=10)

l1.pack(side=LEFT, padx=10, pady=10)

#l1.pack(side=LEFT)

e1=Entry(f1, bg='white', fg='black') 

e1.pack(fill=X, padx=10, expand=True) 

f1.place(x=0, y=0)

  

f2 = Frame(window);

l2=Label(f2, text="capa", width=10)

l2.pack(side=LEFT, padx=10, pady=10)

e2=Entry(f2, bg='white', fg='black') 

e2.pack(fill=X, padx=10, expand=True) 

f2.place(x=0, y=50)

  

f3 = Frame(window);

l3=Label(f3, text="wheel", width=10)

l3.pack(side=LEFT, padx=10, pady=10)

e3=Entry(f3, bg='white', fg='black') 

e3.pack(fill=X, padx=10, expand=True) 

f3.place(x=0, y=100)

  

f4 = Frame(window);

l4=Label(f4, text="seats", width=10)

l4.pack(side=LEFT, padx=10, pady=10)

e4=Entry(f4, bg='white', fg='black') 

e4.pack(fill=X, padx=10, expand=True) 

f4.place(x=0, y=150)

  

f5 = Frame(window);

l5=Label(f5, text="fuel", width=10)

l5.pack(side=LEFT, padx=10, pady=10)

e5=Entry(f5, bg='white', fg='black') 

e5.pack(fill=X, padx=10, expand=True) 

f5.place(x=0, y=200)

  

  

b1 = Button(window, text="add", width=10, command=proc_add)

b2 = Button(window, text="search", width=10, command=proc_search)

b3 = Button(window, text="del", width=10, command=proc_del)

  

b1.place(x = 50, y = 250)

b2.place(x = 150, y = 250)

b3.place(x = 250, y = 250)

  

t1 = Text(window, bg='white', fg='black')

t1.place(x = 10, y = 300)

  

  

window.mainloop()