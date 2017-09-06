import threading
import tkinter as Tk
import sys
from random import choice
from tkinter import N, E, S, W


tam = int(sys.argv[2])
if tam > 150 : exit(1)
bitMap = []
game_labels = []
colors = ("red", "green", "blue")


def trigger():
	def run():
		global bitMap
		while True:
			next_bitMap = []
			for i, alive in enumerate(bitMap):
				cont = 0
				try:
					cont += 1 if bitMap[i+1] else 0
				except IndexError:
					pass
				try:
					cont += 1 if bitMap[i-1] else 0
				except IndexError:
					pass
				try:
					cont += 1 if bitMap[i+1+tam] else 0
				except IndexError:
					pass
				try:
					cont += 1 if bitMap[i-1+tam] else 0
				except IndexError:
					pass
				try:
					cont += 1 if bitMap[i+1-tam] else 0
				except IndexError:
					pass
				try:
					cont += 1 if bitMap[i-1-tam] else 0
				except IndexError:
					pass
				try:
					cont += 1 if bitMap[i+tam] else 0
				except IndexError:
					pass
				try:
					cont += 1 if bitMap[i-tam] else 0
				except IndexError:
					pass

				if alive and cont < 2:
					next_bitMap.append(False)
					continue
				if alive and cont > 3:
					next_bitMap.append(False)
					continue
				if not alive and cont == 3:
					next_bitMap.append(True)
					continue
				next_bitMap.append(alive)

			bitMap = next_bitMap

			for i, alive in enumerate(bitMap):
				game_labels[i].config(bg=choice(colors)) if alive else game_labels[i].config(bg='white')




	game_thread = threading.Thread(target=run)
	game_thread.daemon = True
	game_thread.start()

def main():
	root = Tk.Tk()
	root.title("Conway's")


	button_frame = Tk.Frame(root)
	button_frame.grid(row=0, column=0, sticky=N+E+S+W)

	game_frame = Tk.Frame(root)
	game_frame.grid(row=1, column=0, sticky=N+E+S+W)

	start_button = Tk.Button(button_frame, padx=5, pady=5, text='Start', command=trigger)
	start_button.grid(row=0,column=0)
	
	exit_button = Tk.Button(button_frame, padx=5, pady=5, text='Exit', command=lambda: root.destroy())
	exit_button.grid(row=0,column=1)

	with open(sys.argv[1], 'r') as _map:
		buff = _map.read(1024);
		while buff != '':
			for bit in buff:
				bitMap.append(True) if bit == '*' else bitMap.append(False)
			buff = _map.read(1024)


	for i in range(tam):
		for j in range(tam):
			bg = 'white' if not bitMap[j + i*tam]  else choice(colors)
			game_label = Tk.Canvas(game_frame,width=10, height=10, bg=bg)
			game_label.grid(row=i+1, column=j, sticky=N+E+S+W)
			game_labels.append(game_label)

	root.protocol("WM_DELETE_WINDOW", root.destroy)
	root.mainloop()

if __name__ == "__main__":
	main()

			
