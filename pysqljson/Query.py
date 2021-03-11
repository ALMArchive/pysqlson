import pypika
from pysqljson import Parser

parser = Parser.Parser()


class Query:
    query = None
    allowed_props = []

    def __init__(self, table, allowed_props):
        self.allowed_props = allowed_props
        self.query = pypika.Query.from_(table)

    def select(self, props, jsn):
        return parser.parse(self.query.select(*props), jsn, self.allowed_props)
