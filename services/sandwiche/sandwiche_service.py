import time
from database import Database


class SandwicheService:
    def __init__(self) -> None:
        pass

    def findSandwiches(self):
        db = Database()
        return db.findAll('sandwiches')
