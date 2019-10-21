import tkinter as tk
from tkinter import ttk

class PythonTutorials(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container=ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}

        for F in (StartPage,String,List,Tuple,Set,Dictionary):
            page_name = F.__name__
            frame=F(parent=container, controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame= self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller= controller

        label = tk.Label(self, text="Python Tutorials", font=('arial',30, 'bold'))
        label.pack(side="top", fill="x", pady=10)

        ttk.Style().configure("TButton", padding=6, relief="flat",
                              background="#ccc",fg='blue')

        btnstring=ttk.Button(self, text="What is String in Python?",
                            command=lambda: controller.show_frame("String"))
        btnstring.pack()

        btnlist = ttk.Button(self, text="What is List in Python?",
                                 command=lambda: controller.show_frame("List"))
        btnlist.pack()

        btntuple = ttk.Button(self, text="What is Tuple in Python?",
                            command=lambda: controller.show_frame("Tuple"))
        btntuple.pack()

        btntset= ttk.Button(self, text="What is Set in Python?",
                              command=lambda: controller.show_frame("Set"))
        btntset.pack()

        btnDictionary = ttk.Button(self, text="What is Dictionary in Python?",
                             command=lambda: controller.show_frame("Dictionary"))
        btnDictionary.pack()


class String(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = ttk.Button(self, text="Go To Home Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        text2 = tk.Text(self, height=30, width=60)

        scroll = tk.Scrollbar(self, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))

        text2.insert(tk.END, '\tWhat is String in Python?\n', 'big')
        quote = """
        \tA string is a sequence of characters.
        A character is simply a symbol.For example, 
        the English language has 26 characters.
        Computers do not deal with characters, 
        they deal with numbers (binary). Even though
        you may see characters on your screen, 
        internally it is stored and manipulated 
        as a combination of 0's and 1's.
        This conversion of character to a number 
        is called encoding, and the reverse process 
        is decoding. ASCII and Unicode are some of 
        the popular encoding used.
        In Python, string is a sequence of Unicode character.
        Unicode was introduced to include every character in 
        all languages and bring uniformity in encoding.
        How to create a string in Python?
       
        my_string = 'Hello'
        print(my_string)
        
        How to access characters in a string?
        
        str = 'programiz'
        first character
        print(str[0])
        
        #slicing 2nd to 5th character
        print(str[1:5])

        """

        text2.insert(tk.END, quote, 'color')
        text2.config(state='disabled')
        text2.insert(tk.END, 'follow-up\n', 'follow')
        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)


class List(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = ttk.Button(self, text="Go To Home Page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

        text2 = tk.Text(self, height=30, width=60)

        scroll = tk.Scrollbar(self, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))

        text2.insert(tk.END, '\tWhat is List in Python?\n', 'big')
        quote = """
        \tList is a collection which is ordered and changeable. 
        Allows duplicate members. A list is a collection which is
        ordered and changeable. In Python lists are written with 
        square brackets.
        
        Example
        
        thislist = ["apple", "banana", "cherry"]
        print(thislist)
        
        You access the list items by referring to the index number:
        
        thislist = ["apple", "banana", "cherry"]
        print(thislist[1])
        
        Negative indexing means beginning from the end,-1 refers
        to the last item, -2 refers to the second last item etc.
        
        thislist = ["apple", "banana", "cherry"]
        print(thislist[-1])
        
        You can specify a range of indexes by specifying where 
        to start and where to end the range.
        When specifying a range, the return value will be a 
        new list with the specified items.
        
        thislist = ["apple", "banana", "cherry", "orange", 
        "kiwi", "melon", "mango"]
        print(thislist[2:5])

        """
        text2.insert(tk.END, quote, 'color')
        text2.config(state='disabled')
        text2.insert(tk.END, 'follow-up\n', 'follow')
        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)


class Tuple(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = ttk.Button(self, text="Go To Home Page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

        text2 = tk.Text(self, height=30, width=60)

        scroll = tk.Scrollbar(self, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))

        text2.insert(tk.END, '\tWhat is Tuple in Python?\n', 'big')
        quote = """
        \tA tuple is a collection which is ordered and 
        unchangeable. 
        In Python tuples are written with round brackets.
        
        Create a Tuple:
        
        thistuple = ("apple", "banana", "cherry")
        print(thistuple)
        
        You can access tuple items by referring to
        the index number,inside square brackets:
        
        Print the second item in the tuple:

        thistuple = ("apple", "banana", "cherry")
        print(thistuple[1])
        
        Negative indexing means beginning from the end, -1 
        refers to the last item, -2 refers to
        the second last item etc.
        
        thistuple = ("apple", "banana", "cherry")
        print(thistuple[-1])

        """
        text2.insert(tk.END, quote, 'color')
        text2.config(state='disabled')
        text2.insert(tk.END, 'follow-up\n', 'follow')
        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)


class Set(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = ttk.Button(self, text="Go To Home Page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

        text2 = tk.Text(self, height=30, width=60)

        scroll = tk.Scrollbar(self, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))

        text2.insert(tk.END, '\tWhat is Set in Python?\n', 'big')
        quote = """
        \tA set is a collection which is unordered and unindexed. 
        In Python sets are written with curly brackets.
        
        Example
        Create a Set:
        
        thisset = {"apple", "banana", "cherry"}
        print(thisset) 
        
        Loop through the set, and print the values:
        
        thisset = {"apple", "banana", "cherry"}

        for x in thisset:
            print(x) 
            
        Check if "banana" is present in the set:
        
        thisset = {"apple", "banana", "cherry"}

        print("banana" in thisset)

        """
        text2.insert(tk.END, quote, 'color')
        text2.config(state='disabled')
        text2.insert(tk.END, 'follow-up\n', 'follow')
        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)


class Dictionary(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = ttk.Button(self, text="Go To Home Page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

        text2 = tk.Text(self, height=30, width=60)

        scroll = tk.Scrollbar(self, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))

        text2.insert(tk.END, '\t\tWhat is Dictionary?\n', 'big')
        quote = """
        \tA dictionary is a collection which is unordered,
         changeable and indexed. In Python dictionaries are 
         written with curly brackets, and they 
         have keys and values.
         
         Example
         Create and print a dictionary
         
         thisdict = {
         "brand": "Ford",
         "model": "Mustang",
         "year": 1964 }
         
        print(thisdict)
        
        You can access the items of a dictionary by referring
        to its key name, inside square brackets:
        x = thisdict["model"]
        
        There is also a method called get() that will give you
        the same result:
        
        x = thisdict.get("model")

        """
        text2.insert(tk.END, quote, 'color')
        text2.config(state='disabled')
        text2.insert(tk.END, 'follow-up\n', 'follow')
        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

if __name__ == "__main__":
    app = PythonTutorials()
    app.title("Python Tutorials")
    #app.geometry("500x400")
    app.resizable(False,False)
    app.mainloop()