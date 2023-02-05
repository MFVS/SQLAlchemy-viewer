from sqlalchemy import insert
import tables
def make_test_query(active_table):
    tables = tables.get()
    query_obj = insert(tables["Books"]).values("Some book name", "Release date", 64, 1200)
    return query_obj