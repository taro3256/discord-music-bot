import discord
import os

# カービィ音楽の一覧
kb_music_files = os.listdir("./kb-sound")
for i, f in enumerate(kb_music_files):
    print(i, f)

# Botのアクセストークン
TOKEN = 'hogehoge'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')

    CHANNEL_ID = 546907679155552281
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('こんにちは！')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視
    if message.author.bot:
        return

    global voich
    # ボイスチャンネル接続
    if message.content.startswith('/connect'):
        voich = await discord.VoiceChannel.connect(message.author.voice.channel)

    # ボイスチャンネル切断
    if message.content.startswith('/discon'):
        await voich.disconnect()

    # 楽曲再生
    if message.content.startswith('/play'):
        if len(message.content) > len('/play'):
            sound = message.content.split(" ")[1]
        else:
            sound = 0
            
        player = await voich.play(discord.FFmpegPCMAudio('kb-sound/' + kb_music_files[sound]))
        player.start()

    if message.content.startswith('/stop'):
        voich.stop()


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)