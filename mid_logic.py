import db_model
import time


def get_epoch():
    return int(time.time())


class JournalSevrice:
    def __init__(self):
        self.model = db_model.DbConnection()

    def new_entry(self, log_entry, log_stamp=get_epoch(), source="dev", log_type="none"):
        self.model.make_log_entry(log_stamp, source, log_type, log_entry)

    def log_range(self, low_stamp=get_epoch() - 604800, high_stamp=get_epoch()):
        return self.model.get_log_range(low_stamp, high_stamp)

    def log(self, log_stamp):
        return self.model.get_log_entry(log_stamp)

a = JournalSevrice()
# a.new_entry("blah2", 131, "blah3", "blah4")
# a.new_entry("boeulah2", 134, "bouelah3", "bloeuah4")
# a.new_entry( "blah2", 138, "blah3", "blah4")
print(a.log(131))