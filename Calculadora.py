from tkinter import*

raiz=Tk()
raiz.title("Calculadora")
#raiz.config(width=300,height=300)
miFrame=Frame(raiz,width=200,height=600)
miFrame.pack(fill="both",expand=True)


miFrame.pack()
miLabel=Label(miFrame,text="ESTANDAR")
miLabel.place(x=5,y=100)
#Labels
#labelNombre=Label(miFrame,text="ESTANDAR")
#labelNombre.grid(row=0,column=0,pady=2)


entrada=Entry(miFrame)
entrada.grid(row=3,column=0,pady=20)


#nombre=Entry(miFrame)
#nombre.grid(row=0,column=1,pady=5)

#apellido=Entry(miFrame)
#apellido.grid(row=1,column=1,pady=5)

#direcccion=Entry(miFrame)
#direcccion.grid(row=2,column=1,pady=5)

# comentario=Entry(miFrame)
# comentario.grid(row=3,column=1,pady=5)

#passw=Entry(miFrame)
#passw.grid(row=4,column=1,pady=5)



#comentario=Text(miFrame,width=13,height=5)
#comentario.grid(row=3,column=1,pady=5)

raiz.mainloop()