import FUN as m
import os

op=0
while(op!=4):
    os.system("cls")
    op=m.menu()
    if(op==1):
        m.ingresarInvestigacion()
    elif(op==2):
        m.eliminar()
    elif(op==3):
        m.mostrarUna()