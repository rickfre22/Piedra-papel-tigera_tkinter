from tkinter import *
import random
ventana_principal =Tk()
ventana_principal.title("Miguel Angel Galvis Quiñonez")
ventana_principal.geometry("600x400")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")
#variables de cpu

def piedra():
    n=0
    cpu = random.randint(1,3)
    if cpu == 1:
        t_resultado.insert(INSERT,"la cpu escogio piedra,¡empate!\n")
        
    if cpu == 2:
        t_resultado.insert(INSERT,"la cpu escogio tijera,¡ganaste!\n")
    if cpu == 3:
        t_resultado.insert(INSERT,"la cpu escogio papel,¡perdiste!\n")
    t_resultado.insert(INSERT,"borra el texto\n")
def papel():
    cpu = random.randint(1,3)
    if cpu == 1:
        t_resultado.insert(INSERT,"la cpu escogio piedra,¡ganas!\n")
    if cpu == 2:
        t_resultado.insert(INSERT,"la cpu escogio tijera,¡perdiste!\n")
    if cpu == 3:
        t_resultado.insert(INSERT,"la cpu escogio papel,¡empate!\n")
    t_resultado.insert(INSERT,"borra el texto\n")

def tijera():
    cpu = random.randint(1,3)
    if cpu == 1:
        t_resultado.insert(INSERT,"la cpu escogio piedra,¡perdiste!\n")
    if cpu == 2:
        t_resultado.insert(INSERT,"la cpu escogio tijera,¡empate!\n")
    if cpu == 3:
        t_resultado.insert(INSERT,"la cpu escogio papel,¡ganaste!\n")
    t_resultado.insert(INSERT,"borra el texto\n")
def borrar():
    t_resultado.delete("1.0","end")
frame_1=Frame(ventana_principal)
frame_1.config(bg="blue",width=780,height=580)
frame_1.place(x=10,y=10)
frame_2=Frame(ventana_principal)
frame_2.config(bg="lightblue",width=405,height=200)
frame_2.place(x=140,y=60)
# Etiqueta para sunbtitulo 1 de la app
subtitulo1 = Label(frame_1,text="papel,piedra o tigera")
subtitulo1.config(bg="blue",fg="black",font=("courier",20))
subtitulo1.place(x=5,y=5)

subtitulo1 = Label(frame_1,text="puntos:")
subtitulo1.config(bg="blue",fg="black",font=("courier",20))
subtitulo1.place(x=300,y=300)

subtitulo2= Label(frame_2,text="Respuesta del cpu.")
subtitulo2.config(bg="lightblue",fg="black",font=("courier",20))
subtitulo2.place(x=50,y=10)

img_bt_sumar =PhotoImage(file="img/papel.png")
bt_sumar  =Button(frame_1,image =img_bt_sumar,width=100,height=100,command=papel)
#bt_sumar = Button(frame_2, text="sumar",width=10)
bt_sumar.place(x=5,y=160)

img_bt_piedra =PhotoImage(file="img/piedra.png")
bt_piedra  =Button(frame_1,image =img_bt_piedra,width=100,height=100,command=piedra)
#bt_sumar = Button(frame_2, text="sumar",width=10)
bt_piedra.place(x=5,y=50)


img_bt_salir =PhotoImage(file="img/tigera.png")
bt_salir  =Button(frame_1,image =img_bt_salir,width=100,height=100,command=tijera)
#bt_sumar = Button(frame_2, text="sumar",width=10)
bt_salir.place(x=5,y=270)

#boton para borrar
img_bt_borrar =PhotoImage(file="img/recycle.png")
bt_borrar  =Button(frame_1,image =img_bt_borrar,width=100,height=100, command=borrar)
#bt_sumar = Button(frame_2, text="sumar",width=10)
bt_borrar.place(x=150,y=270)


frame_3= Frame(frame_2)
frame_3.config(bg="ivory2", width=200,height=10)
frame_3.place(x=1,y= 40)
#area de texto
t_resultado =Text(frame_3,width=33,height =7)
t_resultado.config(bg="lightblue",fg="white",font=("Courier",15))
t_resultado.pack()



ventana_principal.mainloop()