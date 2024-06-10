# Chat em Tempo Real com Tkinter e Websockets

Este repositório contém um sistema de chat em tempo real desenvolvido em Python 3.9, utilizando as bibliotecas Tkinter para a interface gráfica e websockets para a comunicação entre cliente e servidor. O projeto permite que os usuários troquem mensagens instantaneamente em uma interface intuitiva.

Estrutura do Projeto

server.py: Código do servidor responsável por estabelecer conexões e gerenciar as trocas de mensagens entre os clientes. Além disso, este arquivo também lida com a persistência das mensagens em um arquivo mensagens.txt.

app.py: Código do programa Tkinter que proporciona a interface gráfica para os usuários enviarem e receberem mensagens no chat.
mensagens.txt: Arquivo de log que armazena todas as mensagens trocadas no chat. Este arquivo é atualizado pelo servidor à medida que novas mensagens são recebidas.

Como Executar

Clone o repositório:

git clone https://github.com/Gabriel-Hernandess/tkinterChat-Python-Websockets.git
cd tkinterChat-Python-Websockets

Instale as dependências:

pip install tk
pip install websockets

Inicie o servidor de chat:

python server.py

Inicie o cliente de chat:

python app.py

Pré-requisitos

Python 3.9
Bibliotecas Python: Tkinter, websockets
