import unittest
import os
from data_app.application import Application


class TestDatabase(unittest.TestCase):

    def setUp(self):
        '''
        Setup a temporary database
        '''
        # create database
        self.test_app = Application()
        self.test_app.database_login('test_reviews.db')
        self.test_app.data_model.create_db_and_primary_table()

        # insert data
        self.add_record = {'id': 0, 'clothing_id': 1008, 'age': 32, 'title': 'Beautiful',
                           'review_text': '''Love this skirt. the detail is amazing. '
                           'runs small i ordered a 12 i'm usually a 10, but still a '
                           'little snug.''', 'rating': 4, 'recommended_ind': 1,
                           'positive_feedback_count': 0, 'division_name': 'General',
                           'department_name': 'Bottoms', 'class_name': 'Skirts'}
        self.update_record = {'id': 0, 'clothing_id': 1008, 'age': 38, 'title': 'Beautiful',
                              'review_text': '''Love this skirt. the detail is amazing. '
                              'runs small i ordered a 12 i'm usually a 10, but still a '
                              'little snug.''', 'rating': 4, 'recommended_ind': 1,
                              'positive_feedback_count': 0, 'division_name': 'General',
                              'department_name': 'Bottoms', 'class_name': 'Skirts'}

    def test_insert(self):
        self.test_app.data_model.add_record(self.add_record)
        query_result = self.test_app.data_model.get_record(0)
        self.assertEqual(query_result, self.add_record)

    def test_update(self):
        self.test_app.data_model.add_record(self.update_record)
        query_result = self.test_app.data_model.get_record(0)
        self.assertEqual(query_result, self.update_record)

    def test_delete(self):
        self.test_app.data_model.delete_record(self.update_record)
        query_result = self.test_app.data_model.get_record(0)
        self.assertEqual(query_result, {})

    def tearDown(self):
        conn = self.test_app.data_model.connection
        if conn.cursor():
            conn.close()
        os.remove("test_reviews.db")


if __name__ == "__main__":
    unittest.main()
