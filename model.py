import pandas as pd
from preprocessing import NLTKPreProcesser

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import LinearSVC
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import ComplementNB
from sklearn.metrics import roc_curve, auc
# from sklearn.neural_network import MLPClassifier
# from sklearn.svm import SVC
# from sklearn.metrics import confusion_matrix


df1 = pd.read_csv('Womens Clothing E-Commerce Reviews.csv', index_col=0)
df = df1[['Review Text', 'Rating', 'Class Name', 'Age']]

df['Review Text'] = df['Review Text'].fillna('')
df['Review Text'] = df['Review Text'].apply(lambda x: NLTKPreProcesser(x).text)

# CountVectorizer() converts a collection
# of text documents to a matrix of token counts
vectorizer = CountVectorizer()
# assign a shorter name for the analyze
# which tokenizes the string
analyzer = vectorizer.build_analyzer()


def wordcounts(s):
    c = {}
    # tokenize the string and continue, if it is not empty
    if analyzer(s):
        d = {}
        # find counts of the vocabularies and transform to array
        w = vectorizer.fit_transform([s]).toarray()
        # vocabulary and index (index of w)
        vc = vectorizer.vocabulary_
        # items() transforms the dictionary's (word, index) tuple pairs
        for k, v in vc.items():
            d[v] = k  # d -> index:word
        for index, i in enumerate(w[0]):
            c[d[index]] = i  # c -> word:count
    return c


# add new column to the dataframe
df['Word Counts'] = df['Review Text'].apply(wordcounts)

# Rating of 4 or higher -> positive, while the ones with
# Rating of 2 or lower -> negative
# Rating of 3 -> neutral
df = df[df['Rating'] != 3]
df['Sentiment'] = df['Rating'] >= 4
# print(df.head())

# split data
train_data, test_data = train_test_split(df, train_size=0.8, random_state=0)
# select the columns and prepare data for the models
X_train = vectorizer.fit_transform(train_data['Review Text'])
y_train = train_data['Sentiment']
X_test = vectorizer.transform(test_data['Review Text'])
y_test = test_data['Sentiment']

# lr = LogisticRegression()
# lr.fit(X_train, y_train)
lda = ComplementNB(alpha=0.3)
lda.fit(X_train, y_train)

# pred_lr = lr.predict_proba(X_test)[:, 1]
# fpr_lr, tpr_lr, _ = roc_curve(y_test, pred_lr)
# roc_auc_lr = auc(fpr_lr, tpr_lr)
# print(roc_auc_lr)

pred_lda = lda.predict_proba(X_test)[:, 1]
fpr_lda, tpr_lda, _ = roc_curve(y_test, pred_lda)
roc_auc_lda = auc(fpr_lda, tpr_lda)
print(roc_auc_lda)

# LogisticRegression: 0.9376004575323043
# LinearSVC: no predict_proba with LinearSVC
# GaussianNB: 0.5474236999350638
# ComplementNB(alpha=0.0): 0.7447193146547358
# ComplementNB(alpha=0.1): 0.9422103337960286
# ComplementNB(alpha=0.2): 0.9455888047564295
# ComplementNB(alpha=0.3): 0.9463579117939674  ******
# ComplementNB(alpha=0.4): 0.9457162942266334
# ComplementNB(alpha=1.0): 0.9349809659412476
# MultinomialNB(alpha=0.1): 0.9422103337960287
# MultinomialNB(alpha=0.2): 0.9455888047564296
# MultinomialNB(alpha=0.3): 0.9463579117939673  ******
# MultinomialNB(alpha=0.4): 0.9457162942266335
# MultinomialNB(alpha=0.5): 0.9447625061808562
# MultinomialNB(alpha=1.0): 0.796092507312772
