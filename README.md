# finalCapstone
##### Compulsory Task 2

# Similarity

### *Find a similar movie*

* ***find_similar_movie*** is the main function in this code, which takes in a movie description, a list of movie descriptions, a list of movie titles, and a *spaCy* language model (NLP), and returns the movie title and description of the movie most similar to the given movie description from the list of movie descriptions. 
* First, the function preprocesses the movie descriptions by removing stop words and punctuation, lemmatizing the words to be vectorized, and then vectorizing both the given and preprocessed movie descriptions. 
* The function calculates similarity scores between the given movie description and the preprocessed movie descriptions using the vectorized representations, determines the movie whose similarity score is highest in the list, then returns the movie's title and description in the input list with that index. 
* The rest of the code loads the *spaCy* language model, reads in a list of movie descriptions and titles from a file, and calls the ***find_similar_movie*** function with a given movie description and the lists of movie descriptions and titles, and prints out the title and description of the movie that is most similar to the given movie description.
* Code was updated for error handling, so the ***preprocess_text()*** function was added for preprocessing input texts and movie descriptions.
* The function will raise a TypeError if the input to ***find_similar_movie()*** is not a string.
* In addition, if a TypeError occurs in the function call, a ***try-except*** block is added to handle the error.
