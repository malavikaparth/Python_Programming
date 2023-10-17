
# Advanced Programming Concepts Project: Quiz

class Quiz(object):
    def __init__(self):
        self.points_tally = 0

# class Quiz(object):

class History(Quiz):
    def __init__(self):
       # self.points_tally = 0
        Quiz.__init__(self)

    def question1(self):
        answer = 'a'
        print('What special substance do mother koalas feed their young?')
        print('(a)  pap') # answer
        print('(b)  1947')
        print('(c)  1918')
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1


        else:
            print("Answer is incorrect")
        print('Points tally for the History segment is ', self.points_tally)
        return ' '

    def question2(self):
        answer = 'b'
        print('What is unique about a wombat\'s droppings?')
        print('(a)  They are purple')
        print('(b)  Cube shaped')
        print('(c)  Glow in dark')
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
        print('Points tally for the History segment is ', self.points_tally)
        return ' '

    def question3(self):
        answer = 'c'
        print('How are platypuses are different from most other mammals?')
        print('(a)  Cold Blooded')
        print('(b)  Have pouches')
        print('(c)  Lay eggs')
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
        print('Points tally for the History segment is ', self.points_tally)
        return ' '

    def question4(self):
        answer = 'b'
        print('The quokka is a type of?')
        print('(a)  Rodent')
        print('(b)  Marsupial')
        print('(c)  Lemur')
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
        print('Points tally for the History segment is ', self.points_tally)
        return ' '

    def question5(self):
        answer = 'a'
        print('What are baby echidnas called?')
        print('(a)  Kids ')  #answer
        print('(b)  Joeys')
        print('(c)  Echidnettes')
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
        print('Points tally for the History segment is ', self.points_tally)
        return ' '

    def getHistoryQuestion(self, number):

        if number == 1:
            History.question1(self)
        elif number == 2:
            History.question2(self)
        elif number == 3:
            History.question3(self)
        elif number == 4:
            History.question4(self)
        elif number == 5:
            History.question5(self)
        else:
            print("Invalid choice. Please try again.")

class Sports(Quiz):
    def __init__(self):
      #self.points_tally = 0
      Quiz.__init__(self)

    def question1(self):
        answer = 'c'
        print('How many moons does Mars have?')
        print('(a)  13')
        print('(b)  50')
        print('(c)  2')     # answer
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
        print('Points tally for the sports segment is', self.points_tally)
        return ' '

    def question2(self):
        answer = 'c'
        print(" ")
        print('Where is asteroid belt')
        print('(a)  Between earth and venus')
        print('(b)  Between Earth and Mars')    #answer
        print('(c)  Between Jupiter and Marse')
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
        print('Points tally for the sports segment is ', self.points_tally)
        return ' '

    def question3(self):
        #def question3():
        answer = 'a'
        print('What is the great red spot on jupiter?')
        print('(a)  A storm')    #answer
        print('(b)  A lake')
        print('(c)  A volcano')
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
        print('Points tally for the sports segment is ', self.points_tally)
        return ' '
    def question4(self):
    #def question4():
        print('What is sun made of')
        print('(a)  Molten iron')
        print('(b)  Gas')
        print('(c)  Liquid lava')

        answer = 'b'
        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")

        print('Points tally for the sports segment is ', self.points_tally)
        return ' '

    def question5(self):
    #def question5():
        answer = 'c'
        print('Oberon and Titania are moons of?')
        print('(a)  Venus')
        print('(b)  Jupiter') #answer
        print('(c)  Uranus')

        selection1 = input('Choose a, b or c: ')
        if selection1 == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
        print('Points tally for the sports segment is ', self.points_tally)
        return ' '

#def getSportsQuestion(self, number):
    def getSportsQuestion(self, number):

        if number == 1:
            Sports.question1(self)
        elif number == 2:
            Sports.question2(self)
        elif number == 3:
            Sports.question3(self)
        elif number == 4:
            Sports.question4(self)
        elif number == 5:
            Sports.question5(self)
        else:
            print("Invalid choice. Please try again.")


quiz = Quiz()
sports_seg = Sports()
history_seg = History()
score = 0

sp_questions_left = 2
h_questions_left = 2
questions_left = sp_questions_left + h_questions_left
sp_questions_answered = [False, False, False, False, False]
h_questions_answered = [False, False, False, False, False]
num_sp_ques = len(sp_questions_answered)
num_h_ques = len(sp_questions_answered)

while questions_left > 0:
    print('\nCategories')
    print('1. Solar System')
    print('2. Animal')
    category = int(input("Choose a category (1-2): "))
    if category == 1:
        choice = int(input("\nChoose a question between 1 and 5: "))
        if sp_questions_answered[choice-1] == True:
            print('This question has already been answered. Please choose another question')
            print('Questions left are:')
            for i in range(num_sp_ques):
                if sp_questions_answered[i]== False:
                    print(i+1)
            print()
        else:
            sp_questions_answered[choice-1] = True
            sports_seg.getSportsQuestion(choice)
            questions_left -= 1
            sp_questions_left -=1
    elif category == 2:
        choice = int(input("\nChoose a question between 1 and 5: "))
        if h_questions_answered[choice-1] == True:
            print('This question has already been answered. Please choose another question')
            print('Questions left are:')
            for i in range(num_h_ques):
                if h_questions_answered[i] == False:
                    print(i + 1)
            print()
        else:
            h_questions_answered[choice - 1] = True
            history_seg.getHistoryQuestion(choice)
            questions_left -= 1
            h_questions_left -=1

    else:
        print('Invalid entry. Please try again')

total_points = sports_seg.points_tally + history_seg.points_tally
#total_points = quiz.points_tally
print('Total points is ', total_points)

print("End of game.")