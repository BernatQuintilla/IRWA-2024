import random

from myapp.search.objects import ResultItem, Document
from myapp.search.algorithms import search_in_corpus

class SearchEngine:
    """Educational search engine"""
    def search(self, search_query, search_id, corpus):
        print("Search query:", search_query)

        # Now we are using the real search functionality, not the demo results
        results = search_in_corpus(search_query, corpus)  # Call to search algorithm

        # We need to return the results as ResultItem objects, as per your initial setup
        result_items = []
        for doc_id, score in results:
            doc = corpus[doc_id]  # Get the document from corpus using the doc_id
            result_items.append(ResultItem(doc.id, doc.title, doc.description, doc.doc_date,
                                           "doc_details?id={}".format(doc.id), doc.url, score, doc.retweets, doc.likes))

        return result_items

