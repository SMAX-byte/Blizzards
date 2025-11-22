#TOdo 1 test user_profile.py creationCreate 
# TODO 2 5 Profile objects
#and call every one of the Profile methods in the driver.
from user_profile import Profile
def test_profile_creation_and_methods():
    #test profile creation
    Sam = Profile("Sam", "CIS", "Physics", "Unknown")
    #test constructor
    assert Sam.name == "Sam"
    assert Sam.major == "CIS"
    assert Sam.minor == "Physics"
    assert Sam.schedule == "Unknown"
    #test update_schedule method
    Sam.update_schedule({"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]})
    assert Sam.schedule == {"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]}
    print("Profile creation and methods test passed.")