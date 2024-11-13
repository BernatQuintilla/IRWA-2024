# README: IRWA-2024 Project 3

**Project Overview**

This project, part of the IRWA 2024 course, finds all the documents that contain all the words in the query and sorts them by
their relevance with regard to the query, using different methods.

**Authors**

- Bernat Quintilla (ID: 254530)
- Eugeni Soler (ID: 253566)
- Roger Viader (ID: 252282)

**Requirements**

Before running the code, ensure the following dependencies are installed:
- Python 3.x
- Jupyter Notebook / Google Colab
- Required Libraries: nltk, pandas, numpy, gensim, sklearn, matplotlib

**Dataset**

The dataset used in this project consists of a collection of tweets related to the Farmers' Protest, stored in a JSON file format. If you're running the project in a local environment, ensure the dataset is accessible by adjusting the file paths accordingly. The project also uses several pre-processed data files (stored in pickle format), including:
- `docs_df.pkl`: Original documents data.
- `docs_processed_df.pkl`: Processed text data.
- `tweets_metrics.pickle`: Metrics for tweets (like retweets, likes, and hashtags).

**How to run the script**

After reading the data, cloning the repository and storing the data in the corresponding format, run the cells in order to see the full picture of the code.
