from line_bot_api import *


def about_us_event(event):
    emoji = [
            {
                "index":0,
                "productId":"5ac2197b040ab15980c9b43d",
                "emojiId":"002"
            },
            {
                "index":17,
                "productId":"5ac2197b040ab15980c9b43d",
                "emojiId":"006"
            }
    ]
    text_message = TextSendMessage(text='''$ Master Finance $
Hello! 您好，歡迎您成為 小天地 的好友！
                                   
我是小天地 財經小幫手
                                   
-這裡有股票、匯率資訊哦～
-直接點選下方[圖中]選單功能
                                   
期待您的光臨''',emojis=emoji)
    sticker_message = StickerMessage(
        package_id='8522',
        sticker_id='16581271'
    )
    buttons_template = TemplateSendMessage(
                alt_text="小幫手 template",
                template=ButtonsTemplate(
                    title="選擇服務",
                    text="請選擇",
                    thumbnail_image_url="https://i.imgur.com/Ssns07Ub.jpg",
                    actions=[
                        MessageTemplateAction(
                            label="油價查詢",
                            text="油價查詢"
                        ),
                        MessageTemplateAction(
                            label="匯率查詢",
                            text="匯率查詢"
                        ),
                        MessageTemplateAction(
                            label="股價查詢",
                            text="股價查詢"
                        )
                    ]
                )
            )

    line_bot_api.reply_message(
            event.reply_token,
            [text_message,sticker_message,buttons_template])
    
def push_msg(event,msg):
    try:
        user_id=event.source.user_id
        line_bot_api.push_message(user_id,TextSendMessage(text=msg))
    except:
        room_id=event.source.room_id
        line_bot_api.push_message(room_id,TextSendMessage(text=msg))
def Usage(event):
    push_msg(event,"🔍查詢方法🔍  \
             \n\
             \n 🔗小幫手可以查詢油價➡匯率➡股票🔗 \
             \n\
             \n💈 油價通知➡輸入查詢股票💸\
             \n💈 匯率通知➡輸入查詢匯率📈\
             \n💈 匯率兌換➡換匯USD/TWD💱\
             \n💈 股價查詢➡輸入#+股價代號 #💰 ")