from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def search_in_corpus(query: str, corpus: dict):
    """
    Perform a search in the corpus using TF-IDF and cosine similarity.
    :param query: Search query string.
    :param corpus: Dictionary of Document objects.
    :return: A list of ranked results (document IDs and scores).
    """
    # Extract document IDs and processed content from the corpus
    doc_ids = list(corpus.keys())
    documents = [' '.join(doc.processed) for doc in corpus.values()]  # Join the list of tokens into a string

    # Add the query to the list for vectorization
    all_text = documents + [query]

    # Vectorize the corpus and the query using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_text)  # TF-IDF matrix for documents + query

    # Compute cosine similarity between query vector and document vectors
    query_vector = tfidf_matrix[-1]  # The last vector corresponds to the query
    doc_vectors = tfidf_matrix[:-1]  # All other vectors are documents
    similarity_scores = cosine_similarity(query_vector, doc_vectors).flatten()

    # Pair document IDs with their similarity scores and sort by score
    ranked_results = sorted(
        zip(doc_ids, similarity_scores),
        key=lambda x: x[1],
        reverse=True
    )

    # Return the ranked results
    return ranked_results






