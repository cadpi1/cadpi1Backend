from tkinter import *
from tkinter import ttk

## Only works if you have a desktop
def getUKCCredentialsDesktopVersion():
    window = Tk()
    window.title("Add UKC login credentials")
    window.geometry('325x250')
    window.configure(background = "gray")
    usernameLabel = Label(window ,text = "Username").grid(row = 0,column = 0)
    passwordLabel = Label(window ,text = "Password").grid(row = 1,column = 0)
    usernameEntry = Entry(window)
    usernameEntry.grid(row = 0,column = 1)
    passwordEntry = Entry(window)
    passwordEntry.grid(row = 1,column = 1)

    def onClick():
        f=open('./.env', 'a')
        env="UKCUsername="+usernameEntry.get() + "\n" + "UKCPassword="+passwordEntry.get()
        f.write(env)
        window.destroy()

    ttk.Button(window, text="Submit", command=onClick).grid()
    window.mainloop()

def getUKCCredentialsServerVersion():
    print("ukc username")
    username = input()
    print("password")
    password = input()

    f=open('./.env', 'a')
    env="UKCUsername="+username+"\n" + "UKCPassword="+password
    f.write(env)



