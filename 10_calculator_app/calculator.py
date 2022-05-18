from tkinter import *  #CTRL+B SA VAD FUNCTIA

window = Tk()  #instantierea ca in oop
window.geometry("500x354")  #dimenstiunea ferestrei
window.title("Calculator")  #ce apare sus pe fereastra
window.resizable(None, None)  #sa nu poata fi modificata fereastra, sa o maresc, sa o micsorez


def click(item):  #o functie care atunci cand dam click ne calculeaza tot ce se vede pe ecranul calculatorului
    global expression
    expression += str(item)
    input_text.set(expression)


def clear():
    global expression
    expression = ""
    input_text.set("")  #golim ce am scris


def egalitate():
    try:
        #atunci cand apasam pe egal ne calculeaza expresia
        global expression  #expresia pe care o realizam la click
        rezultat = str(eval(expression))  #trasforma expresia din string in matematica
        input_text.set(rezultat)
        expression = ""  #devine goala ca a fost calculata
    except Exception:
        expression=""
        input_text.set('Error: Please click C button')



expression = ''
input_text = StringVar()
# incepem sa calculam frame-urile, frameurile reprezinta zona in care sunt incadrate butoanele, o sa avem 2, unul cu rezultatul si unul cu cifrele
input_frame = Frame(window, width=312, height=50)
input_frame.pack(side=TOP)

#inputul in care screm valorile
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg='powderblue', bd=0, justify=RIGHT)


input_field.grid(row=0, column=0)
input_field.pack()


#definim frame-ul pentru butoane, bg = background
frame_butoane = Frame(window, width=500, height=304, bg='grey')
frame_butoane.pack()
buton_clear = Button(frame_butoane, text='C', width=57, height=3, bg='#eee', cursor='hand2', command=lambda: clear()).grid(row=0, column=0, columnspan=3)  #acel C din calculator

impartit = Button(frame_butoane, text='/', width=10, height=3, bg='#FFA500', cursor='hand2', command=lambda: click('/')).grid(row=0, column=3)

sapte = Button(frame_butoane, text='7', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('7')).grid(row=1, column=0)
opt = Button(frame_butoane, text='8', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('8')).grid(row=1, column=1)
noua = Button(frame_butoane, text='9', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('9')).grid(row=1, column=2)
inmultire = Button(frame_butoane, text='*', width=10, height=3, bg='#FAA500', cursor="hand2", command=lambda: click('*')).grid(row=1, column=3)


patru = Button(frame_butoane, text='4', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('4')).grid(row=2, column=0)
cinci = Button(frame_butoane, text='5', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('5')).grid(row=2, column=1)
sase = Button(frame_butoane, text='6', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('6')).grid(row=2, column=2)
inmultire = Button(frame_butoane, text='*', width=10, height=3, bg='#FAA500', cursor="hand2", command=lambda: click('*')).grid(row=2, column=3)


unu = Button(frame_butoane, text='1', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('1')).grid(row=3, column=0)
doi = Button(frame_butoane, text='2', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('2')).grid(row=3, column=1)
trei = Button(frame_butoane, text='3', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('3')).grid(row=3, column=2)
adunare = Button(frame_butoane, text='+', width=10, height=3, bg='#FAA500', cursor="hand2", command=lambda: click('+')).grid(row=3, column=3)

zero = Button(frame_butoane, text='0', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('0')).grid(row=4, column=0)
zerozero = Button(frame_butoane, text='00', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('00')).grid(row=4, column=1)
virgula = Button(frame_butoane, text='.', width=18, height=3, bg='#eee', cursor="hand2", command=lambda: click('.')).grid(row=4, column=2)
egal = Button(frame_butoane, text='=', width=10, height=3, bg='#eee', cursor='hand2', command=lambda: egalitate()).grid(
    row=4, column=3)


window.mainloop()  #ne ajuta sa rulam, creeaza fereastra