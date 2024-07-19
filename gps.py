import numpy as np
import matplotlib.pyplot as plt
from board import Board
from kalmanfilter import Kalman

from IPython.display import Image
import glob
import imageio as iio
import os
import cv2

def gps(path):

	kal = Kalman()

	predictions = []
	measurements = []
	adj = []

	m_plot = []
	r_plot = []
	image_array = []
	y_ax = []

	for t in path:
		x = t[0] - path[0][0]
		y = (-t[1] + path[0][1]) if -t[1] < 0 else -t[1]
		adj.append((x, y))

	for t in adj:
		y_ax.append(t[1])
		if list(adj).index(t)%2 == 0 or list(adj).index(t)%3 == 0  or list(adj).index(t)%7 == 0:
			continue
		measurements.append((t[0] + 2*np.random.normal(0,np.random.rand()), t[1] + 2*np.random.normal(0,np.random.rand())))

	files = glob.glob(r"./gifs/frames/*.png")
	for f in files:
		os.remove(f)

	files = glob.glob(r"./gifs/results/*.png")
	for f in files:
		os.remove(f)


	for m in measurements:

		m_plot.append(m)
		r_plot.append(adj[list(measurements).index(m)])

		kal.filter(m)
		predictions.append((kal.x[0,0], kal.x[0,1]))

		idx = list(measurements).index(m)
		name = f"path_frame_0{idx+1}" if idx < 9 else f"path_frame_{idx+1}"

		plt.plot(*zip(*m_plot), 'o', markersize=2, color='orange', label="Medições")
		plt.plot(*zip(*predictions), color='red', label="Predição de Kalman")
		# plt.plot(*zip(*r_plot), markersize=1, color='green', label="Caminho real")

		plt.xticks(np.arange(0, adj[-1][0], 50))
		plt.yticks(np.arange(min(y_ax), max(y_ax), 50))
		plt.legend()
		plt.savefig(f"./gifs/frames/{name}.png")
		plt.close()

		image = cv2.cvtColor(cv2.imread(f"./gifs/frames/{name}.png"), cv2.COLOR_BGR2RGB)
		image_array.append(image)

	_, axs = plt.subplots(1, 3, figsize=(20, 20))

	axs[0].plot(*zip(*measurements), 'o', markersize=1, color='orange')
	axs[0].set_title('Medições ruidosas')

	axs[1].plot(*zip(*predictions), color='red')
	axs[1].set_title('Filtro de Kalman')

	axs[2].plot(*zip(*measurements), 'o', markersize=3, color='orange')
	axs[2].plot(*zip(*predictions),color='red')
	axs[2].plot(*zip(*adj), markersize=1, color='green')
	axs[2].set_title('Comparação dos resultados')

	plt.show()

	iio.mimwrite("./gifs/results/path_building.gif", image_array, format='gif', loop=0, fps=20)

if __name__ == '__main__':

  path = Board.draw()
  gps(path)
