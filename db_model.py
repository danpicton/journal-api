import sqlite3

class DbConnection:
    def __init__(self):
        self.conn = sqlite3.connect("pank.db")
        self.c = self.conn.cursor()
        self.create_log_table()


    def create_log_table(self):

        self.c.execute('drop table log_table;')

        self.c.execute(
            """
            CREATE TABLE log_table (
                id integer primary key,
                log_stamp integer unique,
                log_type text,
                log_source text,
                log_entry text
            );
            """
        )

    def make_log_entry(self, log_stamp: str, source: str, log_type: str, log_entry: str):
        self.c.execute(
            """
            INSERT INTO log_table (
                log_stamp,
                log_type,
                log_source,
                log_entry
            ) VALUES ({0}, '{1}', '{2}', '{3}');
            """.format(log_stamp, log_type, source, log_entry)
        )

        self.conn.commit()

    def get_log_range(self, low_stamp: int, high_stamp: int):
        self.c.execute(
            """
            select 
                log_stamp,
                log_type,
                log_source,
                log_entry
            from
                log_table
            where
                log_stamp between {0} and {1}
            """.format(low_stamp, high_stamp)
        )

        print("pook: " + str(self.c.fetchone()))

a = DbConnection()
a.make_log_entry(123, "blah2", "blah3", "blah4")
a.get_log_range(120, 125)