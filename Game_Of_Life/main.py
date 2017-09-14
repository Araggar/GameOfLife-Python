import threading
import tkinter as Tk
import sys
from concurrent.futures import ThreadPoolExecutor
from random import choice
from tkinter import N, E, S, W


tam = int(sys.argv[2])
bitMap = []
game_labels = [None]*(tam*tam)
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
					next_bitMap.append((i, False))
					continue
				if alive and cont > 3:
					next_bitMap.append((i, False))
					continue
				if not alive and cont == 3:
					next_bitMap.append((i, True))
					continue

			for ind, bit in next_bitMap:
				bitMap[ind] = bit
				game_labels[ind].config(bg=choice(colors)) if bit else game_labels[ind].config(bg='white')				




	game_thread = threading.Thread(target=run)
	game_thread.daemon = True
	game_thread.start()

def main():
	def callback(i):
		global tam
		global game_labels
		global colors

		for j in range(tam):
			bg = 'white' if not bitMap[j + i*tam]  else choice(colors)
			game_label = Tk.Canvas(game_frame,width=10, height=10, bg=bg)
			game_label.grid(row=i+1, column=j, sticky=N+E+S+W)
			game_labels[j + i*tam] = game_label






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

	pool = ThreadPoolExecutor(128)
	for i in range(tam):
		pool.submit(callback, i)

	print(threading.active_count())


	root.protocol("WM_DELETE_WINDOW", root.destroy)
	root.mainloop()

main()

			
