#TOdo 1 test user_profile.py creationCreate 
# TODO 2 5 Profile objects
#and call every one of the Profile methods in the driver.
from Blizzards.user_profile import Profile
from Blizzards.event import Event
Sam = Profile("Sam", "CIS", "Physics", "Unknown")

def test_profile_creation_and_methods():
    #test constructor
    assert Sam.name == "Sam"
    assert Sam.major == "CIS"
    assert Sam.minor == "Physics"
    assert Sam.schedule == "Unknown"

def test_update_schedule():
    Sam.update_schedule({"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]})
    assert Sam.schedule == {"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]}
    assert isinstance(Sam.schedule, dict)
    assert "Monday" in Sam.schedule
    assert Sam.schedule["Monday"] == ["9AM", "2PM"]
    assert "Wednesday" in Sam.schedule
    assert Sam.schedule["Wednesday"] == ["11AM"]

def test_empty_schedule_update_and_modification():
    #Test empty schedule update
    Sam.update_schedule({})
    assert Sam.schedule == {}

def test_profile_modification():
    #test constructor overwirtes old data
    Sam.name = "Samuel"
    assert Sam.name == "Samuel"
    Sam.major = "Math"
    assert Sam.major == "Math"
    Sam.minor = "Computer Science"
    assert Sam.minor == "Computer Science"
    
def test_remove_event(self):
        # Create events
        e1 = Event("Study Loops", datetime(2024, 9, 10))
        e2 = Event("Study Loops", datetime(2024, 9, 12))
        e3 = Event("Trees", datetime(2024, 9, 15))

        # Add them to the profile schedule
        self.profile.schedule = [e1, e2, e3]

        # Remove all events matching e1.what ("Study Loops")
        removed = self.profile.remove_event(e1)

        # Assertions
        self.assertTrue(removed)
        self.assertEqual(len(self.profile.schedule), 1)
        self.assertEqual(self.profile.schedule[0].what, "Trees")
