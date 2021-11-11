# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 22:32:45 2021

@author: Administrator
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
    #generates a list with an indeks for each player
    players=[]
    players_name=[]
    n=int(input("how many players? "))
    for a in range(n):
        players.append(int(0))
        players_name.append(input(f"what is player nr{a+1}`s name? "))
    
    #asks the questions and checs if they are correct if correct they add points to the list of players
    qst_list = qst("sporsmaalsfil.txt")
    for question in qst_list:
        print(question)
        for player in range(len(players)):
            if (question.check_answer(int(input("what is the answer? "))))  == True:
                players[player]=players[player]+1
            else: 
                pass
        print(f"correct answer is: {question.correct_answer_txt()}")
    #checks who has won
    for points in range(len(players)):
        if players[points] == max(players):
            print(f"{players_name[points]} has won")
        else:
            pass