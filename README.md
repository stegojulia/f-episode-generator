# friends-episode-generator
Friends episode generator

# description
This is a Flask app to generate a Friends episode based on the words provided by the user and the show transcripts.

# how to use

Insert a word to describe an element. For example, if you enter 'janice' the generator will select several episodes that feature Janice the most and will suggest one of them for you to watch.

- test.py is the Flask application
- friends.py is the pre-processing script for pulling the transcripts from https://fangj.github.io/friends/ and tokenising them.
- friends_tokens and friends_titles are pickled data files containing the tokenised transcripts and episode titles


# project status
This is the first version of the app. The next steps include:
- improve the relevance of the suggestions by using TF-IDF for keyword extraction
- enable combining keywords
- keyword suggestions
- negative search (search for episodes without an element)