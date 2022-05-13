from gui import *

def main():
    """
    main class to have basic state of gui such as size, title, etc.
    """
    window = Tk()
    window.geometry('500x300')
    window.title('Weather Teller')
    window.resizable(False, False)

    widgets = gui(window)
    window.mainloop()


if __name__=='__main__':
    main()
