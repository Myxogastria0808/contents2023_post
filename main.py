import tweepy
import settings
import json

#設定
POST_TIMES=40
client = tweepy.Client(
    consumer_key=settings.CONSUMER_KEY,
    consumer_secret=settings.CONSUMER_SECRET,
    access_token=settings.ACCESS_TOKEN,
    access_token_secret=settings.ACCESS_TOKEN_SECRET,
)

#tweet_content
def _tweet_content(id, tag, title, content):
    content = {
        'id': id,
        'tag': tag,
        'title': title,
        'content': content,
    }
    return content

#post
def post_tweet(post_times):
    post_content = [
        "https://github.com/Myxogastria0808/contents2023_post",
        "石黒先生回めっちゃ面白かった",
        "構成的アプローチは、興味深かった",
        "本当に大学の授業をロボットがやるようになったら、面白いな～",
        "触れるって大事だな～",
        "ロボットのボトルネックの1つが皮膚だと知って、意外に思った",
        "テレノイド面白い",
        "なるほど～",
        "ヒューマンロボットインタラクション、興味深いな～",
        "最初から最後までとても楽しめた！"
    ]
    for i in range(1, post_times + 1, 1):
        if i%4==0:
            tweet = json.dumps(
                _tweet_content(id=i, tag='#コンテンツ入門2023', title='石黒先生回', content=post_content[int((i / 4) - 1)]),
                    indent=4,
                    ensure_ascii=False
            )
        else:
            content=f'面白かった！×{i}'
            tweet = json.dumps(
                    _tweet_content(id=i, tag='#コンテンツ入門2023', title='石黒先生回', content=content),
                    indent=4,
                    ensure_ascii=False
            )
        #post
        client.create_tweet(text=tweet)


#実行
exec = post_tweet(post_times=POST_TIMES)
