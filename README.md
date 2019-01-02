# TwitterFriendsActivity
Last activity of your Twitter friends

The script creates an HTML file with all your friends on Twitter with the followings details: Username, Last tweet, Date of the last tweet.
You can use it to verify wich friends are inactive and can unfollow them.

All the variables are stored in settings.conf.
- Username: Your Twitter username
For the next 4 variables follow the guid from Twitter to get the API keys: https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html
- AppKey:
- AppSecret:
- OAuthToken:
- OAuthTokenSecret:
- SleepTime:2 - Time in seconds to sleep between API interogation (default is 2 to avoid being blocked by Twitter for too many interogations)
- Verbose:1 - Shows on the console the data that will be written on the HTML file. 0 - disabled, 1 - enabled (default)

