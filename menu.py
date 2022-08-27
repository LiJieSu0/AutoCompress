import tkinter as tk
from tkinter import filedialog
import os
import makeZipFile as mz
import renameFiles as rf


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.isRename = tk.IntVar()
        self.isMakeZip = tk.IntVar()
        self.nameField=None
        self.initUI()


    def initUI(self):
        self.title('Auto Compress')
        self.geometry('200x150')
        self.buttonCreate()
        self.checkBoxCreate()
        self.entryCreate()

    def entryCreate(self):
        self.nameField=tk.Entry(self)
        self.nameField.pack()

    def checkBoxCreate(self):
        def printValue():
            print(self.isRename.get())
            print(self.isMakeZip.get())
        makeZipCKBox = tk.Checkbutton(self, text='Make Zip Files',variable=self.isMakeZip, onvalue=1, offvalue=0, command=printValue)
        makeZipCKBox.pack()
        renameCKBox = tk.Checkbutton(self, text='Rename Files',variable=self.isRename, onvalue=1, offvalue=0, command=printValue)
        renameCKBox.pack()

    def buttonCreate(self):
        def button_event():
            dir = filedialog.askdirectory(initialdir=os.path.normpath("C://"), title="Select the directory you want to compress")
            fileName=self.nameField.get()
            mybutton['text'] = 'Already chose directory'
            if(self.isRename.get() and self.isMakeZip.get()):
                rf.renameFiles(dir,fileName)
                mz.makeZipFiles(dir)
            elif(self.isRename.get() and not self.isMakeZip.get()):
                rf.renameFiles(dir,fileName)
            elif(self.isMakeZip.get() and not self.isRename.get()):
                mz.makeZipFiles(dir)
            else:
                mybutton['text'] = 'Please select at least one action'
                 
        self.button=mybutton = tk.Button(self, text='button', command=button_event)
        mybutton.pack()
if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
    
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='I love Python ')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         l.config(text='I love C++')
#     elif (var1.get() == 0) & (var2.get() == 0):
#         l.config(text='I do not anything')
#     else:
#         l.config(text='I love both')
 


    
    