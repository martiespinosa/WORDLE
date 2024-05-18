from tkinter import *
from tkinter.ttk import *
from customtkinter import *
from sqlite3 import *
import random
import datetime
import time
from PIL import Image

global palabraElejida
global paraulaUsuari

def validar_y_mover(event, entry_actual, entry_siguiente):
    if entry_actual != labelWordle and entry_siguiente != labelWordle and entry_actual.get() == "":
        entry_actual.focus_set()
    elif entry_actual != labelWordle and entry_siguiente != labelWordle and entry_actual.get() != "" and entry_siguiente.get() == "":
        entry_siguiente.focus_set()
        entry_siguiente = entry_actual
    elif entry_actual == labelWordle:
        labelWordle.focus_set()
        return False

   
    if solo_letras(event):
        entry_siguiente.focus_set()
        return solo_letras(event)
    return False

    
def lasQueNoEstan(entry_actual):
    for i in range(len(noEstan)):
        if entry_actual.get() == noEstan[i]:
            entry_actual.configure(border_color="brown1")


def borrar_y_mover(event, entry_actual, entry_anterior):
    if entry_actual != labelWordle and event.keysym == "BackSpace" and len(entry_actual.get()) == 0:
        entry_anterior.focus_set()
        entry_anterior.delete(0, END)
        entry_anterior.configure(border_color="#565b5e")
    elif entry_actual != labelWordle and event.keysym == "BackSpace" and len(entry_actual.get()) != 0:
        entry_actual.focus_set()
        entry_actual.delete(0, END)
        entry_actual.configure(border_color="#565b5e")
    elif entry_actual == labelWordle and event.keysym == "BackSpace":
        if entry_f1_c5.get() != "" and entry_f2_c5.get() == "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f1_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f2_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f3_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f4_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f5_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() != "":
            entry_anterior = entry_f6_c5

        entry_anterior.delete(0, END)
        entry_anterior.configure(border_color="#565b5e")
        entry_anterior.focus_set()








# ----------------------------------------------------------------


def check_fullscreen(root):
    # Obtener el estado de la ventana
    state = root.wm_state()
    # Verificar si la ventana está en modo de pantalla completa
    return (state == 'zoomed')

def update_ui(root):
    global paraulaUsuari 
    # labelLaPalabraEra = CTkLabel(master=app, text="NO HAS ACERTADO LA PALABRA DE HOY, LA PALABRA ERA:", justify=CENTER)
    # labelRespuesta = CTkLabel(master=app, text=f"{palabraElejida}", justify=CENTER)
    # Verificar si la ventana está en modo de pantalla completa
    if check_fullscreen(root):
        # Si está en pantalla completa:
        
        labelWordle.configure(font=("Dubai", 50, "bold"))
        labelWordle.place(relx=0.47, rely=0.1, anchor = CENTER)

        buttonIdioma.configure(font=("Dubai", 50, "bold"))
        buttonIdioma.place(relx=0.585, rely=0.1, anchor=CENTER)
        

        entry_f1_c1.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f1_c1.place(relx=0.38, rely=0.23, anchor = CENTER)

        entry_f1_c2.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f1_c2.place(relx=0.44, rely=0.23, anchor = CENTER)

        entry_f1_c3.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f1_c3.place(relx=0.5, rely=0.23, anchor = CENTER)

        entry_f1_c4.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f1_c4.place(relx=0.56, rely=0.23, anchor = CENTER)

        entry_f1_c5.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f1_c5.place(relx=0.62, rely=0.23, anchor = CENTER)


        entry_f2_c1.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f2_c1.place(relx=0.38, rely=0.34, anchor = CENTER)

        entry_f2_c2.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f2_c2.place(relx=0.44, rely=0.34, anchor = CENTER)

        entry_f2_c3.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f2_c3.place(relx=0.5, rely=0.34, anchor = CENTER)

        entry_f2_c4.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f2_c4.place(relx=0.56, rely=0.34, anchor = CENTER)

        entry_f2_c5.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f2_c5.place(relx=0.62, rely=0.34, anchor = CENTER)


        entry_f3_c1.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f3_c1.place(relx=0.38, rely=0.45, anchor = CENTER)

        entry_f3_c2.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f3_c2.place(relx=0.44, rely=0.45, anchor = CENTER)

        entry_f3_c3.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f3_c3.place(relx=0.5, rely=0.45, anchor = CENTER)

        entry_f3_c4.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f3_c4.place(relx=0.56, rely=0.45, anchor = CENTER)

        entry_f3_c5.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f3_c5.place(relx=0.62, rely=0.45, anchor = CENTER)


        entry_f4_c1.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f4_c1.place(relx=0.38, rely=0.56, anchor = CENTER)

        entry_f4_c2.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f4_c2.place(relx=0.44, rely=0.56, anchor = CENTER)

        entry_f4_c3.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f4_c3.place(relx=0.5, rely=0.56, anchor = CENTER)

        entry_f4_c4.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f4_c4.place(relx=0.56, rely=0.56, anchor = CENTER)

        entry_f4_c5.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f4_c5.place(relx=0.62, rely=0.56, anchor = CENTER)


        entry_f5_c1.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f5_c1.place(relx=0.38, rely=0.67, anchor = CENTER)

        entry_f5_c2.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f5_c2.place(relx=0.44, rely=0.67, anchor = CENTER)

        entry_f5_c3.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f5_c3.place(relx=0.5, rely=0.67, anchor = CENTER)

        entry_f5_c4.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f5_c4.place(relx=0.56, rely=0.67, anchor = CENTER)

        entry_f5_c5.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f5_c5.place(relx=0.62, rely=0.67, anchor = CENTER)


        entry_f6_c1.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f6_c1.place(relx=0.38, rely=0.78, anchor = CENTER)

        entry_f6_c2.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f6_c2.place(relx=0.44, rely=0.78, anchor = CENTER)

        entry_f6_c3.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f6_c3.place(relx=0.5, rely=0.78, anchor = CENTER)

        entry_f6_c4.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f6_c4.place(relx=0.56, rely=0.78, anchor = CENTER)

        entry_f6_c5.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entry_f6_c5.place(relx=0.62, rely=0.78, anchor = CENTER)


        labelContador.configure(font=("Dubai", 26, "bold"))


        # labelLaPalabraEra.configure(font=("Dubai", 22, "bold"))


        entryGameOver1.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entryGameOver1.place(relx=0.38, rely=0.56, anchor = CENTER)

        entryGameOver2.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entryGameOver2.place(relx=0.44, rely=0.56, anchor = CENTER)

        entryGameOver3.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entryGameOver3.place(relx=0.5, rely=0.56, anchor = CENTER)

        entryGameOver4.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)
        entryGameOver4.place(relx=0.56, rely=0.56, anchor = CENTER)

        entryGameOver5.configure(width=60, height=60, font=("Dubai", 30, "bold"), border_width=2)    
        entryGameOver5.place(relx=0.62, rely=0.56, anchor = CENTER)

        # labelNoHasAcertado.configure(font=("Dubai", 52, "bold"))
        # labelLaPalabraEra.configure(font=("Dubai", 48, "bold"))

        # if paraulaUsuari != palabraElejida and entry_f1_c1._border_color == "#2b2b2b":
        #     labelLaPalabraEra.configure(font=("Dubai", 13, "bold"))
        #     labelLaPalabraEra.place(relx=0.5, rely=0.4, anchor = CENTER)
        #     labelRespuesta.configure(font=("Dubai", 50, "bold"))
        #     labelRespuesta.place(relx=0.5, rely=0.5, anchor = CENTER)
    else:
        # Si no está en pantalla completa:
        
        labelWordle.configure(font=("Dubai", 33, "bold"))
        labelWordle.place(relx=0.42, rely=0.1, anchor = CENTER)

        buttonIdioma.configure(font=("Dubai", 33, "bold"))
        buttonIdioma.place(relx=0.72, rely=0.1, anchor=CENTER)


        entry_f1_c1.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f1_c1.place(relx=0.2, rely=0.25, anchor = CENTER)


        entry_f1_c2.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f1_c2.place(relx=0.35, rely=0.25, anchor = CENTER)

        entry_f1_c3.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f1_c3.place(relx=0.5, rely=0.25, anchor = CENTER)

        entry_f1_c4.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f1_c4.place(relx=0.65, rely=0.25, anchor = CENTER)

        entry_f1_c5.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f1_c5.place(relx=0.8, rely=0.25, anchor = CENTER)


        entry_f2_c1.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f2_c1.place(relx=0.2, rely=0.35, anchor = CENTER)

        entry_f2_c2.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f2_c2.place(relx=0.35, rely=0.35, anchor = CENTER)

        entry_f2_c3.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f2_c3.place(relx=0.5, rely=0.35, anchor = CENTER)

        entry_f2_c4.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f2_c4.place(relx=0.65, rely=0.35, anchor = CENTER)

        entry_f2_c5.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f2_c5.place(relx=0.8, rely=0.35, anchor = CENTER)


        entry_f3_c1.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f3_c1.place(relx=0.2, rely=0.45, anchor = CENTER)

        entry_f3_c2.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f3_c2.place(relx=0.35, rely=0.45, anchor = CENTER)

        entry_f3_c3.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f3_c3.place(relx=0.5, rely=0.45, anchor = CENTER)

        entry_f3_c4.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f3_c4.place(relx=0.65, rely=0.45, anchor = CENTER)

        entry_f3_c5.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f3_c5.place(relx=0.8, rely=0.45, anchor = CENTER)


        entry_f4_c1.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f4_c1.place(relx=0.2, rely=0.55, anchor = CENTER)

        entry_f4_c2.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f4_c2.place(relx=0.35, rely=0.55, anchor = CENTER)

        entry_f4_c3.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f4_c3.place(relx=0.5, rely=0.55, anchor = CENTER)

        entry_f4_c4.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f4_c4.place(relx=0.65, rely=0.55, anchor = CENTER)

        entry_f4_c5.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f4_c5.place(relx=0.8, rely=0.55, anchor = CENTER)


        entry_f5_c1.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f5_c1.place(relx=0.2, rely=0.65, anchor = CENTER)

        entry_f5_c2.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f5_c2.place(relx=0.35, rely=0.65, anchor = CENTER)

        entry_f5_c3.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f5_c3.place(relx=0.5, rely=0.65, anchor = CENTER)

        entry_f5_c4.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f5_c4.place(relx=0.65, rely=0.65, anchor = CENTER)

        entry_f5_c5.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f5_c5.place(relx=0.8, rely=0.65, anchor = CENTER)


        entry_f6_c1.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f6_c1.place(relx=0.2, rely=0.75, anchor = CENTER)

        entry_f6_c2.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f6_c2.place(relx=0.35, rely=0.75, anchor = CENTER)

        entry_f6_c3.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f6_c3.place(relx=0.5, rely=0.75, anchor = CENTER)

        entry_f6_c4.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f6_c4.place(relx=0.65, rely=0.75, anchor = CENTER)

        entry_f6_c5.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entry_f6_c5.place(relx=0.8, rely=0.75, anchor = CENTER)


        labelContador.configure(font=("Dubai", 17, "bold"))


        # labelLaPalabraEra.configure(font=("Dubai", 13, "bold"))


        entryGameOver1.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entryGameOver1.place(relx=0.2, rely=0.55, anchor = CENTER)

        entryGameOver2.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entryGameOver2.place(relx=0.35, rely=0.55, anchor = CENTER)

        entryGameOver3.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entryGameOver3.place(relx=0.5, rely=0.55, anchor = CENTER)

        entryGameOver4.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entryGameOver4.place(relx=0.65, rely=0.55, anchor = CENTER)

        entryGameOver5.configure(width=40, height=40, font=("Dubai", 20, "bold"), border_width=1)
        entryGameOver5.place(relx=0.8, rely=0.55, anchor = CENTER)

        # labelNoHasAcertado.configure(font=("Dubai", 44, "bold"))
        # labelLaPalabraEra.configure(font=("Dubai", 31, "bold"))
        
        # if paraulaUsuari != palabraElejida and entry_f1_c1._border_color == "#2b2b2b":
        #     labelLaPalabraEra.configure(font=("Dubai", 10, "bold"))
        #     labelLaPalabraEra.place(relx=0.5, rely=0.4, anchor = CENTER)
        #     labelRespuesta.configure(font=("Dubai", 33, "bold"))
        #     labelRespuesta.place(relx=0.5, rely=0.5, anchor = CENTER)

    # Programar la siguiente actualización de la interfaz de usuario
    root.after(250, update_ui, root)



# ----------------------------------------------------------------
noEstan = []

def enter(event, entry_actual, entry_siguiente, entry_f1_c1, entry_f1_c2, entry_f1_c3, entry_f1_c4, entry_f1_c5, entry_f2_c1, entry_f2_c2, entry_f2_c3, entry_f2_c4, entry_f2_c5, entry_f3_c1, entry_f3_c2, entry_f3_c3, entry_f3_c4, entry_f3_c5, entry_f4_c1, entry_f4_c2, entry_f4_c3, entry_f4_c4, entry_f4_c5, entry_f5_c1, entry_f5_c2, entry_f5_c3, entry_f5_c4, entry_f5_c5, entry_f6_c1, entry_f6_c2, entry_f6_c3, entry_f6_c4, entry_f6_c5):
    global palabraElejida
    global paraulaUsuari
    global noEstan
    if entry_actual == labelWordle and event.keysym == "Return":
        global AA
        AA = 0
        global BB
        BB = 0
        global CC
        CC = 0
        global DD
        DD = 0
        global EE
        EE = 0
        global FF
        FF = 0
        global GG
        GG = 0
        global HH
        HH = 0
        global II
        II = 0
        global JJ
        JJ = 0
        global KK
        KK = 0
        global LL
        LL = 0
        global MM
        MM = 0
        global NN
        NN = 0
        global ÑÑ
        ÑÑ = 0
        global OO
        OO = 0
        global PP
        PP = 0
        global QQ
        QQ = 0
        global RR
        RR = 0
        global SS
        SS = 0
        global TT
        TT = 0
        global UU
        UU = 0
        global VV
        VV = 0
        global WW
        WW = 0
        global XX
        XX = 0
        global YY
        YY = 0
        global ZZ
        ZZ = 0

        for y in range(5):
            if palabraElejida[y] == "A":
                AA += 1
            if palabraElejida[y] == "B":
                BB += 1
            if palabraElejida[y] == "C":
                CC += 1
            if palabraElejida[y] == "D":
                DD += 1
            if palabraElejida[y] == "E":
                EE += 1
            if palabraElejida[y] == "F":
                FF += 1
            if palabraElejida[y] == "G":
                GG += 1
            if palabraElejida[y] == "H":
                HH += 1
            if palabraElejida[y] == "I":
                II += 1
            if palabraElejida[y] == "J":
                JJ += 1
            if palabraElejida[y] == "K":
                KK += 1
            if palabraElejida[y] == "L":
                LL += 1
            if palabraElejida[y] == "M":
                MM += 1
            if palabraElejida[y] == "N":
                NN += 1
            if palabraElejida[y] == "Ñ":
                ÑÑ += 1
            if palabraElejida[y] == "O":
                OO += 1
            if palabraElejida[y] == "P":
                PP += 1
            if palabraElejida[y] == "Q":
                QQ += 1
            if palabraElejida[y] == "R":
                RR += 1
            if palabraElejida[y] == "S":
                SS += 1
            if palabraElejida[y] == "T":
                TT += 1
            if palabraElejida[y] == "U":
                UU += 1
            if palabraElejida[y] == "V":
                VV += 1
            if palabraElejida[y] == "W":
                WW += 1
            if palabraElejida[y] == "X":
                XX += 1
            if palabraElejida[y] == "Y":
                YY += 1
            if palabraElejida[y] == "Z":
                ZZ += 1


        miConexion = connect(bbdd10k)
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT PALABRA FROM PALABRAS")
        
        todasLasPalabras = miCursor.fetchall()
        
        miCursor.execute("SELECT MAX(id) FROM PALABRAS")
        global numeroPalabrasTotal
        numeroPalabrasTotal = miCursor.fetchone()[0]
                                    
        miConexion.commit()
        miConexion.close()

    
    
        if entry_f1_c5.get() != "" and entry_f2_c5.get() == "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            global paraulaUsuari
            paraulaUsuari = entry_f1_c1.get() + entry_f1_c2.get() + entry_f1_c3.get() + entry_f1_c4.get() + entry_f1_c5.get()
            listaEntrys = [entry_f1_c1, entry_f1_c2, entry_f1_c3, entry_f1_c4, entry_f1_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            paraulaUsuari = entry_f2_c1.get() + entry_f2_c2.get() + entry_f2_c3.get() + entry_f2_c4.get() + entry_f2_c5.get()
            listaEntrys = [entry_f2_c1, entry_f2_c2, entry_f2_c3, entry_f2_c4, entry_f2_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            paraulaUsuari = entry_f3_c1.get() + entry_f3_c2.get() + entry_f3_c3.get() + entry_f3_c4.get() + entry_f3_c5.get()
            listaEntrys = [entry_f3_c1, entry_f3_c2, entry_f3_c3, entry_f3_c4, entry_f3_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            paraulaUsuari = entry_f4_c1.get() + entry_f4_c2.get() + entry_f4_c3.get() + entry_f4_c4.get() + entry_f4_c5.get()
            listaEntrys = [entry_f4_c1, entry_f4_c2, entry_f4_c3, entry_f4_c4, entry_f4_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() == "":
            paraulaUsuari = entry_f5_c1.get() + entry_f5_c2.get() + entry_f5_c3.get() + entry_f5_c4.get() + entry_f5_c5.get()
            listaEntrys = [entry_f5_c1, entry_f5_c2, entry_f5_c3, entry_f5_c4, entry_f5_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() != "":
            paraulaUsuari = entry_f6_c1.get() + entry_f6_c2.get() + entry_f6_c3.get() + entry_f6_c4.get() + entry_f6_c5.get()
            listaEntrys = [entry_f6_c1, entry_f6_c2, entry_f6_c3, entry_f6_c4, entry_f6_c5]
        
            # for i in range(5):
            #     listaEntrys[i].configure(state="disabled")

            for i in range(int(numeroPalabrasTotal)):
                todasLasPalabrasDeUnaEnUna = todasLasPalabras[i][0]
                if paraulaUsuari == todasLasPalabrasDeUnaEnUna:
                    if paraulaUsuari != palabraElejida:
                        app.after(1000, gameOver)
                        


        if paraulaUsuari == palabraElejida:
            for i in range(5):
                listaEntrys[i].configure(state="disabled")

        
        for i in range(int(numeroPalabrasTotal)):
            todasLasPalabrasDeUnaEnUna = todasLasPalabras[i][0]
            if paraulaUsuari == todasLasPalabrasDeUnaEnUna:
                
                # GRISES
                for w in range(5):
                    listaEntrys[w].configure(fg_color="#757575")

                # VERDES
                for w in range(5):
                    if paraulaUsuari[w] == palabraElejida[w]:
                        listaEntrys[w].configure(fg_color="#43a047")
                        if listaEntrys[w].get() == "A":
                            AA -= 1
                        if listaEntrys[w].get() == "B":
                            BB -= 1
                        if listaEntrys[w].get() == "C":
                            CC -= 1
                        if listaEntrys[w].get() == "D":
                            DD -= 1
                        if listaEntrys[w].get() == "E":
                            EE -= 1
                        if listaEntrys[w].get() == "F":
                            FF -= 1
                        if listaEntrys[w].get() == "G":
                            GG -= 1
                        if listaEntrys[w].get() == "H":
                            HH -= 1
                        if listaEntrys[w].get() == "I":
                            II -= 1
                        if listaEntrys[w].get() == "J":
                            JJ -= 1
                        if listaEntrys[w].get() == "K":
                            KK -= 1
                        if listaEntrys[w].get() == "L":
                            LL -= 1
                        if listaEntrys[w].get() == "M":
                            MM -= 1
                        if listaEntrys[w].get() == "N":
                            NN -= 1
                        if listaEntrys[w].get() == "Ñ":
                            ÑÑ -= 1
                        if listaEntrys[w].get() == "O":
                            OO -= 1
                        if listaEntrys[w].get() == "P":
                            PP -= 1
                        if listaEntrys[w].get() == "Q":
                            QQ -= 1
                        if listaEntrys[w].get() == "R":
                            RR -= 1
                        if listaEntrys[w].get() == "S":
                            SS -= 1
                        if listaEntrys[w].get() == "T":
                            TT -= 1
                        if listaEntrys[w].get() == "U":
                            UU -= 1
                        if listaEntrys[w].get() == "V":
                            VV -= 1
                        if listaEntrys[w].get() == "W":
                            WW -= 1
                        if listaEntrys[w].get() == "X":
                            XX -= 1
                        if listaEntrys[w].get() == "Y":
                            YY -= 1
                        if listaEntrys[w].get() == "Z":
                            ZZ -= 1
                        
                # AMARILLAS
                for w in range(5):
                    if paraulaUsuari[w] != palabraElejida[w] and (paraulaUsuari[w] == palabraElejida[0] or paraulaUsuari[w] == palabraElejida[1] or paraulaUsuari[w] == palabraElejida[2] or paraulaUsuari[w] == palabraElejida[3] or paraulaUsuari[w] == palabraElejida[4]):
                        if paraulaUsuari[w] == "A":
                            if AA > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                AA -= 1
                        if paraulaUsuari[w] == "B":
                            if BB > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                BB -= 1
                        if paraulaUsuari[w] == "C":
                            if CC > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                CC -= 1
                        if paraulaUsuari[w] == "D":
                            if DD > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                DD -= 1
                        if paraulaUsuari[w] == "E":
                            if EE > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                EE -= 1
                        if paraulaUsuari[w] == "F":
                            if FF > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                FF -= 1
                        if paraulaUsuari[w] == "G":
                            if GG > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                GG -= 1
                        if paraulaUsuari[w] == "H":
                            if HH > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                HH -= 1
                        if paraulaUsuari[w] == "I":
                            if II > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                II -= 1
                        if paraulaUsuari[w] == "J":
                            if JJ > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                JJ -= 1
                        if paraulaUsuari[w] == "K":
                            if KK > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                KK -= 1
                        if paraulaUsuari[w] == "L":
                            if LL > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                LL -= 1
                        if paraulaUsuari[w] == "M":
                            if MM > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                MM -= 1
                        if paraulaUsuari[w] == "N":
                            if NN > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                NN -= 1
                        if paraulaUsuari[w] == "Ñ":
                            if ÑÑ > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                ÑÑ -= 1
                        if paraulaUsuari[w] == "O":
                            if OO > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                OO -= 1
                        if paraulaUsuari[w] == "P":
                            if PP > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                PP -= 1
                        if paraulaUsuari[w] == "Q":
                            if QQ > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                QQ -= 1
                        if paraulaUsuari[w] == "R":
                            if RR > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                RR -= 1
                        if paraulaUsuari[w] == "S":
                            if SS > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                SS -= 1
                        if paraulaUsuari[w] == "T":
                            if TT > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                TT -= 1
                        if paraulaUsuari[w] == "U":
                            if UU > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                UU -= 1
                        if paraulaUsuari[w] == "V":
                            if VV > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                VV -= 1
                        if paraulaUsuari[w] == "W":
                            if WW > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                WW -= 1
                        if paraulaUsuari[w] == "X":
                            if XX > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                XX -= 1
                        if paraulaUsuari[w] == "Y":
                            if YY > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                YY -= 1
                        if paraulaUsuari[w] == "Z":
                            if ZZ > 0:
                                listaEntrys[w].configure(fg_color="#e4a81d")
                                ZZ -= 1
                
                
                                    

                # LAS QUE NO ESTÁN
                for w in range(5):
                    if paraulaUsuari[w] != palabraElejida[0] and paraulaUsuari[w] != palabraElejida[1] and paraulaUsuari[w] != palabraElejida[2] and paraulaUsuari[w] != palabraElejida[3] and paraulaUsuari[w] != palabraElejida[4]:
                        noEstan.append(listaEntrys[w].get())
                    
                        listaEntrys[w].configure(border_color="#565b5e")
                

                
                



                # pasar a la siguiente linea
                if paraulaUsuari != palabraElejida:
                    if entry_f1_c5.get() != "" and entry_f2_c5.get() == "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
                        entry_siguiente = entry_f2_c1
                    elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
                        entry_siguiente = entry_f3_c1
                    elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
                        entry_siguiente = entry_f4_c1
                    elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
                        entry_siguiente = entry_f5_c1
                    elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() == "":
                        entry_siguiente = entry_f6_c1
                    elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() != "":
                        return False
                else:
                    entry_siguiente = labelWordle  

                entry_siguiente.focus_set()
                


 # PASAR A MAYUSCULAS
def convertir_a_mayusculas(event):
    # Obtener el widget que generó el evento
    widget = event.widget
    # Obtener el texto actual del widget
    texto_actual = widget.get()
    # Verificar si el texto está en minúsculas
    if texto_actual.islower():
        # Convertir el texto a mayúsculas
        texto_nuevo = texto_actual.upper()
        # Reemplazar el texto actual por el texto en mayúsculas
        widget.delete(0, END)
        widget.insert(0, texto_nuevo)


bbdd1k = (r"WORDLE\BBDD\PALABRAS_WORDLE_1K")
bbdd10k = (r"WORDLE\BBDD\PALABRAS_WORDLE_10K")

idiomaActual = "Español"
listaIdiomas = ["Español", "Català", "English"]
idiomaIndex = 0
def cambiarIdioma():
    if entry_f1_c1.get() == "":
        global idiomaIndex, idiomaActual, bbdd1k, bbdd10k, palabraElejida, palabraElejida1, palabraElejida2, palabraElejida3
        idiomaIndex = (idiomaIndex + 1) % len(listaIdiomas)
        idiomaActual = listaIdiomas[idiomaIndex]
        if idiomaActual == "Español":
            buttonIdioma.configure(text = "ES")
            bbdd1k = (r"WORDLE\BBDD\PALABRAS_WORDLE_1K")
            bbdd10k = (r"WORDLE\BBDD\PALABRAS_WORDLE_10K")
            palabraElejida = palabraElejida1
        elif idiomaActual == "Català":
            buttonIdioma.configure(text = "CA")
            bbdd1k = (r"WORDLE\BBDD\PARAULES_WORDLE_1K")
            bbdd10k = (r"WORDLE\BBDD\PARAULES_WORDLE_10K")
            palabraElejida = palabraElejida2
        elif idiomaActual == "English":
            buttonIdioma.configure(text = "EN")
            bbdd1k = (r"WORDLE\BBDD\WORDS_WORDLE_1K")
            bbdd10k = (r"WORDLE\BBDD\WORDS_WORDLE_10K")
            palabraElejida = palabraElejida3


def elegir_palabra_aleatoria():
    miConexion1 = connect(r"WORDLE\BBDD\PALABRAS_WORDLE_1K")
    miCursor1 = miConexion1.cursor()
    miCursor1.execute("SELECT PALABRA FROM PALABRAS ORDER BY RANDOM() LIMIT 1")
    global palabraElejida1
    palabraElejida1 = miCursor1.fetchone()[0]
    print(palabraElejida1)
    miConexion1.close()

    miConexion2 = connect(r"WORDLE\BBDD\PARAULES_WORDLE_1K")
    miCursor2 = miConexion2.cursor()
    miCursor2.execute("SELECT PALABRA FROM PALABRAS ORDER BY RANDOM() LIMIT 1")
    global palabraElejida2
    palabraElejida2 = miCursor2.fetchone()[0]
    print(palabraElejida2)
    miConexion2.close()

    miConexion3 = connect(r"WORDLE\BBDD\WORDS_WORDLE_1K")
    miCursor3 = miConexion3.cursor()
    miCursor3.execute("SELECT PALABRA FROM PALABRAS ORDER BY RANDOM() LIMIT 1")
    global palabraElejida3
    palabraElejida3 = miCursor3.fetchone()[0]
    print(palabraElejida3)
    miConexion3.close()






def gameOver():
    global listatodoslosentry
    for entry in listatodoslosentry:
        entry.configure(fg_color="#2b2b2b", bg_color="#2b2b2b", border_color="#2b2b2b", text_color="#2b2b2b")

    labelWordle.configure(text_color="#2b2b2b")
    buttonIdioma.configure(text_color="#2b2b2b")

    if idiomaActual == "Español":
        global labelNoHasAcertado
        labelNoHasAcertado = CTkLabel(master=app, text="GAME OVER", font=("Dubai", 44, "bold"), justify=CENTER)
        global labelLaPalabraEra
        labelLaPalabraEra = CTkLabel(master=app, text="LA PALABRA ERA:", font=("Dubai", 31, "bold"), justify=CENTER)
    elif idiomaActual == "Català":
        labelNoHasAcertado = CTkLabel(master=app, text="GAME OVER", font=("Dubai", 44, "bold"), justify=CENTER)
        labelLaPalabraEra = CTkLabel(master=app, text="LA PARAULA ERA:", font=("Dubai", 31, "bold"), justify=CENTER)
    elif idiomaActual == "English":
        labelNoHasAcertado = CTkLabel(master=app, text="GAME OVER", font=("Dubai", 44, "bold"), justify=CENTER)
        labelLaPalabraEra = CTkLabel(master=app, text="THE WORD WAS:", font=("Dubai", 31, "bold"), justify=CENTER)

    labelNoHasAcertado.place(relx=0.5, rely=0.1, anchor=CENTER)
    labelLaPalabraEra.place(relx=0.5, rely=0.45, anchor=CENTER)
  
    global entryGameOver1
    entryGameOver1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), border_width=1, insertontime=0, takefocus=False, justify=CENTER)
    global entryGameOver2
    entryGameOver2 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), border_width=1, insertontime=0, takefocus=False, justify=CENTER)
    global entryGameOver3
    entryGameOver3 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), border_width=1, insertontime=0, takefocus=False, justify=CENTER)
    global entryGameOver4
    entryGameOver4 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), border_width=1, insertontime=0, takefocus=False, justify=CENTER)
    global entryGameOver5
    entryGameOver5 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), border_width=1, insertontime=0, takefocus=False, justify=CENTER)

    entryGameOver1.place(relx=0.2, rely=0.55, anchor=CENTER)
    entryGameOver2.place(relx=0.35, rely=0.55, anchor=CENTER)
    entryGameOver3.place(relx=0.5, rely=0.55, anchor=CENTER)
    entryGameOver4.place(relx=0.65, rely=0.55, anchor=CENTER)
    entryGameOver5.place(relx=0.8, rely=0.55, anchor=CENTER)

    app.after(1000, lambda: entryGameOver1.insert(0, palabraElejida[0]))
    app.after(1400, lambda: entryGameOver2.insert(0, palabraElejida[1]))
    app.after(1800, lambda: entryGameOver3.insert(0, palabraElejida[2]))
    app.after(2200, lambda: entryGameOver4.insert(0, palabraElejida[3]))
    app.after(2600, lambda: entryGameOver5.insert(0, palabraElejida[4]))

    app.after(3000, lambda: entryGameOver1.configure(fg_color="#43a047"))
    app.after(3000, lambda: entryGameOver2.configure(fg_color="#43a047"))
    app.after(3000, lambda: entryGameOver3.configure(fg_color="#43a047"))
    app.after(3000, lambda: entryGameOver4.configure(fg_color="#43a047"))
    app.after(3000, lambda: entryGameOver5.configure(fg_color="#43a047"))
        
    labelNuevaPalabraEn = CTkLabel(master=app, text="NUEVA PALABRA EN:", font=("Dubai", 13, "bold"), justify=CENTER)



def actualizar_contador():
    # Obtener la fecha y hora actual
    tiempo_actual = time.localtime()
    hora_actual = tiempo_actual.tm_hour
    minuto_actual = tiempo_actual.tm_min
    segundo_actual = tiempo_actual.tm_sec

    # Calcular los segundos restantes hasta la medianoche
    segundos_restantes = (23 - hora_actual) * 3600 + (59 - minuto_actual) * 60 + (60 - segundo_actual)

    # Actualizar el contador
    horas = segundos_restantes // 3600
    minutos = (segundos_restantes % 3600) // 60
    segundos = segundos_restantes % 60

    if idiomaActual == "Español":
        formato_contador = "PRÓXIMA PALABRA EN: {:02d}:{:02d}:{:02d}"
    elif idiomaActual == "Català":
        formato_contador = "PRÒXIMA PARAULA EN: {:02d}:{:02d}:{:02d}"
    elif idiomaActual == "English":
        formato_contador = "NEXT WORD IN: {:02d}:{:02d}:{:02d}"

    contador = formato_contador.format(horas, minutos, segundos)
    labelContador.configure(text=contador)

    if segundos_restantes > 0:
        # Programar la próxima actualización después de 1 segundo
        app.after(1000, actualizar_contador)


# ----------------------------------------------------------------










# Obtener la fecha actual
fecha_actual = datetime.datetime.now().date()

print(fecha_actual)

miConexion1 = connect(r"WORDLE\BBDD\PALABRAS_WORDLE_1K")
miCursor1 = miConexion1.cursor()
miCursor1.execute("SELECT FECHA FROM FECHAS WHERE ID = 1")
ultima_fecha1 = miCursor1.fetchone()[0]

miConexion2 = connect(r"WORDLE\BBDD\PARAULES_WORDLE_1K")
miCursor2 = miConexion2.cursor()
miCursor2.execute("SELECT FECHA FROM FECHAS WHERE ID = 1")
ultima_fecha2 = miCursor2.fetchone()[0]

miConexion3 = connect(r"WORDLE\BBDD\WORDS_WORDLE_1K")
miCursor3 = miConexion3.cursor()
miCursor3.execute("SELECT FECHA FROM FECHAS WHERE ID = 1")
ultima_fecha3 = miCursor3.fetchone()[0]



if str(fecha_actual) != str(ultima_fecha1) or str(fecha_actual) != str(ultima_fecha2) or str(fecha_actual) != str(ultima_fecha3):
    elegir_palabra_aleatoria()
    if str(fecha_actual) != str(ultima_fecha1):
        miCursor1.execute("UPDATE FECHAS SET FECHA = ? WHERE ID = ?", (fecha_actual,1))
        miCursor1.execute("UPDATE FECHAS SET PALABRA = ? WHERE ID = ?", (palabraElejida1,1))
        miConexion1.commit()
        miConexion1.close()
        ultima_fecha1 = fecha_actual
    if str(fecha_actual) != str(ultima_fecha2):
        miCursor2.execute("UPDATE FECHAS SET FECHA = ? WHERE ID = ?", (fecha_actual,1))
        miCursor2.execute("UPDATE FECHAS SET PALABRA = ? WHERE ID = ?", (palabraElejida2,1))
        miConexion2.commit()
        miConexion2.close()
        ultima_fecha2 = fecha_actual
    if str(fecha_actual) != str(ultima_fecha3):
        miCursor3.execute("UPDATE FECHAS SET FECHA = ? WHERE ID = ?", (fecha_actual,1))
        miCursor3.execute("UPDATE FECHAS SET PALABRA = ? WHERE ID = ?", (palabraElejida3,1))
        miConexion3.commit()
        miConexion3.close()
        ultima_fecha = fecha_actual
else:
    miCursor1.execute("SELECT PALABRA FROM FECHAS WHERE ID = 1")
    palabraElejida1 = miCursor1.fetchone()[0]
    miConexion1.commit()
    miConexion1.close()
    print(palabraElejida1)
    ultima_fecha = ultima_fecha1
    
    miCursor2.execute("SELECT PALABRA FROM FECHAS WHERE ID = 1")
    palabraElejida2 = miCursor2.fetchone()[0]
    miConexion2.commit()
    miConexion2.close()
    print(palabraElejida2)
    ultima_fecha = ultima_fecha2

    miCursor3.execute("SELECT PALABRA FROM FECHAS WHERE ID = 1")
    palabraElejida3 = miCursor3.fetchone()[0]
    miConexion3.commit()
    miConexion3.close()
    print(palabraElejida3)
    ultima_fecha = ultima_fecha3


# if str(fecha_actual) != str(ultima_fecha2):
#     elegir_palabra_aleatoria()
#     miCursor2.execute("UPDATE FECHAS SET FECHA = ? WHERE ID = ?", (fecha_actual,1))
#     miCursor2.execute("UPDATE FECHAS SET PALABRA = ? WHERE ID = ?", (palabraElejida2,1))
#     miConexion2.commit()
#     miConexion2.close()
#     ultima_fecha2 = fecha_actual
# else:
#     miCursor2.execute("SELECT PALABRA FROM FECHAS WHERE ID = 1")
#     palabraElejida2 = miCursor2.fetchone()[0]
#     miConexion2.commit()
#     miConexion2.close()
#     print(palabraElejida2)
#     ultima_fecha = ultima_fecha2
    

# if str(fecha_actual) != str(ultima_fecha3):
#     elegir_palabra_aleatoria()
#     miCursor3.execute("UPDATE FECHAS SET FECHA = ? WHERE ID = ?", (fecha_actual,1))
#     miCursor3.execute("UPDATE FECHAS SET PALABRA = ? WHERE ID = ?", (palabraElejida3,1))
#     miConexion3.commit()
#     miConexion3.close()
#     ultima_fecha3 = fecha_actual
# else:
#     miCursor3.execute("SELECT PALABRA FROM FECHAS WHERE ID = 1")
#     palabraElejida3 = miCursor3.fetchone()[0]
#     miConexion3.commit()
#     miConexion3.close()
#     print(palabraElejida3)
#     ultima_fecha = ultima_fecha3
    

palabraElejida = palabraElejida1
ultima_fecha = ultima_fecha1


root = CTk()
root.title("WORDLE BY MARTIN")
root.geometry("350x500")
# root.resizable(0, 0)
# root.iconbitmap(r"C:\Users\MARTI\OneDrive\Documentos\Carpeta Principal\PYTHON\INTERFACES GRÁFICAS\python_xuVsziQBJR.ico")

# Obtenemos el largo y ancho de la pantalla
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
# Guardamos el largo y alto de la ventana
wventana = 350
hventana = 500
# Calculamos la posición central de la pantalla
pwidth = wtotal / 2
pheight = htotal / 2
# Calculamos los márgenes dinámicos de la ventana en x e y
x_margin = round(wventana / 2) - (17/100) * wtotal  # agrego  "- (17/100) * wtotal" para que realmente quede centrado
y_margin = round(hventana / 2) - (4/100) * htotal  # agrego  "- (4/100) * htotal" para que realmente quede centrado
# Calculamos la posición de la ventana
x = round(pwidth - x_margin)
y = round(pheight - y_margin)
# Se lo aplicamos a la geometría de la ventana
root.geometry("{}x{}+{}+{}".format(wventana, hventana, x, y))



app = CTkFrame(master = root)
app.pack(fill=BOTH, expand=1)
    

labelContador = CTkLabel(master=app, font=("Dubai", 17, "bold"), text_color="grey")
labelContador.place(relx=0.5, rely=0.9, anchor=CENTER)
actualizar_contador()



def set_focus():
    entry_f1_c1.focus()
app.after(100, set_focus)

    

# DECLARAR VARIABLES STRING
solo_letras = lambda text: text.isalpha()
var_f1_c1 = StringVar()
var_f1_c2 = StringVar()
var_f1_c3 = StringVar()
var_f1_c4 = StringVar()
var_f1_c5 = StringVar()

var_f2_c1 = StringVar()
var_f2_c2 = StringVar()
var_f2_c3 = StringVar()
var_f2_c4 = StringVar()
var_f2_c5 = StringVar()

var_f3_c1 = StringVar()
var_f3_c2 = StringVar()
var_f3_c3 = StringVar()
var_f3_c4 = StringVar()
var_f3_c5 = StringVar()

var_f4_c1 = StringVar()
var_f4_c2 = StringVar()
var_f4_c3 = StringVar()
var_f4_c4 = StringVar()
var_f4_c5 = StringVar()

var_f5_c1 = StringVar()
var_f5_c2 = StringVar()
var_f5_c3 = StringVar()
var_f5_c4 = StringVar()
var_f5_c5 = StringVar()

var_f6_c1 = StringVar()
var_f6_c2 = StringVar()
var_f6_c3 = StringVar()
var_f6_c4 = StringVar()
var_f6_c5 = StringVar()

# ----------------------------------------------------------------


entryGameOver1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), insertontime=0, takefocus=False, justify=CENTER)
entryGameOver2 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), insertontime=0, takefocus=False, justify=CENTER)
entryGameOver3 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), insertontime=0, takefocus=False, justify=CENTER)
entryGameOver4 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), insertontime=0, takefocus=False, justify=CENTER)
entryGameOver5 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), insertontime=0, takefocus=False, justify=CENTER)


# -----------------------------------------------------------------



# -------------------------------------------------------------------------------------------

buttonIdioma = CTkButton(master = app, width=30, height=30, text = "ES", anchor=CENTER, fg_color="transparent", hover=False, cursor="hand2", command=cambiarIdioma)


labelWordle = CTkLabel(master=app, text="WORDLE", justify=CENTER)
# labelWordle.place(relx=0.5, rely=0.1, anchor = CENTER)

# ------------ fila 1 ------------

entry_f1_c1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c1, entry_f1_c2)), "%S"), insertontime=0, textvariable=var_f1_c1, takefocus=False)
# entry_f1_c1.place(relx=0.2, rely=0.25, anchor = CENTER)
# def set_focus():
#     entry_f1_c1.focus()
# app.after(300, set_focus)

entry_f1_c2 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c2, entry_f1_c3)), "%S"), insertontime=0, textvariable=var_f1_c2, takefocus=False)
# entry_f1_c2.place(relx=0.35, rely=0.25, anchor = CENTER)

entry_f1_c3 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c3, entry_f1_c4)), "%S"), insertontime=0, textvariable=var_f1_c3, takefocus=False)
# entry_f1_c3.place(relx=0.5, rely=0.25, anchor = CENTER)

entry_f1_c4 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c4, entry_f1_c5)), "%S"), insertontime=0, textvariable=var_f1_c4, takefocus=False)
# entry_f1_c4.place(relx=0.65, rely=0.25, anchor = CENTER)

entry_f1_c5 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f1_c5, takefocus=False)
# entry_f1_c5.place(relx=0.8, rely=0.25, anchor = CENTER)

# ------------ fila 2 ------------

entry_f2_c1 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c1, entry_f2_c2)), "%S"), insertontime=0, textvariable=var_f2_c1, takefocus=False)
# entry_f2_c1.place(relx=0.2, rely=0.35, anchor = CENTER)

entry_f2_c2 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c2, entry_f2_c3)), "%S"), insertontime=0, textvariable=var_f2_c2, takefocus=False)
# entry_f2_c2.place(relx=0.35, rely=0.35, anchor = CENTER)

entry_f2_c3 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c3, entry_f2_c4)), "%S"), insertontime=0, textvariable=var_f2_c3, takefocus=False)
# entry_f2_c3.place(relx=0.5, rely=0.35, anchor = CENTER)

entry_f2_c4 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c4, entry_f2_c5)), "%S"), insertontime=0, textvariable=var_f2_c4, takefocus=False)
# entry_f2_c4.place(relx=0.65, rely=0.35, anchor = CENTER)

entry_f2_c5 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f2_c5, takefocus=False)
# entry_f2_c5.place(relx=0.8, rely=0.35, anchor = CENTER)

# ------------ fila 3 ------------

entry_f3_c1 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c1, entry_f3_c2)), "%S"), insertontime=0, textvariable=var_f3_c1, takefocus=False)
# entry_f3_c1.place(relx=0.2, rely=0.45, anchor = CENTER)

entry_f3_c2 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c2, entry_f3_c3)), "%S"), insertontime=0, textvariable=var_f3_c2, takefocus=False)
# entry_f3_c2.place(relx=0.35, rely=0.45, anchor = CENTER)

entry_f3_c3 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c3, entry_f3_c4)), "%S"), insertontime=0, textvariable=var_f3_c3, takefocus=False)
# entry_f3_c3.place(relx=0.5, rely=0.45, anchor = CENTER)

entry_f3_c4 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c4, entry_f3_c5)), "%S"), insertontime=0, textvariable=var_f3_c4, takefocus=False)
# entry_f3_c4.place(relx=0.65, rely=0.45, anchor = CENTER)

entry_f3_c5 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f3_c5, takefocus=False)
# entry_f3_c5.place(relx=0.8, rely=0.45, anchor = CENTER)

# ------------ fila 4 ------------

entry_f4_c1 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c1, entry_f4_c2)), "%S"), insertontime=0, textvariable=var_f4_c1, takefocus=False)
# entry_f4_c1.place(relx=0.2, rely=0.55, anchor = CENTER)

entry_f4_c2 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c2, entry_f4_c3)), "%S"), insertontime=0, textvariable=var_f4_c2, takefocus=False)
# entry_f4_c2.place(relx=0.35, rely=0.55, anchor = CENTER)

entry_f4_c3 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c3, entry_f4_c4)), "%S"), insertontime=0, textvariable=var_f4_c3, takefocus=False)
# entry_f4_c3.place(relx=0.5, rely=0.55, anchor = CENTER)

entry_f4_c4 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c4, entry_f4_c5)), "%S"), insertontime=0, textvariable=var_f4_c4, takefocus=False)
# entry_f4_c4.place(relx=0.65, rely=0.55, anchor = CENTER)

entry_f4_c5 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f4_c5, takefocus=False)
# entry_f4_c5.place(relx=0.8, rely=0.55, anchor = CENTER)

# ------------ fila 5 ------------

entry_f5_c1 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c1, entry_f5_c2)), "%S"), insertontime=0, textvariable=var_f5_c1, takefocus=False)
# entry_f5_c1.place(relx=0.2, rely=0.65, anchor = CENTER)

entry_f5_c2 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c2, entry_f5_c3)), "%S"), insertontime=0, textvariable=var_f5_c2, takefocus=False)
# entry_f5_c2.place(relx=0.35, rely=0.65, anchor = CENTER)

entry_f5_c3 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c3, entry_f5_c4)), "%S"), insertontime=0, textvariable=var_f5_c3, takefocus=False)
# entry_f5_c3.place(relx=0.5, rely=0.65, anchor = CENTER)

entry_f5_c4 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c4, entry_f5_c5)), "%S"), insertontime=0, textvariable=var_f5_c4, takefocus=False)
# entry_f5_c4.place(relx=0.65, rely=0.65, anchor = CENTER)

entry_f5_c5 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f5_c5, takefocus=False)
# entry_f5_c5.place(relx=0.8, rely=0.65, anchor = CENTER)

# ------------ fila 6 ------------

entry_f6_c1 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c1, entry_f6_c2)), "%S"), insertontime=0, textvariable=var_f6_c1, takefocus=False)
# entry_f6_c1.place(relx=0.2, rely=0.75, anchor = CENTER)

entry_f6_c2 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c2, entry_f6_c3)), "%S"), insertontime=0, textvariable=var_f6_c2, takefocus=False)
# entry_f6_c2.place(relx=0.35, rely=0.75, anchor = CENTER)

entry_f6_c3 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c3, entry_f6_c4)), "%S"), insertontime=0, textvariable=var_f6_c3, takefocus=False)
# entry_f6_c3.place(relx=0.5, rely=0.75, anchor = CENTER)

entry_f6_c4 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c4, entry_f6_c5)), "%S"), insertontime=0, textvariable=var_f6_c4, takefocus=False)
# entry_f6_c4.place(relx=0.65, rely=0.75, anchor = CENTER)

entry_f6_c5 = CTkEntry(master=app, justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f6_c5, takefocus=False)
# entry_f6_c5.place(relx=0.8, rely=0.75, anchor = CENTER)



listatodoslosentry = [entry_f1_c1, entry_f1_c2, entry_f1_c3, entry_f1_c4, entry_f1_c5, entry_f2_c1, entry_f2_c2, entry_f2_c3,  entry_f2_c4, entry_f2_c5, entry_f3_c1, entry_f3_c2, entry_f3_c3, entry_f3_c4, entry_f3_c5, entry_f4_c1, entry_f4_c2, entry_f4_c3, entry_f4_c4, entry_f4_c5, entry_f5_c1, entry_f5_c2, entry_f5_c3, entry_f5_c4, entry_f5_c5, entry_f6_c1, entry_f6_c2, entry_f6_c3, entry_f6_c4, entry_f6_c5]



entry_f1_c1.bind("<FocusOut>", convertir_a_mayusculas)
entry_f1_c2.bind("<FocusOut>", convertir_a_mayusculas)
entry_f1_c3.bind("<FocusOut>", convertir_a_mayusculas)
entry_f1_c4.bind("<FocusOut>", convertir_a_mayusculas)
entry_f1_c5.bind("<FocusOut>", convertir_a_mayusculas)

entry_f2_c1.bind("<FocusOut>", convertir_a_mayusculas)
entry_f2_c2.bind("<FocusOut>", convertir_a_mayusculas)
entry_f2_c3.bind("<FocusOut>", convertir_a_mayusculas)
entry_f2_c4.bind("<FocusOut>", convertir_a_mayusculas)
entry_f2_c5.bind("<FocusOut>", convertir_a_mayusculas)

entry_f3_c1.bind("<FocusOut>", convertir_a_mayusculas)
entry_f3_c2.bind("<FocusOut>", convertir_a_mayusculas)
entry_f3_c3.bind("<FocusOut>", convertir_a_mayusculas)
entry_f3_c4.bind("<FocusOut>", convertir_a_mayusculas)
entry_f3_c5.bind("<FocusOut>", convertir_a_mayusculas)

entry_f4_c1.bind("<FocusOut>", convertir_a_mayusculas)
entry_f4_c2.bind("<FocusOut>", convertir_a_mayusculas)
entry_f4_c3.bind("<FocusOut>", convertir_a_mayusculas)
entry_f4_c4.bind("<FocusOut>", convertir_a_mayusculas)
entry_f4_c5.bind("<FocusOut>", convertir_a_mayusculas)

entry_f5_c1.bind("<FocusOut>", convertir_a_mayusculas)
entry_f5_c2.bind("<FocusOut>", convertir_a_mayusculas)
entry_f5_c3.bind("<FocusOut>", convertir_a_mayusculas)
entry_f5_c4.bind("<FocusOut>", convertir_a_mayusculas)
entry_f5_c5.bind("<FocusOut>", convertir_a_mayusculas)

entry_f6_c1.bind("<FocusOut>", convertir_a_mayusculas)
entry_f6_c2.bind("<FocusOut>", convertir_a_mayusculas)
entry_f6_c3.bind("<FocusOut>", convertir_a_mayusculas)
entry_f6_c4.bind("<FocusOut>", convertir_a_mayusculas)
entry_f6_c5.bind("<FocusOut>", convertir_a_mayusculas)



# BORRAR Y MOVER
entry_f1_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c1, entry_f1_c1))
entry_f1_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c2, entry_f1_c1))
entry_f1_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c3, entry_f1_c2))
entry_f1_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c4, entry_f1_c3))
entry_f1_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c5, entry_f1_c4))

entry_f2_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c1, entry_f2_c1))
entry_f2_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c2, entry_f2_c1))
entry_f2_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c3, entry_f2_c2))
entry_f2_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c4, entry_f2_c3))
entry_f2_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c5, entry_f2_c4))

entry_f3_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c1, entry_f3_c1))
entry_f3_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c2, entry_f3_c1))
entry_f3_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c3, entry_f3_c2))
entry_f3_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c4, entry_f3_c3))
entry_f3_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c5, entry_f3_c4))

entry_f4_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c1, entry_f4_c1))
entry_f4_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c2, entry_f4_c1))
entry_f4_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c3, entry_f4_c2))
entry_f4_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c4, entry_f4_c3))
entry_f4_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c5, entry_f4_c4))

entry_f5_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c1, entry_f5_c1))
entry_f5_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c2, entry_f5_c1))
entry_f5_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c3, entry_f5_c2))
entry_f5_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c4, entry_f5_c3))
entry_f5_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c5, entry_f5_c4))

entry_f6_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c1, entry_f6_c1))
entry_f6_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c2, entry_f6_c1))
entry_f6_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c3, entry_f6_c2))
entry_f6_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c4, entry_f6_c3))
entry_f6_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c5, entry_f6_c4))

labelWordle.bind("<Key>", lambda event: borrar_y_mover(event, labelWordle, labelWordle))
labelWordle.bind("<Key>", lambda event: enter(event, labelWordle, labelWordle, entry_f1_c1, entry_f1_c2, entry_f1_c3, entry_f1_c4, entry_f1_c5, entry_f2_c1, entry_f2_c2, entry_f2_c3, entry_f2_c4, entry_f2_c5, entry_f3_c1, entry_f3_c2, entry_f3_c3, entry_f3_c4, entry_f3_c5, entry_f4_c1, entry_f4_c2, entry_f4_c3, entry_f4_c4, entry_f4_c5, entry_f5_c1, entry_f5_c2, entry_f5_c3, entry_f5_c4, entry_f5_c5, entry_f6_c1, entry_f6_c2, entry_f6_c3, entry_f6_c4, entry_f6_c5))


# ------------------------------------------------------------------------------------------------

# EN ROJO LAS QUE NO ESTÁN
entry_f2_c1.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f2_c1))
entry_f2_c2.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f2_c2))
entry_f2_c3.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f2_c3))
entry_f2_c4.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f2_c4))
entry_f2_c5.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f2_c5))

entry_f3_c1.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f3_c1))
entry_f3_c2.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f3_c2))
entry_f3_c3.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f3_c3))
entry_f3_c4.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f3_c4))
entry_f3_c5.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f3_c5))

entry_f4_c1.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f4_c1))
entry_f4_c2.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f4_c2))
entry_f4_c3.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f4_c3))
entry_f4_c4.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f4_c4))
entry_f4_c5.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f4_c5))

entry_f5_c1.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f5_c1))
entry_f5_c2.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f5_c2))
entry_f5_c3.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f5_c3))
entry_f5_c4.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f5_c4))
entry_f5_c5.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f5_c5))

entry_f6_c1.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f6_c1))
entry_f6_c2.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f6_c2))
entry_f6_c3.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f6_c3))
entry_f6_c4.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f6_c4))
entry_f6_c5.bind("<Key>", lambda event: root.after(0, lasQueNoEstan, entry_f6_c5))


# NO INTERACTUABLE CON EL RATON
entry_f1_c1.bind("<Button-1>", lambda event: "break")
entry_f1_c2.bind("<Button-1>", lambda event: "break")
entry_f1_c3.bind("<Button-1>", lambda event: "break")
entry_f1_c4.bind("<Button-1>", lambda event: "break")
entry_f1_c5.bind("<Button-1>", lambda event: "break")
entry_f1_c1.bind("<Button-2>", lambda event: "break")
entry_f1_c2.bind("<Button-2>", lambda event: "break")
entry_f1_c3.bind("<Button-2>", lambda event: "break")
entry_f1_c4.bind("<Button-2>", lambda event: "break")
entry_f1_c5.bind("<Button-2>", lambda event: "break")
entry_f1_c1.bind("<Button-3>", lambda event: "break")
entry_f1_c2.bind("<Button-3>", lambda event: "break")
entry_f1_c3.bind("<Button-3>", lambda event: "break")
entry_f1_c4.bind("<Button-3>", lambda event: "break")
entry_f1_c5.bind("<Button-3>", lambda event: "break")

entry_f2_c1.bind("<Button-1>", lambda event: "break")
entry_f2_c2.bind("<Button-1>", lambda event: "break")
entry_f2_c3.bind("<Button-1>", lambda event: "break")
entry_f2_c4.bind("<Button-1>", lambda event: "break")
entry_f2_c5.bind("<Button-1>", lambda event: "break")
entry_f2_c1.bind("<Button-2>", lambda event: "break")
entry_f2_c2.bind("<Button-2>", lambda event: "break")
entry_f2_c3.bind("<Button-2>", lambda event: "break")
entry_f2_c4.bind("<Button-2>", lambda event: "break")
entry_f2_c5.bind("<Button-2>", lambda event: "break")
entry_f2_c1.bind("<Button-3>", lambda event: "break")
entry_f2_c2.bind("<Button-3>", lambda event: "break")
entry_f2_c3.bind("<Button-3>", lambda event: "break")
entry_f2_c4.bind("<Button-3>", lambda event: "break")
entry_f2_c5.bind("<Button-3>", lambda event: "break")

entry_f3_c1.bind("<Button-1>", lambda event: "break")
entry_f3_c2.bind("<Button-1>", lambda event: "break")
entry_f3_c3.bind("<Button-1>", lambda event: "break")
entry_f3_c4.bind("<Button-1>", lambda event: "break")
entry_f3_c5.bind("<Button-1>", lambda event: "break")
entry_f3_c1.bind("<Button-2>", lambda event: "break")
entry_f3_c2.bind("<Button-2>", lambda event: "break")
entry_f3_c3.bind("<Button-2>", lambda event: "break")
entry_f3_c4.bind("<Button-2>", lambda event: "break")
entry_f3_c5.bind("<Button-2>", lambda event: "break")
entry_f3_c1.bind("<Button-3>", lambda event: "break")
entry_f3_c2.bind("<Button-3>", lambda event: "break")
entry_f3_c3.bind("<Button-3>", lambda event: "break")
entry_f3_c4.bind("<Button-3>", lambda event: "break")
entry_f3_c5.bind("<Button-3>", lambda event: "break")

entry_f4_c1.bind("<Button-1>", lambda event: "break")
entry_f4_c2.bind("<Button-1>", lambda event: "break")
entry_f4_c3.bind("<Button-1>", lambda event: "break")
entry_f4_c4.bind("<Button-1>", lambda event: "break")
entry_f4_c5.bind("<Button-1>", lambda event: "break")
entry_f4_c1.bind("<Button-2>", lambda event: "break")
entry_f4_c2.bind("<Button-2>", lambda event: "break")
entry_f4_c3.bind("<Button-2>", lambda event: "break")
entry_f4_c4.bind("<Button-2>", lambda event: "break")
entry_f4_c5.bind("<Button-2>", lambda event: "break")
entry_f4_c1.bind("<Button-3>", lambda event: "break")
entry_f4_c2.bind("<Button-3>", lambda event: "break")
entry_f4_c3.bind("<Button-3>", lambda event: "break")
entry_f4_c4.bind("<Button-3>", lambda event: "break")
entry_f4_c5.bind("<Button-3>", lambda event: "break")

entry_f5_c1.bind("<Button-1>", lambda event: "break")
entry_f5_c2.bind("<Button-1>", lambda event: "break")
entry_f5_c3.bind("<Button-1>", lambda event: "break")
entry_f5_c4.bind("<Button-1>", lambda event: "break")
entry_f5_c5.bind("<Button-1>", lambda event: "break")
entry_f5_c1.bind("<Button-2>", lambda event: "break")
entry_f5_c2.bind("<Button-2>", lambda event: "break")
entry_f5_c3.bind("<Button-2>", lambda event: "break")
entry_f5_c4.bind("<Button-2>", lambda event: "break")
entry_f5_c5.bind("<Button-2>", lambda event: "break")
entry_f5_c1.bind("<Button-3>", lambda event: "break")
entry_f5_c2.bind("<Button-3>", lambda event: "break")
entry_f5_c3.bind("<Button-3>", lambda event: "break")
entry_f5_c4.bind("<Button-3>", lambda event: "break")
entry_f5_c5.bind("<Button-3>", lambda event: "break")

entry_f6_c1.bind("<Button-1>", lambda event: "break")
entry_f6_c2.bind("<Button-1>", lambda event: "break")
entry_f6_c3.bind("<Button-1>", lambda event: "break")
entry_f6_c4.bind("<Button-1>", lambda event: "break")
entry_f6_c5.bind("<Button-1>", lambda event: "break")
entry_f6_c1.bind("<Button-2>", lambda event: "break")
entry_f6_c2.bind("<Button-2>", lambda event: "break")
entry_f6_c3.bind("<Button-2>", lambda event: "break")
entry_f6_c4.bind("<Button-2>", lambda event: "break")
entry_f6_c5.bind("<Button-2>", lambda event: "break")
entry_f6_c1.bind("<Button-3>", lambda event: "break")
entry_f6_c2.bind("<Button-3>", lambda event: "break")
entry_f6_c3.bind("<Button-3>", lambda event: "break")
entry_f6_c4.bind("<Button-3>", lambda event: "break")
entry_f6_c5.bind("<Button-3>", lambda event: "break")

entryGameOver1.bind("<Button-1>", lambda event: "break")
entryGameOver2.bind("<Button-1>", lambda event: "break")
entryGameOver3.bind("<Button-1>", lambda event: "break")
entryGameOver4.bind("<Button-1>", lambda event: "break")
entryGameOver5.bind("<Button-1>", lambda event: "break")
entryGameOver1.bind("<Button-2>", lambda event: "break")
entryGameOver2.bind("<Button-2>", lambda event: "break")
entryGameOver3.bind("<Button-2>", lambda event: "break")
entryGameOver4.bind("<Button-2>", lambda event: "break")
entryGameOver5.bind("<Button-2>", lambda event: "break")
entryGameOver1.bind("<Button-3>", lambda event: "break")
entryGameOver2.bind("<Button-3>", lambda event: "break")
entryGameOver3.bind("<Button-3>", lambda event: "break")
entryGameOver4.bind("<Button-3>", lambda event: "break")
entryGameOver5.bind("<Button-3>", lambda event: "break")



root.unbind_all('<<NextWindow>>')

root.update()
update_ui(root)
root.mainloop()