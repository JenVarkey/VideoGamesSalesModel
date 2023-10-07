import psycopg2
import utils as u

class VGsales:

    def __init__(self) -> None:
        self.conn = psycopg2.connect(host="localhost", database="linear_regression", user="postgres", password="***")
