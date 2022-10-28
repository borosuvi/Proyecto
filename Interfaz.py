from tkinter import*
raiz=Tk()
raiz.title("Primera Ventana")
#raiz.config(width=300,height=300)
raiz.resizable(0,0)
raiz.iconbitmap("imagen.ico")
raiz.config(bg="blue")
raiz.geometry("600x350")
#Mi Frame
miFrame=Frame()
miFrame.pack(fill="both",expand=True)
miFrame.config(bg="red",width=100,height=100,bd=35)
raiz.mainloop()
