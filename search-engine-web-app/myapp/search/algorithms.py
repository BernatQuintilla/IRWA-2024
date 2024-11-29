from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def search_in_corpus(query: str, corpus: dict, score_threshold=0.1):
    """
    Perform a search in the corpus using TF-IDF and cosine similarity.
    :param query: Search query string.
    :param corpus: Dictionary of Document objects.
    :param score_threshold: Minimum score to filter documents.
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

    # Tokenize the query for matching terms in documents
    query_tokens = set(query.lower().split())

    # Filter and rank the results based on score and query term presence
    ranked_results = []
    for doc_id, score in zip(doc_ids, similarity_scores):
        if score > score_threshold:  # Filter by score threshold
            document_tokens = set(corpus[doc_id].processed)  # Document's tokens
            if query_tokens & document_tokens:  # Check if any query term is in the document
                ranked_results.append((doc_id, score))

    # Sort the results by score in descending order
    ranked_results.sort(key=lambda x: x[1], reverse=True)

    return ranked_results







