import pandas as pd
import pickle
from myapp.core.utils import load_json_file
from myapp.search.objects import Document
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stemmer = PorterStemmer()
try:
    stop_words = set(stopwords.words("english"))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words("english"))
_corpus = {}

def build_terms(line):
    line= line.lower()
    line= line.split()
    line= [token for token in line if token not in stop_words]
    line= [token for token in line if not (token.startswith("http") or token.startswith("#") or token.startswith("@"))]
    line = ' '.join(line)
    line = re.sub(r'[^a-zA-Z\s]', ' ', line)
    line= line.split()
    line= [stemmer.stem(token) for token in line]
    return line

def load_corpus(path) -> list[Document]:
    """
    Load file and transform to dictionary with each document as an object for easier treatment when needed for displaying
     in results, stats, etc.
    :param path:
    :return:
    """
    try:
       # If preloaded, load the tweets
        _corpus = pickle.load(open("loaded_corpus_processed.pickle", 'rb'))
        print("CORPUS LOADED SUCCESSFULY FROM MEMORY")
        return _corpus
    except:
        _corpus = {}
        df = _load_corpus_as_dataframe(path)
        # Process files
        df["Tweet Processed"] = df["Tweet"].apply(build_terms) 
        # TODO: Enxtend
        # df["Keywords Extended"] = df["Tweet Processed"] (word2vec expand query)
        df.apply(_row_to_doc_dict, axis=1)
        print("CORPUS LOADED SUCCESSFULY")
        with open("loaded_corpus_processed.pickle", 'wb') as handle:
            pickle.dump(_corpus, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return _corpus


def _load_corpus_as_dataframe(path):
    """
    Load documents corpus from file in 'path'
    :return:
    """
    json_data = load_json_file(path)
    tweets_df = _load_tweets_as_dataframe(json_data)
    tweets_df = _clean_hashtags_and_urls(tweets_df)
    # Rename columns to obtain: Tweet | Username | Date | Hashtags | Likes | Retweets | Url | Language
    corpus = tweets_df.rename(
        columns={"id": "Id", "content": "Tweet", "username": "Username", "date": "Date",
                 "likeCount": "Likes",
                 "retweetCount": "Retweets", "lang": "Language"})
    # select only interesting columns
    filter_columns = ["Id", "Tweet", "Username", "Date", "Hashtags", "Likes", "Retweets", "Url", "Language"]
    corpus = corpus[filter_columns]
    return corpus


def _load_tweets_as_dataframe(json_data):
    data = pd.DataFrame(json_data)
    # parse user data as new columns and rename some columns to prevent duplicate column names
    data = pd.concat([data.drop(['user'], axis=1), data['user'].apply(pd.Series).rename(
        columns={"created_at": "user_created_at", "id": "user_id", "id_str": "user_id_str", "lang": "user_lang"})],
                     axis=1)

    return data

def _build_url(row):
    url = ""
    try:
        for possible_url in row["url"]:
            if row["id"] in possible_url:
                url = possible_url  # tweet URL
    except:
        pass
    return url


def _clean_hashtags_and_urls(df):
    df["Hashtags"] = df["content"].apply(lambda row : [words for words in row.split() if words[0]=='#'])
    # The below line raises errors, update it with a simpler one
    # df["Hashtags"] = df["hashtags"].apply(_build_tags)
    df["Url"] = df.apply(lambda row: _build_url(row), axis=1)
    # df["Url"] = "TODO: get url from json"
    # df.drop(columns=["entities"], axis=1, inplace=True)
    return df


def load_tweets_as_dataframe2(json_data):
    """Load json into a dataframe

    Parameters:
    path (string): the file path

    Returns:
    DataFrame: a Panda DataFrame containing the tweet content in columns
    """
    # Load the JSON as a Dictionary
    tweets_dictionary = json_data.items()
    # Load the Dictionary into a DataFrame.
    dataframe = pd.DataFrame(tweets_dictionary)
    # remove first column that just has indices as strings: '0', '1', etc.
    dataframe.drop(dataframe.columns[0], axis=1, inplace=True)
    return dataframe


def load_tweets_as_dataframe3(json_data):
    """Load json data into a dataframe

    Parameters:
    json_data (string): the json object

    Returns:
    DataFrame: a Panda DataFrame containing the tweet content in columns
    """
    # Load the JSON object into a DataFrame.
    dataframe = pd.DataFrame(json_data).transpose()
    # select only interesting columns
    filter_columns = ["id", "content", "date", "retweetCount", "likeCount", "lang"] #, "entities"]
    dataframe = dataframe[filter_columns]
    return dataframe


def _row_to_doc_dict(row: pd.Series):
    _corpus[row['Id']] = Document(row['Id'], 
                                  row['Tweet'][0:100], row['Tweet'], 
                                  row['Date'],
                                  row['Likes'], row['Retweets'],
                                  row['Url'], row['Hashtags'], row["Tweet Processed"])
