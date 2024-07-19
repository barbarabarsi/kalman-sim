import numpy as np
import matplotlib.pyplot as plt

class Kalman:

    def __init__(self):

        dt = 0.1

        self.x = np.zeros((4,1))

        # Matriz de transição de estado -> usada na etapa de predição
        self.F = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]])

        # Matriz de observação -> mapeia o estado usando as medições
        self.H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])

        # Matriz de covariância dos estados -> mapeia a incerteza na definição dos estados
        self.P = np.eye(4) * 0.1

        # Matriz de covariância do processo, ou seja, seu rúido
        self.Q = np.eye(4) * 0.1

        # Matriz de covariância da medição, ou seja, o seu ruído
        # (obs: o valor abaixo foi escolhido con5iderando a variância escolhida para a simulação das medições ruidosas)
        self.R =  np.eye(2) * 10

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, b):
        K = self.P @ self.H.T @ np.linalg.inv(self.H @ self.P @ self.H.T + self.R)
        self.P = (np.eye(4) - K @ self.H) @ self.P @ (np.eye(4) - K @ self.H) + (K @ self.R @ K.T)

        self.x = self.x + K @ (b - self.H @ self.x)
        return self.x

    def filter(self, b):
        self.predict()
        self.update(b)


