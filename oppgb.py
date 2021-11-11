# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:41:35 2021

@author: casparaarlie
"""


class GuessingGame:

    def __init__(self, question, answers, answer):
        self.question = question
        self.answers = answers
        self.answer = answer

    def __str__(self):
        print(self.question)
        for i in range(len(self.answers)):
            print(f"{i+1}. {self.answers[i]}")
        return " "

    def check_answer(self, number):
        if int(self.answer) == (number):
            return True
        else:
            return False
    
    def correct_answer_txt(self):
        return self.answer
        

def qst(qsts_file):
    qst_list= []
    with open(qsts_file, encoding="UTF8") as qst_file:
        for line in qst_file:
            split_line=line.split(":")
            
            #fikser indeks 2 slik at det blir en egen liste i lista
            split_answers=split_line[2].replace(" ", "").replace("[", "").replace("]", "").split(",")
            
            #gjør at vi får en int som "korrekt svar" i Check_answer 
            split_line[1]=int(split_line[1])
            
            #setter opp en egen liste med linjer som er tilpasset guessing game
            qst_list.append(GuessingGame(split_line[0], split_answers, split_line[1]+1))
        return qst_list    
      

if __name__=="__main__": 
    player1 = 0
    player2 = 0
    qst_list = qst("sporsmaalsfil.txt")
    for question in qst_list:
        print(question)
        for player in range(2):
            if (question.check_answer(int(input("what is the answer? "))))  == True:
                if player == 0:
                    player1 += 1
                elif player == 1:
                    player2 += 1
                else: 
                    pass
            else: 
                pass
        print(f"correct answer was: {question.correct_answer_txt()}\n ")
    print(f"the score is: \nplayer nr1 {player1} \nplayer nr2 {player2}\n")
    if player1>player2:
        print("player nr1 has won")
    elif player1 < player2:
        print("player nr2 has won")
    else:
        print("it is a draw")
        

"""
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
            print("Answer with one of the numbers listed")"""
