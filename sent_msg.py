def sent_msg(msg):
    TOKEN = f'777********43:AAHOR***********cEj4lbJo'  # Указываем Токен, который получили на Шаге 2 от BotFather
    CHATS_ID = [f'-35*****8']   # Указываем ID чата в который планируем отправлять сообщения ботом

    for CHAT_ID in CHATS_ID:  
      url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}&parse_mode=HTML"
      response = requests.get(url)

      if response.status_code == 200:
          print(f"Message sent successfully to {CHAT_ID}")
      else:
          print(f"Failed to send message to {CHAT_ID}: {response.text}")