import string
import nltk

punctuation = string.punctuation
punctuation += "‘’•“”°½€…´–—·‰«" # add other special characters to filter

lemmatizer = nltk.stem.WordNetLemmatizer()
stop_words = set(nltk.corpus.stopwords.words("english"))

def preprocess(sentence):
    """
    Applies the following transformations to a text/string:
    - remove punctuation marks and other special characters
    - lowercase
    - remove stopwords
    - lemmatize
    - tokenize
    returns a list of words
    """
    # remove punctuation and make lowercase
    sentence = sentence.translate(str.maketrans("", "", punctuation)).lower()
    
    # remove numbers?
    # sentence = re.sub(r"\d+", "", sentence)
    
    # tokenize sentence remove stopwords, then stem and lemmatize the words
    return [lemmatizer.lemmatize(w) for w in nltk.tokenize.word_tokenize(sentence) if w not in stop_words]