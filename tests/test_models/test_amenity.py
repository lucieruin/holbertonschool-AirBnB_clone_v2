#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest
from models.place import Place
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def setUpClass(cls):
        """ Set up the database connection before the tests """
        if getenv("HBNB_TYPE_STORAGE") == "db":
            cls.engine = create_engine('sqlite:///:memory:')
            Base.metadata.create_all(cls.engine)
            cls.Session = sessionmaker(bind=cls.engine)
        else:
            cls.engine = None

    @classmethod
    def tearDownClass(cls):
        """ Tear down the database connection after the tests """
        if cls.engine is not None:
            Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """ Create a new session and add sample data before each test """
        if self.engine is not None:
            self.session = self.Session()
            Base.metadata.create_all(self.engine)
            self.amenity = Amenity(name="Sample Amenity")
            self.place = Place(name="Sample Place")
            self.session.add_all([self.amenity, self.place])
            self.session.commit()

    def tearDown(self):
        """ Rollback the session and close after each test """
        if self.engine is not None:
            self.session.rollback()
            self.session.close()

    def test_amenity_relationship(self):
        """ Test the relationship between Amenity and Place """
        if self.engine is not None:
            self.place.amenities.append(self.amenity)
            self.session.commit()
            self.assertEqual(len(self.place.amenities), 1)
            self.assertEqual(self.place.amenities[0], self.amenity)


if __name__ == '__main__':
    unittest.main()
