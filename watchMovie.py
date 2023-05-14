import spacy

def preprocess_text(text, nlp):
    if not isinstance(text, str):
        raise TypeError("You must enter a string of text")
    
    # parsed the text using the 'spaCy'
    parsed_text = nlp(text)

    # removed stop words and punctuation, and lemmatize the words
    preprocessed_words = [
        token.lemma_.lower() for token in parsed_text
        if not token.is_stop and not token.is_punct
    ]
    return preprocessed_words


def find_similar_movie(given_movie_description, movie_descriptions, movie_titles, nlp):
    # preprocess movie descriptions
    preprocessed_movies = [preprocess_text(
        desc.lower(), nlp) for desc in movie_descriptions]

    # vectorized movie descriptions used 'spaCy'
    vectorized_movies = [nlp(" ".join(movie)) for movie in preprocessed_movies]

    # vectorize the given movie description
    given_movie_description = given_movie_description.lower()
    vectorized_given_movie = nlp(
        " ".join(preprocess_text(given_movie_description, nlp)))

    # calculate similarity scores between the given movie and other movies
    similarity_scores = [vectorized_given_movie.similarity(
        movie) for movie in vectorized_movies]

    # find the index of the movie with the highest similarity score
    max_index = similarity_scores.index(max(similarity_scores))

    # return the title and description of the similar movie
    return movie_titles[max_index].strip(), movie_descriptions[max_index].strip()


# load the English language model 'md' for 'spaCy'
nlp = spacy.load("en_core_web_md")

# read movie descriptions and titles from 'movies.txt'
with open("movies.txt", "r") as my_file:
    movies = my_file.readlines()
movie_descriptions = [desc.split(":")[1].strip() for desc in movies]
movie_titles = [desc.split(":")[0] for desc in movies]

given_movie_description = "When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

similar_movie_title, similar_movie_description = find_similar_movie(
    given_movie_description, movie_descriptions, movie_titles, nlp)

print(f"\nWe recommend watching this movie: \"{similar_movie_title}\"")
print(f"The description of the recommended movie is: \"{similar_movie_description}\"")