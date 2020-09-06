# A utitlity file to ease querying against Reddit for better content
# TODO:
# - Understand what to parse for comments
# - How to configure/tune the parsing and understanding of the content

import praw

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
redditID = os.getenv('REDDIT_ID')
reddit_secret = os.getenv('REDDIT_SECRET')
reddit_refresh = os.getenv('REDDIT_REFRESH')

reddit = praw.Reddit(client_id=redditID, client_secret=reddit_secret,
    refresh_token = reddit_refresh, user_agent='MemeBot')


