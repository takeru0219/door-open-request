import subprocess

from slackbot.bot import listen_to

@listen_to('ドア開けて')
def door_open_request(message):
    # subprocess.call([f'aplay {filename}.wav'], shell = True)
    message.reply('チャイムを鳴らしました。')
