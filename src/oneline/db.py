from dotenv import load_dotenv
import os
import logging
import sqlalchemy

load_dotenv()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class DB:
    __instance = None

    def __init__(self):
        """Virtually private constructor."""

        if DB.__instance is not None:
            raise Exception("This class is a singleton, use DB.create()")
        else:
            DB.__instance = self
        self.engine = self.create_engine()

    @staticmethod
    def create():
        if DB.__instance is None:
            DB.__instance = DB()

        return DB.__instance

    def create_engine(self):
        return sqlalchemy.create_engine(
            os.environ["DATABASE_URL"].replace("postgresql://", "cockroachdb://")
        )

    def connect(self):
        return self.engine.connect()
