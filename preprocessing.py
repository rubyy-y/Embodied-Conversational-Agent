import string
import nltk
import numpy as np

punctuation = string.punctuation
punctuation += "‘’•“”°½€…´–—·‰«" # add other special characters to filter

lemmatizer = nltk.stem.WordNetLemmatizer()
stop_words = set(nltk.corpus.stopwords.words("english"))

def preprocess(sentence):
    """
    Applies the following transformations to a text/string:
    - remove punctuation marks and other special characters
    - lowercase
    (- remove numbers)
    (- remove stopwords) decide against because text is stort anyway
    - lemmatize
    - tokenize

    returns a list of word strings
    """
    # remove punctuation and lowercase
    sentence = sentence.translate(str.maketrans("", "", punctuation)).lower()
    
    # remove numbers?
    # sentence = re.sub(r"\d+", "", sentence)
    
    # tokenize sentence, remove stopwords, then lemmatize the words
    return [lemmatizer.lemmatize(w) for w in nltk.tokenize.word_tokenize(sentence)] # if w not in stop_words]


def bag_of_words(pat, all_words):
    """
    example: (not real)
    sentence  = ['hey', 'how', 'are', 'you']
    all_words = [ 'hi', 'hey', 'you', 'bye', 'thanks']
    bow       = [    0,     1,     1,     0,        0]
    """
    pat = [preprocess(w) for w in pat]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for i, word in enumerate(all_words):
        if [word] in pat:
            bag[i] = 1.0
    return bag