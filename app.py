import random
from tkinter import messagebox, Label, Button, DISABLED, Tk, StringVar
from PIL import ImageTk, Image

root = Tk()
root.title("Hangman Nama Hewan")
root.geometry("720x480")
root.resizable(0, 0)

hewan = open("hewan.txt", "r")
daftar_hewan = hewan.readlines()
hewan_cocok = []
hewan_cocok_var = StringVar()
kesempatan = 0

image_array = ["hangman/hangman1.png", "hangman/hangman2.png", "hangman/hangman3.png", "hangman/hangman4.png",
               "hangman/hangman5.png", "hangman/hangman6.png", "hangman/hangman7.png"]

nama_hewan = random.choice(daftar_hewan)

for i in range(0, len(nama_hewan) - 1):
    if nama_hewan[i] == " ":
        hewan_cocok.append(" ")
    else:
        hewan_cocok.append("_")

hangman = Image.open(image_array[kesempatan])
hangman = hangman.resize((200, 300), Image.ANTIALIAS)
hangman = ImageTk.PhotoImage(hangman)
display = Label(root, image=hangman)
display.grid(row=1, column=0, rowspan=2)

hewan_cocok_str = ' '.join(hewan_cocok)
hewan_cocok_var.set(hewan_cocok_str)
Label(root, textvariable=hewan_cocok_var, font="Arial 20 bold").grid(row=1, column=1, columnspan=10)


def clicked(tebakan, row, column):
    control = False
    Button(root, text=tebakan, font="Arial 16 bold", state=DISABLED, width=2).grid(row=row, column=column)
    for x in range(0, len(nama_hewan)):
        if tebakan == nama_hewan[x]:
            control = True
            hewan_cocok[x] = tebakan
            update = ' '.join(hewan_cocok)
            hewan_cocok_var.set(update)

    if "_" not in hewan_cocok:
        messagebox.showinfo("You Win", "Anda Menang!")
        root.destroy()

    if not control:
        global kesempatan
        kesempatan += 1
        hangman_new = Image.open(image_array[kesempatan])
        hangman_new = hangman_new.resize((200, 300), Image.ANTIALIAS)
        hangman_new = ImageTk.PhotoImage(hangman_new)
        display.configure(image=hangman_new)
        display.image = hangman_new
        if kesempatan == 6:
            messagebox.showinfo("Game Over", "Anda Gagal!\nJawaban: " + nama_hewan)
            root.destroy()


Button(root, text="Q", font="Arial 16 bold", command=lambda: clicked("Q", 3, 1), width=2).grid(row=3, column=1)
Button(root, text="W", font="Arial 16 bold", command=lambda: clicked("W", 3, 2), width=2).grid(row=3, column=2)
Button(root, text="E", font="Arial 16 bold", command=lambda: clicked("E", 3, 3), width=2).grid(row=3, column=3)
Button(root, text="R", font="Arial 16 bold", command=lambda: clicked("R", 3, 4), width=2).grid(row=3, column=4)
Button(root, text="T", font="Arial 16 bold", command=lambda: clicked("T", 3, 5), width=2).grid(row=3, column=5)
Button(root, text="Y", font="Arial 16 bold", command=lambda: clicked("Y", 3, 6), width=2).grid(row=3, column=6)
Button(root, text="U", font="Arial 16 bold", command=lambda: clicked("U", 3, 7), width=2).grid(row=3, column=7)
Button(root, text="I", font="Arial 16 bold", command=lambda: clicked("I", 3, 8), width=2).grid(row=3, column=8)
Button(root, text="O", font="Arial 16 bold", command=lambda: clicked("O", 3, 9), width=2).grid(row=3, column=9)
Button(root, text="P", font="Arial 16 bold", command=lambda: clicked("P", 3, 10), width=2).grid(row=3, column=10)

Button(root, text="A", font="Arial 16 bold", command=lambda: clicked("A", 4, 1), width=2).grid(row=4, column=1)
Button(root, text="S", font="Arial 16 bold", command=lambda: clicked("S", 4, 2), width=2).grid(row=4, column=2)
Button(root, text="D", font="Arial 16 bold", command=lambda: clicked("D", 4, 3), width=2).grid(row=4, column=3)
Button(root, text="F", font="Arial 16 bold", command=lambda: clicked("F", 4, 4), width=2).grid(row=4, column=4)
Button(root, text="G", font="Arial 16 bold", command=lambda: clicked("G", 4, 5), width=2).grid(row=4, column=5)
Button(root, text="H", font="Arial 16 bold", command=lambda: clicked("H", 4, 6), width=2).grid(row=4, column=6)
Button(root, text="J", font="Arial 16 bold", command=lambda: clicked("J", 4, 7), width=2).grid(row=4, column=7)
Button(root, text="K", font="Arial 16 bold", command=lambda: clicked("K", 4, 8), width=2).grid(row=4, column=8)
Button(root, text="L", font="Arial 16 bold", command=lambda: clicked("L", 4, 9), width=2).grid(row=4, column=9)

Button(root, text="Z", font="Arial 16 bold", command=lambda: clicked("Z", 5, 1), width=2).grid(row=5, column=1)
Button(root, text="X", font="Arial 16 bold", command=lambda: clicked("X", 5, 2), width=2).grid(row=5, column=2)
Button(root, text="C", font="Arial 16 bold", command=lambda: clicked("C", 5, 3), width=2).grid(row=5, column=3)
Button(root, text="V", font="Arial 16 bold", command=lambda: clicked("V", 5, 4), width=2).grid(row=5, column=4)
Button(root, text="B", font="Arial 16 bold", command=lambda: clicked("B", 5, 5), width=2).grid(row=5, column=5)
Button(root, text="N", font="Arial 16 bold", command=lambda: clicked("N", 5, 6), width=2).grid(row=5, column=6)
Button(root, text="M", font="Arial 16 bold", command=lambda: clicked("M", 5, 7), width=2).grid(row=5, column=7)

root.mainloop()
