# This is python language.
# This script is for motion detection, its notification alerting and the sending process to the telegram.

import P3picam
import picamera
import telepot
import time

motionState = False
chat_id = "id of telegram user"
bot = telepot.Bot('"BOT\'S TOKEN GOES HERE"')

while True:
    motionState = P3picam.motion()
    print('Motion detected!')

    if motionState:
        bot.sendMessage(chat_id, 'Motion detected! Press /snap to take photo')
        print('Alert sent to telegram.')
        time.sleep(5)



