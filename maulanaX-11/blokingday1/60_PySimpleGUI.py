import tkinter as tk

def tombol_diklik():
    print("Tombol diklik")

window = tk.Tk()
window.title("Contoh Program Tkinter")

btn = tk.Button(window, text="Klik Saya", command=tombol_diklik)
btn.pack(padx=20, pady=20)

window.mainloop()