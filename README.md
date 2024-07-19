# Kalman Sim
![Python Version](https://badgen.net/badge/status/finished%20:\)/green)
![Python 3.6](https://img.shields.io/badge/python-3.12-blue.svg)
![Last Commit](https://badgen.net/github/last-commit/barbarabarsi/kalman-sim?color=yellow)

Esse projeto simula a aplicação de um filtro de Kalman para determinar a posição de um carro em movimento dentro de um túnel (ou qualquer local onde os sensores estejam suscetíveis a ruído). O programa utiliza leituras simuladas de um GPS e aplica o filtro de Kalman para suavizar os dados ruidosos e obter uma trajetória mais precisa.

## Modelagem do Sistema
A modelagem do sistema considera 4 estados: posição ao norte, posição ao leste, velocidade ao norte e velocidade ao leste, sendo os dois primeiros os que serão devolvidos ao usuário. Aqui considera-se que a acelerção é constante,que a modelagem das equações está correta e que não existem forças externas atuando no sistema.

## Arquivos do Repositório

- `gps.py`: Script principal que executa a simulação.
- `board.py`: Contém a função para criar um quadro de desenho da trajetória do carro.
- `kalmanfilter.py`: Implementação do filtro de Kalman.

## Como Executar

Primeiro, instale as dependências do projeto com o comando

``` pip install -r ./requirements.txt ```

Em seguida, execute o arquivo gps.py:

```python3 gps.py```

Uma janela será aberta para que você possa desenhar a trajetória desejada. Após concluir, feche a janela de desenho para que o programa simule leituras de GPS com ruído baseadas no desenho do percurso. Lembre que estamos considerando que o carro passa por um túnel, ou seja, o sinal do GPS é suscetível a distorções e ruídos.

## Exibição dos Resultados:

Após a simulação, uma nova janela será aberta exibindo a trajetória real do carro, as leituras simuladas do GPS (com ruído) e a trajetória estipulada pelo filtro de Kalman em uma exibição gráfica. Além disso, após fechar a janela de resultados, você pode visualizar um GIF mostrando a aplicação do filtro de Kalman ao longo do tempo na pasta gifs/results.Cada frame utilizado para gerar o GIF pode ser encontrado na pasta gifs/frames.

<img src="https://i.ibb.co/QrqnTrj/path-building.gif">
