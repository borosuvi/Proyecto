from tkinter import *

root=Tk()
miFrame=Frame(root,width=800,height=500)
miFrame.pack()
miLabel=Label(miFrame,text="Digite su nombre")
#miLabel.pack()
miLabel.place(x=150,y=435)
###imagen
miImagen=PhotoImage(file="ciber.gif")
milabel2=Label(miFrame,image=miImagen)
milabel2.place(x=100,y=50)
#root.mainloop()
##Cuadrsos de texto
cuadro1=Entry(miFrame)
cuadro1.place(x=150,y=460)
cuadro1.config(fg="red",justify="center")
root.mainloop()