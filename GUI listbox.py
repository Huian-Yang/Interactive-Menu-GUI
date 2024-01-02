

from tkinter import *

def submit():
    
    food = []
    
    for index in listbox.curselection(): #for loop will iterate once for each item we select
        food.insert(index,listbox.get(index)) #obtain the index and the item at each index
        
    print("You have ordered: ")
    
    for index in food:  #print out everything we select and press submit
        print(index)
        
def add():
    listbox.insert(listbox.size(),entryBox.get()) #we need (index, item)
    listbox.config(height=listbox.size()) #chnages the size dynamically as more stuff is added by the user
    
def delete():
    for index in reversed(listbox.curselection()): #revered - to work towards zero in that order
        listbox.delete(index)
        
    listbox.config(height=listbox.size()) #configs the size after an item is deleted
    

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia',35),
                  width=50,
                  selectmode=MULTIPLE, #allows to submit multiple items
                  )
listbox.pack() #make it show

listbox.insert(1,"Pizza $5") #(index, text item)
listbox.insert(2,"Pasta $8") #(index, text item)
listbox.insert(3,"Garlic Bread $2") #(index, text item)
listbox.insert(4,"Soup $3") #(index, text item)
listbox.insert(5,"Salad $2") #(index, text item)

listbox.config(height=listbox.size()) #adjust the size of listbox dynamically

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack() #make it show

addButton = Button(window,text="add",command=add)
addButton.pack() #make it show

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()

window.mainloop() #display GUI