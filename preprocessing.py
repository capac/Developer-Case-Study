import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


class PreProcessing():
    def __init__(self, text):
        self.text = text
        # lowercase
        self.text = self.text.lower()
        # remove digits
        self.text = re.sub(r'\d+', '', self.text)
        # remove puncuations
        self.text = re.sub(r'[^\w\s]', '', self.text)


class PreProcessWithSpacy(PreProcessing):
    def __init__(self, text):
        super().__init__(text)
        # remove stopwords
        text = " ".join([w for w in text.split() if w not in
                        set(stopwords.words("english"))])
        # get the lemma for each word
        text = " ".join([WordNetLemmatizer().lemmatize(w) for w in text.split()])


class PreProcessWithNLTK(PreProcessing):
    def __init__(self, text):
        super().__init__(text)
        nlp = spacy.load("en_core_web_sm", disable=["tok2vec", "textcat", "ner"])
        return nlp(text)
