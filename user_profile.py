# Implement Profile Class
#Attributes: name, major, minor, schedule
#Methods: update_schedule()

#Create a Profile class that has attributes: id(int), first_name(str), last_name(str), schedule(list[Event]), major(str).  
# Create a constructor and a __str__ method.  The first and last names must be formatted in Titlecase.  
# The major must be formatted in TITLECASE.  The schedule must begin as an empty list.

class Profile:
    Valid_majors = {'CS', 'CIS', 'CE', 'CE', 'BINF'}

    def __init__(self, id, first_name, last_name, major, schedule=None):

        self.id = int(id)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.major = major.upper()
        if self.major not in self.Valid_majors:
            raise ValueError(f"Invalid major: {self.major}. Valid majors are: {', '.join(self.Valid_majors)}")
        self.schedule = schedule if schedule is not None else []

    def update_schedule(self, new_event):
        self.schedule.append(new_event)
    

    def __str__(self):
        return f"Profile(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, major={self.major}, schedule={self.schedule})"
















# class Profile:
#     def __init__(self, name, major, minor, schedule=None):
#         self.name = name
#         self.major = major
#         self.minor = minor
#         self.schedule = schedule if schedule is not None else []

#     def update_schedule(self, new_schedule):
#         self.schedule = new_schedule

#     def __repr__(self):
#         return f"Profile(name={self.name}, major={self.major}, minor={self.minor}, schedule={self.schedule})"
