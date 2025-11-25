from datetime import datetime, timedelta
from user_profile import Profile
from study_session import StudySession
from invite_logic import InviteLogic
from auto_cancel import AutoCancelJob
from flashcards import FlashcardGenerator

def print_welcome_banner():
    banner = r"""
    ================================================
    __        __   _                            _         
    \ \      / /__| | ___ ___  _ __ ___   ___  | |   
     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |_|   
      \ V  V /  __/ | (_| (_) | | | | | |  __/  _ 
       \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_|

    ________________________________________________
    
    Welcome to Study Buddies — let us learn together!
    ________________________________________________
    ================================================
    """
    print(banner)

def main():
    print (print_welcome_banner())



    p1 = Profile(0, "Sam", "Maxey", "CS")
    p1.update_schedule_dict({"Monday": ["9AM", "2PM"], "Wednesday": ["11AM"]})

    p2 = Profile(1, "Jamie", "Johnson", "CE")
    p3 = Profile(2, "Taylor", "Jackson", "BINF")
    p4 = Profile(3, "Jordan", "Michael", "CIS")
    p5 = Profile(4, "Casey", "Brown", "CIS")

    profiles = [p1, p2, p3, p4, p5]

    for profile in profiles:
        if profile.major == "CIS":
            profile.update_schedule_dict({"Tuesday": ["1PM", "3PM"]})
        else:
            profile.update_schedule_dict({"Friday": ["10AM"]})
    print(profile)
    print("Updated schedule:", profile.schedule)
    print("-" * 40)




if __name__ == "__main__":
    main()