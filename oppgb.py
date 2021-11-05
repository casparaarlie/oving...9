# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:41:35 2021

@author: stian
"""


class GuessingGame:

    def __init__(self, question, answers, answer):
        self.question = question
        self.answers = answers
        self.answer = answer

    def __str__(self):
        print(self.question)
        counter = 0
        for i in range(len(self.answers)):
            counter += 1
            print(f"{counter}. {self.answers[i]}")
        return " "

    def check_answer(self, number):
        if self.answer == number:
            return True
        else:
            return False


if __name__ == "__main__":
    question_1 = GuessingGame("What has three legs?",
                              ["Egg", "Donut", "Peacock"], 2)
    question_2 = GuessingGame("What time is it?",
                              ["It's High Noon", "2 o'clock", "3:03",
                               "Why should I answer?"], 1)
    questions = [question_1, question_2]
    cont = True
    while cont:
        try:
            for question in questions:
                print(question)
                print(question.check_answer(int(input("What is the answer?"))))
                print("\n")
            # print(question_1)
            # print(question_1.check_answer(int(input("What is the answer?"))))
            # print(question_2)
            # print(question_2.check_answer(int(input("What is the answer?"))))
            cont = False
        except ValueError:
            print("Answer with one of the numbers listed")
