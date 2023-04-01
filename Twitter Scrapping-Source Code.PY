import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import pymongo

st.title("--Twitter data scraping--")
search_term = st.text_input('Enter the hashtag or keyword to search:')
start_date = st.date_input('Enter the start date: ')
end_date = st.date_input('Enter the end date: ')
max_tweets = st.slider('Enter the maximum number of tweets to scrape:', 10, 20, 30, 40)
tweets_list = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"{search_term} since:{start_date} until:{end_date}").get_items()):
    if i > max_tweets:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,
         tweet.lang, tweet.source, tweet.likeCount])
# convert the scraped data into a pandas dataframe
tweets_df = pd.DataFrame(tweets_list, columns=['date', 'id', 'url', 'tweet_content', 'user', 'reply_count',
                                               'retweet_count', 'language', 'source', 'like_count'])
if st.button("Scrape all the Tweets"):
    st.write("Scraping...")
    st.write(tweets_df)

if st.button ("Download as CSV"):
    csv=tweets_df.to_csv()
    st.download_button(label="Download data as CSV", data=csv, file_name='Twitter_data.csv', mime='text/csv', )


if st.button ("Download as JSON"):
    json_string=tweets_df.to_json(orient='records')
    st.download_button(label="Download data as JSON", data=json_string, file_name="Twitter_data.json", mime="application/json", )

if st.button('Upload Tweets to Database'):
    client = pymongo.MongoClient("mongodb+srv://RamaniShankarVB:ramani2000@cluster0.50az78x.mongodb.net/?retryWrites=true&w=majority")
    db = client["DataBase"]
    collection = db["TwitterScrapping"]
    data_dict = tweets_df.to_dict(orient='records')
    collection.insert_many(data_dict)
    st.success('Successfully uploaded to database', icon="✅")
