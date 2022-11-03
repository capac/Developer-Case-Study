from data_app.application import Application

app = Application()

# read record
app.get_record('0')

# insert new record / update existing record test
app.insert({'id': 23487, 'clothing_id': 1104, 'age': 25,
            'title': 'Please make more like this one!',
            'review_text': 'This dress fits perfectly!',
            'rating': 5, 'recommended_ind': 1, 'positive_feedback_count': 22,
            'division_name': 'General Petite', 'department_name': 'Dresses',
            'class_name': 'Dresses'})

# delete record test
app.delete({'id': 23488})
