from gui import *

def main():
    window = Tk()
    window.geometry('300x300')
    window.title('Weather Teller')
    window.resizable(False, False)

    widgets = gui(window)
    window.mainloop()


if __name__=='__main__':
    main()
