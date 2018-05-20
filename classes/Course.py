# 'Course' class Definitions

class Course(object):
    """ Class representing a Course at school.
        Note: the concatenation of the course type and id results in the full
        course code.
        Example: 
            Course Code = ACCT 3401
                Course Type = ACCT
                Course Id = 3401

    attributes:
        name: A String representing the name of the course.
        type: A String representing the the type of the course.
        id: A String representing the id (numeric) of the course.
        desc: A String representing the description of the course.
        credits: An Integer representing how many credits this course is worth.
    """ 

    def __init__(self, name, type, id, desc, credits):
        """Inits a Course object whose name is *name*,
        id is *id*, course description is *desc*,
        and the number of credits is *credits*.
       
        Args:
            name: A String representing the name of the course.
            type: A String representing the the type of the course.
            id: A String representing the id (numeric) of the course.
            desc: A String representing the description of the course.
            credits: An Integer representing this course's credits.

        Returns:
            A Course Object
       """
        self.name = name
        self.type = type
        self.id = id
        self.desc = desc
        self.credits = credits

         
    
