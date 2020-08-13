import os
from os.path import join, dirname
from dotenv import load_dotenv

"""
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path,encoding="utf-8_sig")
"""

API_TOKEN = os.environ.get('SLACKBOT_API_TOKEN')
# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = os.environ.get('SLACKBOT_DEFAULT_REPLY')
# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ["plugin"]#os.environ.get('SLACKBOT_PLUGINS').split()