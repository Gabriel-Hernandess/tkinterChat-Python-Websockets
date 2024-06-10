import tkinter as tk
import asyncio
import websockets
import threading

global nome

def enviar_mensagem():
    global nome
    mensagem = mensagem_entry.get()
    if mensagem:
        chat_text.config(state=tk.NORMAL)
        chat_text.insert(tk.END, f"Você: {mensagem}\n", "enviado")
        chat_text.config(state=tk.DISABLED)
        mensagem_entry.delete(0, tk.END)
        # Enviar mensagem para o servidor
        try:
            mensagem = f'{nome}: {mensagem}'
            asyncio.run(send_message_to_server(mensagem))
        except Exception as e:
            print("Erro ao enviar mensagem:", e)

async def send_message_to_server(message):
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(message)

def iniciar_chat():
    global nome
    nome = nome_entry.get()
    if nome:
        nome_entry.pack_forget()
        nome_button.pack_forget()
        chat_text.pack(fill=tk.BOTH, expand=True)
        mensagem_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        enviar_button.pack(side=tk.RIGHT)
        nome_label.configure(text=f"Chat iniciado como {nome}")
        # Iniciar thread para receber mensagens do servidor
        threading.Thread(target=receber_mensagens).start()

def receber_mensagens():
    global nome
    async def receive_messages():
        async with websockets.connect('ws://localhost:8765') as websocket:
            while True:
                try:
                    mensagem = await websocket.recv()
                    
                    # Verificar se a mensagem é enviada pelo próprio cliente
                    if mensagem.split(": ")[0] != nome:
                        tag = "recebido"
                        
                        # Adicionar a mensagem com a tag apropriada
                        chat_text.config(state=tk.NORMAL)
                        chat_text.insert(tk.END, mensagem + "\n", tag)
                        chat_text.config(state=tk.DISABLED)
                    
                except Exception as e:
                    print("Erro ao receber mensagem:", e)
                    break
    asyncio.run(receive_messages())

# Criar uma instância da janela principal
root = tk.Tk()
root.title("Chat Tkinter")
root.geometry("450x550")

# Barra para digitar o nome
nome_label = tk.Label(root, text="Digite seu nome:")
nome_label.pack(pady=5)
nome_entry = tk.Entry(root)
nome_entry.pack(pady=5)
nome_button = tk.Button(root, text="Iniciar Chat", command=iniciar_chat)
nome_button.pack(pady=5)

# Bloco de texto para exibir mensagens
chat_text = tk.Text(root, state=tk.DISABLED)
chat_text.pack(fill=tk.BOTH, expand=True)

# Barra para digitar mensagem
mensagem_entry = tk.Entry(root)
enviar_button = tk.Button(root, text="Enviar", command=enviar_mensagem)

# Configurar estilos de texto
chat_text.tag_config("enviado", foreground="green")
chat_text.tag_config("recebido", foreground="blue")

# Executar o loop principal da interface gráfica
root.mainloop()