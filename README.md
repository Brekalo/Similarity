# *Project Name:* Similarity
### *Subtitle of the project:* Find a similar movie

> **Table of Contents:**
> * Code description
> * Installation
> * Usage

#### **Code description:**
* This code uses natural language processing (NLP) techniques to find the most similar movie from a given list of movies, based on the provided movie description. 
* The main function of the project, `find_similar_movie`, takes in a movie description, a list of movie descriptions, a list of movie titles, and a `spaCy` language model, and returns the movie title and description of the movie most similar to the given movie description from the list of movie descriptions.
* In order to use this code, you will need `spaCy` installed and the English language model downloaded, and you simply run `watchMovie.py` after updating the input movie description and movie list.

#### **Installation:**
1. Copy code or Clone the repository:
* `git clone https://github.com/Brekalo/finalCapstone.git`
* `cd finalCapstone`

2. Install the required packages:
* `pip install spacy`
* `python -m spacy download en_core_web_md`

#### **Usage:**
1. Update the `given_movie_description` variable in the `watchMovie.py` file to your desired movie description.
2. Update the `movies.txt` file to contain the list of movies you want to search.
3. Run the `watchMovie.py` file.
