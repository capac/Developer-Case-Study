import sqlite3
import csv
import os


class SQLModel:
    '''SQL database values'''

    # create table if it doesn't exists
    create_table_command = ('CREATE TABLE IF NOT EXISTS reviews '
                            '(id REAL PRIMARY KEY, '
                            'clothing_id REAL NOT NULL, '
                            'age REAL NOT NULL, '
                            'title TEXT, '
                            'review_text TEXT, '
                            'rating REAL NOT NULL, '
                            'recommended_ind REAL NOT NULL, '
                            'positive_feedback_count REAL NOT NULL, '
                            'division_name TEXT, '
                            'department_name TEXT, '
                            'class_name TEXT)')

    # insert entry in table
    insert_command = ('INSERT INTO reviews VALUES (:id, '
                      ':clothing_id, :age, :title, :review_text, '
                      ':rating, :recommended_ind, :positive_feedback_count, '
                      ':division_name, :department_name, :class_name)')

    # update entry in table
    update_command = ('UPDATE reviews SET clothing_id=:clothing_id, '
                      'age=:age, '
                      'title=:title, '
                      'review_text=:review_text, '
                      'rating=:rating, '
                      'recommended_ind=:recommended_ind, '
                      'positive_feedback_count=:positive_feedback_count, '
                      'division_name=:division_name, '
                      'class_name=:class_name '
                      'WHERE id=:id')

    # delete record from table
    delete_command = ('DELETE FROM reviews WHERE id=:id')

    # create or connect to a database
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row

    def query(self, query, parameters=None):
        cursor = self.connection.cursor()
        try:
            if parameters is not None:
                cursor.execute(query, parameters)
            else:
                parameters = {}
                cursor.execute(query, parameters)
        except (sqlite3.Error) as e:
            self.connection.rollback()
            raise e
        else:
            self.connection.commit()
            if cursor.description is not None:
                result = [dict(row) for row in cursor.fetchall()]
                return result
        finally:
            cursor.close()

    # only upon first run of the application
    def create_db_and_primary_table(self):
        '''Creates database and table if they don't already exist'''
        self.query(self.create_table_command)

    def get_record(self, id):
        query = ('SELECT * FROM reviews WHERE id=:id')
        result = self.query(query, {"id": id})
        return result[0] if result else {}

    def add_record(self, record):
        query_id = record['id']
        self.results = self.get_record(query_id)
        # if no previous record exists then add it
        if not self.results:
            query = self.insert_command
        # if the record exists then update it
        else:
            query = self.update_command
        self.query(query, record)

    def delete_record(self, record):
        # delete record information
        query_id = record['id']
        delete_result = self.get_record(query_id)
        if not delete_result:
            print(f'Cannot delete record {query_id}, not in database')
        else:
            delete_query = self.delete_command
            self.query(delete_query, record)
            print(f'Record {query_id} deleted from database')


class CSVModel:
    '''CSV file retrieval and storage'''

    def __init__(self, filename, filepath=None):

        if filepath:
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            self.filename = os.path.join(filepath, filename)
        else:
            self.filename = filename

    def load_records(self):
        '''Reads in all records from the CSV file and returns a list'''

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r', encoding='utf-8') as fh:
            # turning fh into a list is necessary for the unit tests
            csvreader = csv.DictReader(list(fh.readlines()))
            return list(csvreader)
