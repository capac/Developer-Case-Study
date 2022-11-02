from . import data as d
from sqlite3 import IntegrityError


class Application():

    def __init__(self, *args, **kwargs):
        '''On initiatization creates database, loads data and tests
        addition, update and deletion of record'''

        # database login
        self.database_login()

        # create database and table if non-existent
        self.data_model.create_db_and_primary_table()

        # import CSV file to database
        self.file_import("Womens Clothing E-Commerce Reviews.csv")

        # insert record test
        self.insert({'id': 23486, 'clothing_id': 1104, 'age': 25,
                     'title': 'Please make more like this one!',
                     'review_text': 'This dress fits perfectly!',
                     'rating': 5, 'recommended_ind': 1, 'positive_feedback_count': 22,
                     'division_name': 'General Petite', 'department_name': 'Dresses',
                     'class_name': 'Dresses'})

        # delete record test
        self.delete({'id': 23487, 'clothing_id': 1104, 'age': 52,
                     'title': 'Please make more like this one!',
                     'review_text': 'This dress fits perfectly!',
                     'rating': 5, 'recommended_ind': 1, 'positive_feedback_count': 22,
                     'division_name': 'General Petite', 'department_name': 'Dresses',
                     'class_name': 'Dresses'})

    def database_login(self):
        '''Creates database and table for data'''

        self.db_name = 'reviews.db'
        self.data_model = d.SQLModel(self.db_name)

    def file_import(self, filename):
        '''Imports CSV file and load records to the database'''

        try:
            if filename:
                try:
                    csv_read = d.CSVModel(filename=filename, filepath='data_app/')
                except Exception as e:
                    print('Problem reading file')
                    raise e
                else:
                    try:
                        records = csv_read.load_records()
                        for row in records:
                            self.data_model.add_record(row)
                    except TypeError:
                        print('Cannot add data to table')
            else:
                raise Exception("File doesn't exist")
        except IntegrityError:
            pass

    def insert(self, record):
        '''Handles adding or updating new record(s) to database'''

        try:
            self.data_model.add_record(record)
        except Exception as e:
            print('Problem reading file')
            raise e

    def delete(self, record):
        '''Removes record from database'''

        try:
            self.data_model.delete_record(record)
        except Exception as e:
            print('Problem deleting file')
            raise e
