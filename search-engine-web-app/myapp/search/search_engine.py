import random

from myapp.search.objects import ResultItem, Document
from myapp.search.algorithms import search_in_corpus

# We no longer need build_demo_results as we are using search_in_corpus
def build_demo_results(corpus: dict, search_id):
    """
    Helper method, just to demo the app
    :return: a list of demo docs sorted by ranking
    """
    res = []
    size = len(corpus)
    ll = list(corpus.values())
    for index in range(random.randint(0, 40)):
        item: Document = ll[random.randint(0, size)]
        res.append(ResultItem(item.id, item.title, item.description, item.doc_date,
                              "doc_details?id={}&search_id={}&param2=2".format(item.id, search_id), random.random()))

    # Simulate sort by ranking (This is a placeholder, we'll remove it once we use actual search)
    res.sort(key=lambda doc: doc.ranking, reverse=True)
    return res

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
                                           "doc_details?id={}&search_id={}&param2=2".format(doc.id, search_id), score))

        return result_items

