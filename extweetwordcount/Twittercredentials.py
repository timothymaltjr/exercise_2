import tweepy

consumer_key = "pcMKYjdGsOWjcdOUqJ31LpaO6";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "8Ahq11BxzDt1ZN3Hx6wFd81Ua0eQKOAzqhTtXDSQzxLD4CXkxy";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "872491214-apayJ073FxanNvtLatRA3VzQKWAMhv1eOnThJD1A";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "	s5hGT1mcB7KKyemueeqFJPcguurSm7aaM8kZtRQMauOUn";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



