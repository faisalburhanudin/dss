from flask_sqlalchemy import SQLAlchemy


class CerminDB(SQLAlchemy):

    def drop_all(self, bind='__all__', app=None):
        """Drops all tables.

        .. versionchanged:: 0.12
           Parameters were added"""
        self.__memory_only(app=app)

        self._execute_for_all_tables(app, bind, 'drop_all')

    def create_all(self, bind='__all__', app=None):
        """Creates all tables.

        .. versionchanged:: 0.12
           Parameters were added
        """
        self.__memory_only(app=app)

        self._execute_for_all_tables(app, bind, 'create_all')

    def __memory_only(self, app):
        """Override to make sure only drop sqlite memory"""
        database_uri = self.get_app(app).config['SQLALCHEMY_DATABASE_URI']

        if database_uri != "sqlite:///:memory:":
            raise Exception("Cannot drop_all except sqlite:///:memory:")

db = CerminDB()

__all__ = [db]
