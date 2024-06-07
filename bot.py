import requests
from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with the token provided by BotFather
bot_token = '7026649860:AAEdozGA0D1uQ1_1uvSmUUnbQnAVnHsN2VE'
bot = Bot(token=bot_token)

# Function to get updates and extract chat_id
def get_chat_id(bot_token):
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(url)
    data = response.json()

    # Debugging: Print the raw response
    print("Raw data from getUpdates:", data)
    
    if 'result' in data:
        results = data['result']
        print("Results found in updates:", results)
        if len(results) > 0:
            chat_id = results[-1]['message']['chat']['id']
            print("Chat ID extracted:", chat_id)
            return chat_id
    print("No results found in updates.")
    return None

# Function to send a message
def send_message(chat_id, message):
    bot.send_message(chat_id="6286297782", text=message)

# Main logic
if __name__ == '__main__':
    chat_id = get_chat_id(bot_token)
    if chat_id:
        message = "Hello, this is a test message from your bot!"
        send_message(chat_id, message)
        print(f'Message sent to chat_id: {chat_id}')
    else:
        print('No chat_id found. Please send a message to your bot first.')
