
import spacy

def preprocess_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.lower()

def find_similar_movie(given_movie_description):
    # preprocess the input description
    given_movie_description = preprocess_text(given_movie_description)

    # load the English language model 'md' for 'spaCy'
    nlp = spacy.load("en_core_web_md")

    # read the movie descriptions from the file
    with open("movies.txt", "r") as my_file:
        movie_descs = my_file.readlines()

    # preprocess the movie descriptions
    movie_descs = [preprocess_text(desc) for desc in movie_descs]

    # tokenize the input description and the movie descriptions using 'spaCy'
    input_doc = nlp(given_movie_description)
    movie_docs = [nlp(desc) for desc in movie_descs]

    # calculate similarity scores between input description and movie descriptions
    similarity_scores = [input_doc.similarity(movie_doc) for movie_doc in movie_docs]

    # get the index of the movie with the highest similarity score
    max_index = similarity_scores.index(max(similarity_scores))

    # get the title of the most similar movie
    movie_title = movie_descs[max_index].split(":")[0].strip()

    return movie_title


given_movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for Earth, the Illuminati trick the Hulk into a rocketship and launch him into space to a planet where the Hulk can live in peace. Unfortunately, the Hulk lands on the planet Sakaar, where he is sold into slavery and trained as a gladiator."

try:
    similar_movie = find_similar_movie(given_movie_description)
    print(f"\nWe recommend watching this movie: \"{similar_movie}\"")
except TypeError as e:
    print(f"Error: {e}")
