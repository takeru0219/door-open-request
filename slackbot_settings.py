# coding: utf-8

import os
import subprocess

subprocess.call(['source', '../setting_intercom.sh'], shell = True)

API_TOKEN = os.environ['BOT_TOKEN_INTERCOM']

DEFALLT_REPLY = 'すみません、よくわかりません。'

PLUGINS = ['reply']