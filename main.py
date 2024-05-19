import telebot
from telebot import types
import requests
import os
from time import sleep
import warnings


bot = telebot.TeleBot('你的bot token')
admin_id = [管理员1的tg id, 管理员2的tg id]

# apis = ['咪狐:mihu', '卡哇伊:kawayi', '蜜桃:mitao', '套路:taolu', '蛟龙:jiaolong','花蝴蝶:huahudie ', '蜜桃:mitao', 'love:love', '小妲己:xiaodaji', '77直播:77zhibo', '依依:yiyi', '日出:richu', '久久:jiujiu', '彩虹:caihong', '蝶恋:dielian', '夜妖姬:yeyaoji', '樱花:yinghua', '享色:xiangse', '红浪漫:honglangman', '金鱼:jinyu', '桃花:taohua', '花房:huafang', '小仙女:xiaoxiannv', '视觉秀:shijuexiu', '小天使:xiaotianshi', '彩云:caiyun', '暗语:anyu', '咪咪:mimi', '娇媚:jiaomei', '黄瓜:huanggua', '色趣:sequ', '糯米:nuomi', '爱爱你:aiaini', '樱花雨i:yinghuayui', '夜来香:yelaixiang', '爱零:ailing', '盘他:panta', '小蜜蜂:xiaomifeng', '桃花运:taohuayun', '夜色:yese', '蝴蝶:hudie', '小天仙:xiaotianxian', '杏趣:xingqu', '小坏蛋:xiaohuaidan', '飘雪:piaoxue', '樱桃:yingtao', '卡路里:kaluli', '小黄书:xiaohuangshu', '二嫂:ersao', '花果山:huaguoshan', '云鹿:yunlu', '菠萝:boluo', '星宝贝:xingbaobei', '夜艳:yeyan', '兰桂坊:languifang', 'dancelife:dancelife', '小萌猪:xiaomengzhu', '蝴蝶飞:hudiefei', '幽梦:youmeng', '丽柜厅:liguiting', '颜如玉:yanruyu', '橙秀:chengxiu', '豹娱l:baoyul', '小花螺:xiaohualuo', '皇后:huanghou', '心之恋:xinzhilian', '台妹l:taimeil', '亚米:yami', '爱恋:ailian', '903娱乐:903yule', '九尾狐:jiuweihu', '尤物岛:youwudao', '夜女郎:yenulang', '娇喘:jiaochuan', '芒果派:mangguopai', '媚颜:meiyan', '风流:fengliu', '夜律:yelu', '玲珑:linglong', '浴火:yuhuo', '翠鸟:cuiniao', '幸运星:xingyunxing', '她秀:taxiu', '招财猫:zhaocaimao', '双碟:shuangdie', '糖果:tangguo', '么么哒:memeda', '小性感:xiaoxinggan', '小喵宠:xiaomiaochong', '兔女郎:tunulang', '睡美人:shuimeiren', '金呗:jinbei', '美夕:meixi', '小妖:xiaoyao', '约直播:yuezhibo', '花仙子:huaxianzi', '土豪:tuhao', '红妆:hongzhuang', '妞妞:niuniu', '艳后:yanhou', 'moon:moon', '蓝猫:lanmao', '美人妆:meirenzhuang', '入巷:ruxiang', '倾心:qingxin', '小精灵:xiaojingling', '偶遇:ouyu', '灰灰:huihui', '猫头鹰:maotouying', '喜欢你:xihuanni', '夜纯:yechun', '杏播:xingbo', '名流:mingliu', '小辣椒:xiaolajiao', '情趣:qingqu', '小棉袄:xiaomianao']
apis = ['咪狐:mihu', '卡哇伊:kawayi', '蜜桃:mitao', '套路:taolu', '蛟龙:jiaolong','花蝴蝶:huahudie ', '蜜桃:mitao', 'love:love', '小妲己:xiaodaji', '77直播:77zhibo', '依依:yiyi', '日出:richu', '久久:jiujiu', '彩虹:caihong', '蝶恋:dielian', '夜妖姬:yeyaoji', '樱花:yinghua', '享色:xiangse', '红浪漫:honglangman', '金鱼:jinyu', '桃花:taohua', '花房:huafang', '小仙女:xiaoxiannv', '视觉秀:shijuexiu', '小天使:xiaotianshi', '彩云:caiyun', '暗语:anyu', '咪咪:mimi', '娇媚:jiaomei', '黄瓜:huanggua', '色趣:sequ', '糯米:nuomi', '爱爱你:aiaini', '樱花雨i:yinghuayui', '夜来香:yelaixiang', '爱零:ailing', '盘他:panta', '小蜜蜂:xiaomifeng', '桃花运:taohuayun', '夜色:yese', '蝴蝶:hudie', '小天仙:xiaotianxian', '杏趣:xingqu', '小坏蛋:xiaohuaidan', '飘雪:piaoxue', '樱桃:yingtao', '卡路里:kaluli', '小黄书:xiaohuangshu', '二嫂:ersao', '花果山:huaguoshan', '云鹿:yunlu', '菠萝:boluo', '星宝贝:xingbaobei', '夜艳:yeyan', '兰桂坊:languifang', 'dancelife:dancelife', '小萌猪:xiaomengzhu', '蝴蝶飞:hudiefei', '幽梦:youmeng', '丽柜厅:liguiting', '颜如玉:yanruyu', '橙秀:chengxiu', '豹娱l:baoyul', '小花螺:xiaohualuo', '皇后:huanghou', '心之恋:xinzhilian', '台妹l:taimeil', '亚米:yami', '爱恋:ailian', '903娱乐:903yule', '九尾狐:jiuweihu', '尤物岛:youwudao', '夜女郎:yenulang', '娇喘:jiaochuan', '芒果派:mangguopai', '媚颜:meiyan', '风流:fengliu', '夜律:yelu', '玲珑:linglong', '浴火:yuhuo', '翠鸟:cuiniao', '幸运星:xingyunxing', '她秀:taxiu', '招财猫:zhaocaimao', '双碟:shuangdie', '糖果:tangguo', '么么哒:memeda', '小性感:xiaoxinggan', '小喵宠:xiaomiaochong', '兔女郎:tunulang', '睡美人:shuimeiren', '金呗:jinbei', '美夕:meixi', '小妖:xiaoyao', '约直播:yuezhibo', '花仙子:huaxianzi', '土豪:tuhao']
anti_add_group = True

PAGE_SIZE = 98

project_data = {}
current_api = {}
project_counter = 0


@bot.message_handler(commands=['show'])
def send_welcome(message):
    buttons = [types.InlineKeyboardButton(api.split(':')[0], callback_data=f"api|{api}|0") for api in apis]
    buttons = [buttons[i:i + 5] for i in range(0, len(buttons), 5)]
    buttons.append([types.InlineKeyboardButton("❌不想看了", callback_data="close")])
    reply_markup = types.InlineKeyboardMarkup(buttons)
    bot.reply_to(message, "请选择要观看的平台", reply_markup=reply_markup)


def process_api_selection(chat_id, message_id, api, page):
    global project_counter, company
    try:
        api_url = f"http://api.vipmisss.com:81/xcdsw/json{api}.txt"
        response = requests.get(api_url)
        data = response.json()['zhubo']

        start = max(page * PAGE_SIZE, 0)
        end = min(start + PAGE_SIZE, len(data))
        page_data = data[start:end]
        buttons = []
        for i, item in enumerate(page_data):
            project_data[project_counter] = item
            button_text = item['title']
            callback_data = f"item|{project_counter}"
            button = types.InlineKeyboardButton(text=button_text, callback_data=callback_data)
            if i % 2 == 0:
                buttons.append([button])
            else:
                buttons[-1].append(button)
            project_counter += 1

        # navigation_buttons = []
        # if start > 0:
        #     navigation_buttons.append(types.InlineKeyboardButton("⬅️上一页", callback_data=f"api|{api}|{page - 1}"))
        # if end < len(data):
        #     navigation_buttons.append(types.InlineKeyboardButton("下一页➡️", callback_data=f"api|{api}|{page + 1}"))
        # if len(navigation_buttons) > 0:
        #     buttons.append(navigation_buttons)

        back_button = [
            types.InlineKeyboardButton("🏠换个平台", callback_data="home"),
            types.InlineKeyboardButton("❌不想看了", callback_data="close"),
        ]

        buttons.append(back_button)

        markup = types.InlineKeyboardMarkup(buttons)
        company = api.split(':')[0]
        text = f"{company}当前共 {len(data)} 名在线主播，点击按钮预览直播间封面，如果点击按钮获取不到内容，那就是主播离线了。\n\n⚠️*注意：不要点击的太快哦，获取直播源和直播间预览图需要大概一秒钟时间！*"
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=markup, parse_mode='Markdown')
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global company, current_api
    chat_id = call.message.chat.id
    callback_data = call.data.split('|')
    try:
        if callback_data[0] == 'api':
            api, page = str(callback_data[1]).split(':')[1], int(callback_data[2])
            current_api[chat_id] = api
            process_api_selection(chat_id, call.message.message_id, api, page)

        elif callback_data[0] == 'item':
            project_id = int(callback_data[1])
            item = project_data.get(project_id)
            if item:
                title = item['title']
                img = item['img']
                img_name = img.split('/')[-1]
                address = item['address']
                message_text = f"*平台：*`{company}`\n*标题：*`{title}`\n\n*直播源*\n`{address}`\n\n使用*VLC播放器*导入直播源即可观看"

                photo = requests.get(url=img, verify=False).content
                warnings.filterwarnings("ignore")
                if not os.path.exists('./img'):
                    os.makedirs('./img')
                img_path = f'./img/{img_name}.jpg'
                with open(img_path, 'wb') as f:
                    f.write(photo)
                    f.close()
                img_send = open(img_path, 'rb')
                markup = types.InlineKeyboardMarkup()
                back_btn = types.InlineKeyboardButton(text="❌叉出去", callback_data='close')
                markup.add(back_btn)
                bot.send_photo(chat_id=chat_id, photo=img_send, caption=message_text, reply_markup=markup, parse_mode='Markdown')
                img_send.close()

        elif callback_data[0] == 'close':
            bot.delete_message(chat_id, call.message.message_id)
            return

        elif callback_data[0] == 'home':
            send_welcome(call.message)

    except Exception as t:
        print(t)


@bot.message_handler(commands=['set'])
def set(message):
    global anti_add_group
    if message.from_user.id in admin_id:
        anti_add_group = not anti_add_group
        bot.reply_to(message, f"防拉群已{'开启' if anti_add_group else '关闭'}")


@bot.my_chat_member_handler()
def check(message):
    if message.new_chat_member.user.id == bot.get_me().id:
        try:
            if anti_add_group and message.from_user.id not in admin_id:
                chat_id = message.chat.id
                bot.send_message(chat_id, "❌bot已开启防拉群保护，请联系管理员拉群！", timeout=5)
                sleep(1)
                bot.leave_chat(chat_id)
            else:
                pass
        except Exception as t:
            print(t)


if __name__ == '__main__':
    print('=====bot已启动=====')
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            sleep(30)
