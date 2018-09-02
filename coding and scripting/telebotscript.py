# This is python language.
# This script is for the communication between raspberry pi and telegram bot.


import telepot
import picamera

chat_id = "id of telegram user"
bot = telepot.Bot('"BOT\'S TOKEN GOES HERE"')

def handle(msg):

    chat_id = "id of telegram user"
    command = msg['text']

    print('Got command: ' + str(command))

    if command == '/snap':
        bot.sendMessage(chat_id, 'Request sent. Please wait :)')
        print('Capturing photo...')
        camera = picamera.PiCamera()
        camera.capture('/home/pi/Desktop/photobot/photo.jpg' )
        camera.close()
        print('Sending photo to ' + str(chat_id))
        bot.sendPhoto(chat_id, photo = open('/home/pi/Desktop/photobot/photo.jpg', 'rb'))
        bot.sendMessage(chat_id, 'Photo sent!')
        print('Photo sent to telegram.')


    elif command == '/start':
        bot.sendMessage(chat_id, 'Welcome my master, everything is good to go!')

    elif command == '/status':
        bot.sendMessage(chat_id, 'Device ready!')


bot.message_loop(handle)

print ('Bot ready')
