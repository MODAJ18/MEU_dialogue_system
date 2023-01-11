from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


## helper functions and variables
STOPWORDS = set(stopwords.words('english'))

def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

lemmatizer = WordNetLemmatizer()
wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
def lemmatize_words(text):
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN))
                     for word, pos in pos_tagged_text])



## main text cleaning function
def text_clean(text):
    text = text.lower().strip()
    # text = str(TextBlob(text).correct())
    # text = lemmatize_words(text)
    # text = remove_stopwords(text)
    return text

def prepare_data(df):
    # feature selection
    data = df[["transcription", "action", "object", "location"]]
    # text cleaning
    data["transcription_clean"] = data["transcription"].apply(lambda x: text_clean(x))
    return data


from sklearn.feature_extraction.text import TfidfVectorizer
def get_tfidf(df_col):
    tfidf_vectorizer = TfidfVectorizer()
    values = tfidf_vectorizer.fit_transform(df_col)
    # feature_names = tfidf_vectorizer.get_feature_names_out()
    return values, tfidf_vectorizer

from sklearn import preprocessing
def encode_label(df_col):
    le_y = preprocessing.LabelEncoder()
    y_encoded = le_y.fit_transform(df_col)

    return y_encoded, le_y

def split(X, y, test_size=0.2, stratify=True):
    if stratify == True:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                            random_state=110, stratify=y)
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                            random_state=110)
    return X_train, X_test, y_train, y_test
