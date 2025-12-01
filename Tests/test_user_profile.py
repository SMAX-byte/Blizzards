#TOdo 1 test user_profile.py creationCreate 
#TODO 2 5 Profile objects
#and call every one of the Profile methods in the driver.
from user_profile import Profile
from event import Event
from study_session import StudySession
from datetime import datetime
import unittest

class TestProfile(unittest.TestCase):
    def setUp(self):
        self.Sam = Profile("Sam", "CIS", "Physics", "Unknown")

    def test_profile_creation_and_methods(self):
        #test constructor
        self.assertEqual(self.Sam.name, "Sam")
        self.assertEqual(self.Sam.major, "CIS")
        self.assertEqual(self.Sam.minor, "Physics")
        self.assertEqual(self.Sam.schedule, "Unknown")

    def test_update_schedule(self):
        self.Sam.update_schedule({"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]})
        self.assertEqual(self.Sam.schedule, {"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]})
        self.assertIsInstance(self.Sam.schedule, dict)
        self.assertIn("Monday", self.Sam.schedule)
        self.assertEqual(self.Sam.schedule["Monday"], ["9AM", "2PM"])
        self.assertIn("Wednesday", self.Sam.schedule)
        self.assertEqual(self.Sam.schedule["Wednesday"], ["11AM"])

    def test_empty_schedule_update_and_modification(self):
        #Test empty schedule update
        self.Sam.update_schedule({})
        self.assertEqual(self.Sam.schedule, {})

    def test_profile_modification(self):
        #test constructor overwirtes old data
        self.Sam.name = "Samuel"
        self.assertEqual(self.Sam.name, "Samuel")
        self.Sam.major = "Math"
        self.assertEqual(self.Sam.major, "Math")
        self.Sam.minor = "Computer Science"
        self.assertEqual(self.Sam.minor, "Computer Science") 

    def test_str_and_repr_methods(self):
        profile_str = str(self.Sam)
        profile_repr = repr(self.Sam)
        self.assertIsInstance(profile_str, str)
        self.assertIsInstance(profile_repr, str)
        self.assertEqual(profile_str, profile_repr)

    def test_add_event(self):
        event_added = self.Sam.add_event("Math Exam on Friday at 10AM")
        self.assertIn("Math Exam on Friday at 10AM", self.Sam.schedule)
        self.assertTrue(event_added)

    def test_remove_event(self):
        self.Sam.add_event("Math Exam on Friday at 10AM")
        event_removed = self.Sam.remove_event("Math Exam on Friday at 10AM")
        self.assertNotIn("Math Exam on Friday at 10AM", self.Sam.schedule)
        self.assertTrue(event_removed)

if __name__ == '__main__':
    unittest.main()   
