import os
from os.path import join, dirname
from dotenv import load_dotenv

"""
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path,encoding="utf-8_sig")
"""

TOKEN = os.environ.get("API_TOKEN")

API_TOKEN = TOKEN
# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "I dont't understand you."

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']