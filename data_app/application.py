from . import data as d


class Application():

    def __init__(self, *args, **kwargs):
        '''On initiatization creates database, loads data and tests
        addition or update and deletion of record'''

        # database login
        self.database_login('reviews.db')

        # create database and table if non-existent
        self.data_model.create_db_and_primary_table()

        # import CSV file to database
        self.file_import("Womens Clothing E-Commerce Reviews.csv")

    def database_login(self, db_name):
        '''Creates database and table for data'''

        self.db_name = db_name
        self.data_model = d.SQLModel(self.db_name)

    def file_import(self, filename):
        '''Imports CSV file and load records to the database'''

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

    def get_record(self, id):
        try:
            result = self.data_model.get_record(id)
        except Exception as e:
            print('Problem reading file')
            raise e
        else:
            print(f'Result {int(id)}: {result}')

    def insert(self, record):
        '''Handles adding or updating new record(s) to database'''

        try:
            self.data_model.add_record(record)
        except Exception as e:
            print('Problem adding or updating file')
            raise e
        else:
            if not self.data_model.results:
                print(f'''Added record {record['id']}''')
            else:
                print(f'''Updated record {record['id']}''')

    def delete(self, record):
        '''Removes record from database'''

        try:
            self.data_model.delete_record(record)
        except Exception as e:
            print('Problem deleting file')
            raise e
