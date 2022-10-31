import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import warnings
warnings.filterwarnings('ignore')


class PreProcesser():
    def __init__(self, text):
        self.text = text
        # lowercase
        self.text = self.text.lower()
        # remove digits
        self.text = re.sub(r'\d+', '', self.text)
        # remove puncuations
        self.text = re.sub(r'[^\w\s]', '', self.text)


class NLTKPreProcesser(PreProcesser):
    def __init__(self, text):
        super().__init__(text)
        # remove stopwords
        self.text = " ".join([w for w in self.text.split() if w not in
                             set(stopwords.words("english"))])
        # get the lemma for each word
        self.text = " ".join([WordNetLemmatizer().lemmatize(w) for w in self.text.split()])


class SpacyPreProcesser(PreProcesser):
    def __init__(self, text):
        super().__init__(text)
        nlp = spacy.load("en_core_web_sm", disable=["tok2vec", "textcat", "ner"])
        self.text = nlp(self.text)
        # remove stopwords
        self.text = [token for token in self.text if not token.is_stop]
        # get the lemma for each word
        self.text = [str(token.lemma_) for token in self.text]
        self.text = " ".join(self.text)


if __name__ == "__main__":
    text = "Hello, how are you today? I hope you don't find this case study too dificult!"
    preprocess0 = PreProcesser(text)
    preprocess1 = NLTKPreProcesser(text)
    preprocess2 = SpacyPreProcesser(text)
    print(preprocess0.text)
    print(preprocess1.text)
    print(preprocess2.text)
