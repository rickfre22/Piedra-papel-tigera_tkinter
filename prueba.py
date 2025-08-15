from tkinter import *
from tkinter import messagebox
# -----------------------------------------------------
#funciones de la app
#------------------------------------------------------

def sumar():
    c = int(a.get()) + int(b.get())
    t_resultado.insert(INSERT,"La suma de "+ a.get() + "+" + b.get() + "casi siempre es " + str(c) + "\n")

def borrar():
    messagebox.showinfo("Suma 1.0","Los datos seran borrados...")
    a.set("")
    b.set("")
    t_resultado.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0","la app se cerrara...")
    ventana_principal.destroy()
    
#-----------------------------------------------------
# ventana principal
#------------------------------------------------------

# Se declara una variable llamada ventana_principal, que adquiere ls carcteristicas de un objeto de tipo TK()
ventana_principal = Tk()

#Titulo de la ventana
ventana_principal.title("Miguel Angel Galvis Quiñonez")

#Tamaño de laventana
ventana_principal.geometry("800x500")

#desavilitar boton maximizar
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------------
#variables globales
#----------------------------------
a = StringVar()
b = StringVar()
c = IntVar()
#_-------------------------
# frame 1 - entrada de datos
#--------------------------
frame_1= Frame(ventana_principal)
frame_1.config(bg="ivory2", width=780,height=240)
frame_1.place(x=10,y=10)

# imagen logo de la app
logo = PhotoImage(file="img/btn-suma.png")
Label_logo=Label(frame_1,image=logo)
Label_logo.place(x=10,y=10)
# etiqueta para el titulode la app
titulo = Label(frame_1,text=" Colegio San José de Guanenta")
titulo.config(bg="yellow", fg="blue",font=("arial",16))
titulo.place(x=390,y=10)
# Etiqueta para sunbtitulo 1 de la app
subtitulo1 = Label(frame_1,text="  Especialidad en sistemas")
subtitulo1.config(bg="yellow",fg="blue",font=("arial",12))
subtitulo1.place(x=390,y=40)
#Etiqueta subtitulo2
subtitulo2 = Label(frame_1,text="SUMA DE DOS ENTEROS")
subtitulo2.config(bg="ivory2",fg="blue",font=("arial",15),anchor=CENTER)
subtitulo2.place(x=390,y=70)
#Etiqueta el primer vaolr
label_a = Label(frame_1,text="a= ")
label_a.config(bg="ivory2",fg="blue",font=("arial",20),anchor=CENTER)
label_a.place(x=390,y=120)
#Etiqueta el primer valor
label_b = Label(frame_1,text="b= ")
label_b.config(bg="ivory2",fg="blue",font=("arial",20),anchor=CENTER)
label_b.place(x=585,y=120)

#Entry para el primer valor
entry_a =Entry(frame_1,width=4,textvariable=a)
entry_a.config(font=("arial", 20),justify=CENTER)
entry_a.focus_set()
entry_a.place(x=487,y= 120)
#Entry para el primer valor
entry_b =Entry(frame_1,width=4,textvariable=b)
entry_b.config(font=("arial", 20),justify=CENTER)
entry_b.place(x=682,y= 120)
#-------------------------
# frame 2 - panel de operaciones
#--------------------------
frame_2= Frame(ventana_principal)
frame_2.config(bg="ivory2", width=780,height=120)
frame_2.place(x=10,y=260)
#boton para sumar
img_bt_sumar =PhotoImage(file="img/boton_sumar.png")
bt_sumar  =Button(frame_2,image =img_bt_sumar,width=105,height=105,command=sumar)
#bt_sumar = Button(frame_2, text="sumar",width=10)
bt_sumar.place(x=116,y=7)

#boton para borrar
img_bt_borrar =PhotoImage(file="img/boton_borrar.png")
bt_borrar  =Button(frame_2,image =img_bt_borrar,width=105,height=105, command=borrar)
#bt_sumar = Button(frame_2, text="sumar",width=10)
bt_borrar.place(x=337,y=7)

#boton para salir
img_bt_salir =PhotoImage(file="img/boton_salir.png")
bt_salir  =Button(frame_2,image =img_bt_salir,width=105,height=105,command=salir)
#bt_sumar = Button(frame_2, text="sumar",width=10)
bt_salir.place(x=558,y=7)
#--------------------------
# frame 3 -Resultado
#--------------------------
frame_3= Frame(ventana_principal)
frame_3.config(bg="ivory2", width=780,height=100)
frame_3.place(x=10,y= 390)
#area de teto
t_resultado =Text(frame_3,width=50,height =3)
t_resultado.config(bg="green",fg="white",font=("Courier",20))
t_resultado.pack()

#Metodo principal quedespiega la ventana en pantalla
ventana_principal.mainloop()