from slackbot.bot import respond_to # @botname: で反応するデコーダ
from slackbot.bot import listen_to # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply # 該当する応答がない場合に反応するデコーダ
import datetime
import functions


@respond_to('今何時？')
def mention_func(message):
  dt_now = datetime.datetime.now() #現在の日時を取得
  message.reply(dt_now.strftime('%H時%M分') + 'だよ！') # メンションをつけて現在の時刻を投稿
@listen_to('今何時？')
def listen_func(message):
  message.send('時間を知りのですか？') # ただの投稿
  message.reply('メンションをつけて直接聞いてください') # メンション
@respond_to("hello kume")
def hello(message):
  message.reply("hello")
@respond_to("ニュース")
def send_news(message):
  news = functions.get_news()
  message.reply(news)