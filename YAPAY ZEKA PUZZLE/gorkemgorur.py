import tkinter as Tk
import random as rnd
import time
from YSA_ENSON import Network

def degistir(dno):
    global tiklamasayisi, ilkdugme, ikincidugme
    tiklamasayisi = tiklamasayisi + 1
    if tiklamasayisi == 1:
        ilkdugme = dno
        dugmeler[ilkdugme].configure(bg=renk[2])  
    else:
        ikincidugme = dno
        tiklamasayisi = 0
        dugmeler[ikincidugme].configure(bg=renk[3])  
        form.update()
        time.sleep(0.2) # 0.2 saniye
        if (abs(ilkdugme // sutun - ikincidugme // sutun) <= 1 and abs(ilkdugme % sutun - ikincidugme % sutun) <= 1) and (
                (ikincidugme // sutun + ikincidugme % sutun) % 2 != (ilkdugme // sutun + ilkdugme % sutun) % 2):
            d1 = min(ilkdugme, ikincidugme)
            d2 = max(ilkdugme, ikincidugme)
            d1t = int(dugmeler[d1]["text"])
            d2t = int(dugmeler[d2]["text"])
            if SinirAgim.feedforward([d1t, d2t]) > 0.5:
                dugmeler[ilkdugme]["text"], dugmeler[ikincidugme]["text"] = dugmeler[ikincidugme]["text"], dugmeler[ilkdugme]["text"]
                dugmeler[ilkdugme]["bg"], dugmeler[ikincidugme]["bg"] = renk[1], renk[1]  
                dugmeler[ilkdugme]["fg"], dugmeler[ikincidugme]["fg"] = renk[0], renk[0]  
                form.update()
                time.sleep(1)  
        geri_dondur()

def geri_dondur():
    dugmeler[ilkdugme].configure(bg=renk[1])  
    dugmeler[ikincidugme].configure(bg=renk[1])  
    form.update()

form = Tk.Tk()
form.geometry("400x400+50+50")
tiklamasayisi = 0
satir, sutun = 5, 5 
renk = ["Black", "White", "Lime", "Red", "Yellow"]
dugmeler = []

numaralar = rnd.sample(range(satir * sutun), satir * sutun)

for sat in range(satir):
    for sut in range(sutun):
        x = rnd.randint(0, 1)
        Dugme = Tk.Button(form, text="%s" % (numaralar[sat * sutun + sut]), height=3, width=7, fg=renk[0], bg=renk[1],
                          command=lambda dn=sat * sutun + sut: degistir(dn))
        Dugme.grid(row=sat, column=sut)
        dugmeler.append(Dugme)

SinirAgim = Network()

puzzleTamamlandi = False

while not puzzleTamamlandi:
    puzzle = [[int(dugme["text"]) for dugme in dugmeler[i:i + sutun]] for i in range(0, len(dugmeler), sutun)]
    
    puzzleTamamlandi = True
    for i in range(satir * sutun - 1):
        if int(dugmeler[i]["text"]) > int(dugmeler[i + 1]["text"]):
            puzzleTamamlandi = False
            break

    ilkdugme = rnd.randint(0, satir * sutun - 1)
    ikincidugme = rnd.randint(0, satir * sutun - 1)
    while ilkdugme == ikincidugme:
        ikincidugme = rnd.randint(0, satir * sutun - 1)

    degistir(ilkdugme)
    degistir(ikincidugme)

for dugme in dugmeler:
    dugme.configure(bg=renk[4]) 
    dugme.configure(state="disabled")  

puzzleTamamlandiEtiketi = Tk.Label(form, text="Puzzle Tamamlandı", font=("Arial", 16), fg="blue")
puzzleTamamlandiEtiketi.grid(row=satir, columnspan=sutun, pady=20)

Tk.mainloop()
