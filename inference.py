import joblib


class PredictReviewSentiment():
    '''Make predictons from sentiment model'''
    def __init__(self, message):
        self.message = message
        # load the model
        self.model = joblib.load('model.pkl')
        self.cv_model = joblib.load('cv_model.pkl')

    def make_prediction(self):
        data = [self.message]
        vect = self.cv_model.transform(data).toarray()
        my_prediction = self.model.predict(vect)
        return my_prediction[0]


if __name__ == "__main__":
    message1 = '''I am a great fan of Uniqlo styling and quality but \
        this was not for me. I'm a size 10 and XS usually fits well but \
        this was huge. Also the fabric was rather stiff and bulky. \
        Sadly, it went back. I liked the idea of a warm over \
        shirt for the winter but it didn't work for me.'''
    message2 = 'Lovely because it goes under other clothes without showing because \
        of the ballet neck. Warm without being bulky'
    pred1 = PredictReviewSentiment(message1)
    pred2 = PredictReviewSentiment(message2)
    print(f'Output 1: {pred1.make_prediction()}')
    print(f'Output 2: {pred2.make_prediction()}')
