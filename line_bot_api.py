from flask import Flask,request,abort
from linebot import(LineBotApi,WebhookHandler,exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import  *


app= Flask(__name__)

line_bot_api= LineBotApi("Cb1zn5Z1dBNV1osEa7otXndEk3Drfx8FgJdhtMzYyy6zEqzZI/Qck6YKb4qhuQThZcwbL6DM7y4hvAhztthuWlsizsVyuKNMBGNOWe7OGsnQGybzol83rn6zIDMwHAlczfM3RnPEyOxLYKIFwyXlQgdB04t89/1O/w1cDnyilFU=")
handler=WebhookHandler("ec9d3c43144b10b5730b7f6309c5d89b")


