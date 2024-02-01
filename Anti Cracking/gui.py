'''
Este modulo se encarga de la configuración
de la interfaz grafica de usuario

'''

from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox
import tkinter as tk
from pgm import password_generator, save_passwords
from colors import*

def PG_App(length: int, symbols: bool, uppercase: bool, quantity: int):
    contraseñas = []

    ventana = CTk()
    ventana.minsize(480, 300)  # Ajusta la altura de la ventana
    ventana.config(bg=c_negro)
    ventana.resizable(False, False)
    ventana.title("Contraseñas")

    frame2 = CTkFrame(ventana, fg_color=c_negro,
                      border_color="#00FFFF", border_width=2)
    frame2.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

    scrollbar = tk.Scrollbar(frame2)
    textarea = tk.Text(frame2, font=('Arial', 12), yscrollcommand=scrollbar.set, fg="white", bg=c_negro,
                       relief="solid", borderwidth=2, highlightthickness=2, padx=4, pady=4, wrap=tk.WORD)
    textarea.config(highlightbackground="blue")

    # Ubicar el Text widget y scrollbar en la ventana
    textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    for i in range(quantity):
        password = f"Contraseña número {i+1}  ---->  " + password_generator(
            length=length, symbols=symbols, uppercase=uppercase)
        contraseñas.append(password)
        textarea.insert(tk.END, password + "\n\n")

    # Deshabilitar la escritura en el Text widget
    textarea.configure(state=tk.DISABLED)

    derechos = "ITE"
    label_derechos = CTkLabel(
        ventana, bg_color=c_negro, text=derechos, font=("Arial", 12))
    label_derechos.grid(row=2, columnspan=2, padx=0, pady=10)

    # Agregar botón "Guardar"
    bt_guardar = CTkButton(ventana, font=('Arial', 12), border_color=c_rojo,
                           fg_color=c_negro, hover_color="#F2A405", corner_radius=12, border_width=2, text='Guardar', height=35,
                           command=lambda: save_passwords(contraseñas, 'contraseñas_guardadas.txt'))
    bt_guardar.grid(row=3, column=0, columnspan=2, pady=10)

    # Fin ventana
    ventana.mainloop()

# Pestaña principal

def main():
	root = CTk()
	root.geometry('500x600+320+20')
	root.minsize(480, 500)
	root.config(bg=c_negro)
	root.resizable(False, False)
	root.title("Anti Cracking")

	frame = CTkFrame(root, fg_color=c_negro,
	                 border_color="#427EF6", border_width=2)
	frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

	frame.columnconfigure([0, 1], weight=1)
	frame.rowconfigure([0, 1, 2, 3, 4], weight=1)

	# Dentro de la ventana principal configuramos la posición del frame
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)

	# Elementos de la app

	# Crear el label para el texto
	texto = "Anti Cracking"
	label_texto = CTkLabel(frame, text=texto, font=("Arial", 25))
	label_texto.grid(row=0, column=1, padx=0, pady=5)

	longitud = CTkEntry(frame, font=('Arial', 12),
	                    placeholder_text='Longitud de la Contraseña', border_color=c_cyan, fg_color=c_negro, width=200, height=40)
	longitud.grid(columnspan=2, row=1, padx=4, pady=2)

	cantidad = CTkEntry(frame, font=('Arial', 12),
	                    placeholder_text='Cantidad de Contraseñas', border_color=c_cyan, fg_color=c_negro, width=200, height=40)
	cantidad.grid(columnspan=2, row=2, padx=4, pady=2)

	simbolos = CTkCheckBox(frame, text='Símbolos', hover_color=c_verde,
	                       border_color=c_cyan, fg_color=c_cyan)
	simbolos.grid(column=0, row=3, padx=4, pady=6)

	mayusculas = CTkCheckBox(frame, text='Mayúsculas', hover_color=c_verde,
	                         border_color=c_cyan, fg_color=c_cyan)
	mayusculas.grid(column=1, row=3, padx=4, pady=6)

	# Botón
	bt_gen = CTkButton(frame, font=('Arial', 12), border_color=c_cyan,
	                   fg_color=c_negro, hover_color="#F2A405", corner_radius=12, border_width=2, text='Generar Contraseñas', height=35,
	                   command=lambda: PG_App(length=int(longitud.get().strip()),
	                                                 symbols=simbolos.get(),
	                                                 uppercase=mayusculas.get(),
	                                                 quantity=int(cantidad.get().strip())))
	bt_gen.grid(columnspan=2, row=4, padx=4, pady=18)

	derechos = "ITE"
	label_derechos = CTkLabel(frame, text=derechos, font=("Arial", 12))
	label_derechos.grid(row=5, columnspan=2, padx=0, pady=5)

	# Fin ventana
	root.mainloop()

if __name__ == "__main__":
    main()