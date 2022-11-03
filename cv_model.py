import pickle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from data_app.preprocessing import NLTKPreProcesser
from sklearn.model_selection import train_test_split

# check time duration
from time import time
t0 = time()

# read data and save in dataframe
df = pd.read_csv('data_app/Womens Clothing E-Commerce Reviews.csv')
df_copy = df[['review_text', 'rating']].copy()
df_copy['review_text'] = df_copy['review_text'].fillna('')
df_copy['review_text'] = df_copy['review_text'].apply(lambda x: NLTKPreProcesser(x).text)

# remove neutral review and consider positive reviews all those above 4
df_copy = df_copy[df_copy['rating'] != 3]
df_copy['sentiment'] = df_copy['rating'] >= 4
cv = CountVectorizer()

# train CounterVectorizer model with training data
train_data, test_data = train_test_split(df_copy, train_size=0.8, random_state=0)
X_train = cv.fit_transform(train_data['review_text'])

# save cv model
with open('cv_model.pkl', 'wb') as fh:
    pickle.dump(cv, fh)

print(f'Time elapsed: {time() -t0} sec')
