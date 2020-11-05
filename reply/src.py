import subprocess

from slackbot.bot import listen_to

@listen_to('ドア|非常階段')
def door_open_request(message):
    subprocess.call([f'aplay', './sound.wav'], shell = True)
    message.reply('チャイムを鳴らしました。')
