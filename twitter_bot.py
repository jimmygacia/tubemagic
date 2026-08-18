import os
import random
import tweepy

# Mengambil kunci rahasia dari GitHub Secrets
api_key = os.environ.get("X_API_KEY")
api_secret = os.environ.get("X_API_SECRET")
access_token = os.environ.get("X_ACCESS_TOKEN")
access_secret = os.environ.get("X_ACCESS_SECRET")

# 10 Variasi pesan tweet (Acak setiap kali posting)
tweets = [
    "Want to grow your YouTube channel faster? 🚀 Check out Tube Magic AI: https://jimmygacia.github.io/tubemagic/ #YouTubeSEO",
    "Struggling with YouTube video ideas & scripts? Tube Magic solves it instantly: https://jimmygacia.github.io/tubemagic/ #ContentCreator",
    "Supercharge your YouTube creation workflow with AI: https://jimmygacia.github.io/tubemagic/ #AITools #YouTuber",
    "Stop overthinking your next video! Generate viral titles & scripts in seconds: https://jimmygacia.github.io/tubemagic/ #YouTubeTips",
    "Scale your channel without burnt out. Let AI handle script writing and optimization: https://jimmygacia.github.io/tubemagic/ #CreatorEconomy",
    "Save hours of planning and creation time on your YouTube channel: https://jimmygacia.github.io/tubemagic/ #VideoMarketing",
    "Looking for the best AI tool designed specifically for YouTubers? Try Tube Magic: https://jimmygacia.github.io/tubemagic/ #DigitalTools",
    "Boost your views and watch time with highly optimized video scripts: https://jimmygacia.github.io/tubemagic/ #YouTubeGrowth",
    "Transform how you create video content today with smart AI assistance: https://jimmygacia.github.io/tubemagic/ #AITools",
    "Ready to take your YouTube channel to the next level? Get started here: https://jimmygacia.github.io/tubemagic/ #ContentStrategy"
]

# Inisialisasi koneksi X API v2
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

# Kirim 1 tweet acak dari daftar di atas
tweet_text = random.choice(tweets)
response = client.create_tweet(text=tweet_text)
print(f"Tweet posted successfully! ID: {response.data['id']}")
