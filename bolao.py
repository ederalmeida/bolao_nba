import whatsbot

cestinha = whatsbot.WhatsappBot()
ultima_msg_recebida = ''
while True:
    msg_recebida = cestinha.EscutaMensagens()
    if msg_recebida != ultima_msg_recebida:
        ultima_msg_recebida = msg_recebida
        print(msg_recebida)