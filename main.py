from Class_1 import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "none"
TWITTER_EMAIL = "tanvir.python.test@gmail.com"
TWITTER_PASSWORD = "v%Fyr8Ea$o4y6X8(Y"

twitter_bot = InternetSpeedTwitterBot()

twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()

