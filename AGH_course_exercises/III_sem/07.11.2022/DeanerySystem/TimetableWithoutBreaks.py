from typing import List
from DeanerySystem.day import Day
from DeanerySystem.term_class import Term
from DeanerySystem.lesson_class import Lesson
from DeanerySystem.action import Action

class TimetableWithoutBreaks:
    """ Class containing a set of operations to manage the timetable """
    all_lessons = [] # all lessons list
##########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        given_date = term
        

##########################################################

    def busy(self, term: Term) -> bool:
        for lesson in TimetableWithoutBreaks.all_lessons:
            if lesson.term == term:
                return True
        return False

 ##########################################################

    def put(self, lesson: Lesson) -> bool:
        pass

##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        pass

##########################################################

    def get(self, term: Term = None) -> Lesson:
        if not term:
            return
        lesson = Lesson()
        lesson.term = term
        return lesson