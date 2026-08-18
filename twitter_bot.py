import os
import random
import tweepy

# Mengambil kunci rahasia dari GitHub Secrets
api_key = os.environ.get("X_API_KEY")
api_secret = os.environ.get("X_API_SECRET")
access_token = os.environ.get("X_ACCESS_TOKEN")
access_secret = os.environ.get("X_ACCESS_SECRET")

# Variasi pesan tweet
tweets = [
    "Want to grow your YouTube channel faster? 🚀 Check out Tube Magic AI: https://jimmygacia.github.io/tubemagic/",
    "Struggling with YouTube video ideas & scripts? Tube Magic solves it instantly: https://jimmygacia.github.io/tubemagic/ #YouTubeSEO",
    "Supercharge your YouTube creation workflow with AI: https://jimmygacia.github.io/tubemagic/ #ContentCreator #AITools"
]

# Inisialisasi koneksi X API v2
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

# Kirim 1 tweet acak
tweet_text = random.choice(tweets)
response = client.create_tweet(text=tweet_text)
print(f"Tweet posted successfully! ID: {response.data['id']}")
