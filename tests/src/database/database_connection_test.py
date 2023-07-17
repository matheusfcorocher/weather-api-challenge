import gc
import pytest
import sys
from pymongo import MongoClient

sys.path.append('./src/database')
from database_connection import MongoConnection 


class Test_database_connection:
    """
        Description
        -----------
            This class contains tests cases to check database_connection class
            from database_connection.py.
    """

    @pytest.fixture(scope='function')
    def mongo_connection(self, request):
        """
            Fixture to initiate a instance of MongoConnection.
        """

        connection = MongoConnection(mongo_client=MongoClient)

        # After each test, closes connection fixture
        def fin():
            connection.__del__()

        request.addfinalizer(fin)

        return connection



    def test_get_connection(self, mongo_connection):
        """
            Description
            -----------
                When is given a mongo connection check
                if get_connection returns a mongo_connection
            
            Expected Result
            ---------------
                returns True
        """

        connection = mongo_connection.get_connection()
        assert isinstance(connection, MongoClient)


    def test_get_weather_db(self, mongo_connection):
        """
            Description
            -----------
                When is given a mongo connection check
                if returns weather database
            
            Expected Result
            ---------------
                returns True
        """

        db = mongo_connection.get_weather_db()
        assert db.name == "weather"


    def test_singleton_pattern(self):
        """
            Description
            -----------
                When try to access the same instance of MongoConnection
                it retuns the same connection
            
            Expected Result
            ---------------
                returns True
        """

        mongo_connection1 = MongoConnection(mongo_client=MongoClient)
        mongo_connection2 = MongoConnection(mongo_client=MongoClient)
        assert mongo_connection1 is mongo_connection2