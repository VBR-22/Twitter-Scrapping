# Twitter-Scrapping
Interative GUI using streamlit for twitter scraping

REQUIRED SKILLS:

1.Python scripting
2.MongoDB
3.Streamlit
4.Snscrape

OVERVIEW:

I have Created a GUI using streamlit that contains the follwing features

Can enter any keyword or Hashtag to be searched,
Select the starting date
Select the ending date
Maximum Number of tweets needs to be scrapped.

After scraping is done, it has the following options

Display All the Scrappping Tweets
Download Scrapped data in CSV Format
Download Scrapped data as JSON Format
Upload Scrapped data to DATABASE in Mongodb Atlas

WORKING:

Step1: Initially I get the Keyword, Start date, End date, and Number of tweets from the user using streamlit.

Step 2: Then the above details are given to TwitterSearchScrape. A dataframe is created to store the entire scraped data Now we can download this scraped data in the form of CSV or JSON format

Step3: The database connection is established using pymongo and mongoClient.A new collection will be created in the Mongodb database and data is uploaded into that collection if the user wish to upload
