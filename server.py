import asyncio
import websockets
from datetime import datetime

# Lista de clientes conectados ao servidor
clients = set()

# Função para lidar com a conexão de um novo cliente
async def handle_client(websocket, path):
    clients.add(websocket)
    print(f'Cliente conectado com sucesso. IP: {websocket.remote_address}')

    try:
        # Iniciar a tarefa de ping
        ping_task = asyncio.create_task(ping_clients(websocket))
        async for message in websocket:
            # Salvar mensagem no arquivo
            save_message(message)
            await broadcast(message, websocket)
    finally:
        clients.remove(websocket)
        ping_task.cancel()

# Função para transmitir mensagens para todos os clientes
async def broadcast(message, sender):
    for client in clients:
        if client != sender:
            await client.send(message)

# Função para salvar mensagens no arquivo mensagens.txt
def save_message(message):
    with open('mensagens.txt', 'a') as f:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'({now}) {message}\n')

# Função para enviar ping aos clientes
async def ping_clients(websocket):
    try:
        while True:
            await websocket.ping()
            await asyncio.sleep(30)  # 30 segundos
    except websockets.exceptions.ConnectionClosed:
        print(f'Conexão fechada: {websocket.remote_address}')

# Função principal
async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)

    print("Servidor de chat iniciado")

    await server.wait_closed()

# Executa o programa
asyncio.run(main())