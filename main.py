# Advanced Programming Concepts Project: Quiz

class Quiz(object):
    def __init__(self):
        self.points_tally = 0
        self.lives = 3  # Number of answers the player can get wrong, after which the player loses the game.


# This class contains code related to the section 'History' of the quiz.
class History(Quiz):
    def __init__(self):
        Quiz.__init__(self)
        self.lives_used = 0

    def question1(self):
        answer = 'a'
        print('In what year did world war 2 end?')
        print('(a)  1945')  # answer
        print('(b)  1947')
        print('(c)  1918')
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1
        print('Points tally for the History segment is ', self.points_tally)
        return ' '


    def question2(self):
        answer = 'c'
        print('When was the UN established?')
        print('(a)  March 20, 1956')
        print('(b)  July 8, 1930')
        print('(c)  October 24, 1945')
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1
        print('Points tally for the History segment is ', self.points_tally)
        return ' '

    def question3(self):
        answer = 'a'
        print('When did the Berlin Wall fall?')
        print('(a)  Nov 9, 1989')
        print('(b)  May 7, 1956')
        print('(c)  June 12, 1941')
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1

        print('Points tally for the History segment is ', self.points_tally)
        return ' '

    def question4(self):
        answer = 'b'
        print('When did the EU become a reality?')
        print('(a)  September 2, 1965')
        print('(b)  Nov 1, 1993')
        print('(c)  October ,1, 2001')
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            self.lives_used += 1
            print("Answer is incorrect")
        print('Points tally for the History segment is ', self.points_tally)
        return ' '

    def question5(self):
        answer = 'a'
        print('In what year did Google begin')
        print('(a)  Sep 4 1998 ')  # answer
        print('(b)  May 14, 1992')
        print('(c)  Nov 10, 2004')
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1
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
        Quiz.__init__(self)
        self.lives_used = 0

    def question1(self):
        answer = 'c'
        print('How many NBA championships did Michael Jordan playing for  the Chicago Bulls?')
        print('(a)  3')
        print('(b)  8')
        print('(c)  6')  # answer
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1
        print('Points tally for the sports segment is', self.points_tally)
        return ' '

    def question2(self):
        answer = 'b'
        print(" ")
        print('Who’s the fastest sprinter alive?')
        print('(a)  Michael Johnson')
        print('(b)  Usain Bolt')  # answer
        print('(c)  Tyson Gay')
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1
        print('Points tally for the sports segment is ', self.points_tally)
        return ' '

    def question3(self):
        # def question3():
        answer = 'a'
        print('Which country won the FIFA world cup in 2018?')
        print('(a)  France')  # answer
        print('(b)  Italy')
        print('(c)  Spain')
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1
        print('Points tally for the sports segment is ', self.points_tally)
        return ' '

    def question4(self):
        # def question4():
        print('Which team won the T20 world cup 2020?')
        print('(a)  England')
        print('(b)  West Indies')
        print('(c)  Australia')  # answer

        answer = 'c'
        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1
        print('Points tally for the sports segment is ', self.points_tally)
        return ' '

    def question5(self):
        # def question5():
        answer = 'b'
        print('Who won the female segment of the US open female singles tennis competition in 2021?')
        print('(a)  Serena Williams')
        print('(b)  Emma Raducanu')  # answer
        print('(c)  Ashley Bartley')

        selection1 = input('Choose a, b or c: ')
        if selection1.lower() == answer:
            print(" You're correct")
            self.points_tally += 1
        else:
            print("Answer is incorrect")
            self.lives_used += 1
        print('Points tally for the sports segment is ', self.points_tally)
        return ' '

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

class Cultural(Quiz):
        def __init__(self):
            Quiz.__init__(self)
            self.lives_used = 0

        def question1(self):
            answer = 'c'
            print('In what country is it considered a compliment to shup loudly while eating soup?')
            print('(a)  Iceland')  # answer
            print('(b)  Russia')
            print('(c)  Japan')
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1


            else:
                print("Answer is incorrect")
            print('Points tally for the Cultural segment is ', self.points_tally)
            return ' '

        def question2(self):
            answer = 'b'
            print('In which country would showing up half an hour late for an invitation is considered rude?')
            print('(a)  Greece')
            print('(b)  Switzerland')
            print('(c)  Panama')
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")
            print('Points tally for the Cultural segment is ', self.points_tally)
            return ' '

        def question3(self):
            answer = 'a'
            print('Which country has been labelled the second most diverse country in the world?')
            print('(a)  India')
            print('(b)  China')
            print('(c)  United States of America')
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")
            print('Points tally for the Cultural segment is ', self.points_tally)
            return ' '

        def question4(self):
            answer = 'b'
            print('The word KETCHUP comes from KOETSIAP which is from which language ?')
            print('(a)  Swedish')
            print('(b)  Malay')
            print('(c)  Hindi')
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")
            print('Points tally for the Cultural segment is ', self.points_tally)
            return ' '

        def question5(self):
            answer = 'a'
            print('What is the Thai word for free ?')
            print('(a)  Thai ')
            print('(b)  Mai')
            print('(c)  Fee')
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")
            print('Points tally for the Cultural segment is ', self.points_tally)
            return ' '

        def getCulturalQuestion(self, number):

            if number == 1:
                Cultural.question1(self)
            elif number == 2:
                Cultural.question2(self)
            elif number == 3:
                Cultural.question3(self)
            elif number == 4:
                Cultural.question4(self)
            elif number == 5:
                Cultural.question5(self)
            else:
                print("Invalid choice. Please try again.")

        class Food(Quiz):
            def __init__(self):
                Quiz.__init__(self)
                self.lives_used = 0

        def question1(self):
            answer = 'a'
            print(" ")
            print('What vegetable is also called a courgette')
            print('(a)  Zucchini')
            print('(b)  Onions')
            print('(c)  Tomotoes')
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")
            print('Points tally for the food segment is', self.points_tally)
            return ' '

        def question2(self):
            answer = 'b'
            print(" ")
            print('Which country did brie cheese originate from?')
            print('(a) Greece')
            print('(b) France')  # answer
            print('(c) Germany')
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")
            print('Points tally for the food segment is ', self.points_tally)
            return ' '

        def question3(self):
            # def question3():
            answer = 'a'
            print('How many curries usually accompany rice at traditional South Indian festivities?')
            print('(a)  Seven')  # answer
            print('(b)  Eight')
            print('(c)  Nine')
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")
            print('Points tally for the food segment is ', self.points_tally)
            return ' '

        def question4(self):
            # def question4():
            print('What year did the first Taco Bell open?')
            print('(a)  1962')
            print('(b)  1972')
            print('(c)  1982')

            answer = 'a'
            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")

            print('Points tally for the food segment is ', self.points_tally)
            return ' '

        def question5(self):
            # def question5():
            answer = 'b'
            print('An enchilada is from which cuisine?')
            print('(a)  Chinese')
            print('(b)  Mexican')  # answer
            print('(c)  Italian')

            selection1 = input('Choose a, b or c: ')
            if selection1.lower() == answer:
                print(" You're correct")
                self.points_tally += 1
            else:
                print("Answer is incorrect")
            print('Points tally for the food segment is ', self.points_tally)
            return ' '

            # def getSportsQuestion(self, number):

        def getFoodQuestion(self,number):


           if number == 1:
             Food.question1(self)
           elif number == 2:
             Food.question2(self)
           elif number == 3:
             Food.question3(self)
           elif number == 4:
             Food.question4(self)
           elif number == 5:
              Food.question5(self)
           else:
              print("Invalid choice. Please try again.")


class Food(Quiz):
    def __init__(self):
        # self.points_tally = 0
        Quiz.__init__(self)

    # Main part of program.

class Main(Quiz):
            def __init__(self):
                Quiz.__init__(self)
                self.sports_seg = Sports()
                self.history_seg = History()
                self.cultural_seg = Cultural()
                self.food_seg = Food()
                self.quiz = Quiz()
                self.score = 0
                self.sp_questions_left = 5
                self.h_questions_left = 5
                self.ct_questions_left = 5
                self.f_questions_left = 5
                self.questions_left = self.sp_questions_left + self.h_questions_left
                self.sp_questions_answered = [False, False, False, False, False]
                self.h_questions_answered = [False, False, False, False, False]
                self.ct_questions_answered = [False, False, False, False, False]
                self.f_questions_answered = [False, False, False, False, False]

                self.choices_chosen = [False, False, False]

                self.num_categories = 3  # These categories include the choice 'Exit.'
                self.num_sp_ques = len(self.sp_questions_answered)
                self.num_h_ques = len(self.sp_questions_answered)
                self.num_ct_ques = len(self.sp_questions_answered)
                self.num_f_ques = len(self.sp_questions_answered)


def category1(self):
    # category1(sp_questions_left,sp_questions_answered, num_sp_ques, questions_left, sports_seg, quiz )
    while self.sp_questions_left > 0:
        valid_choice = False
        while valid_choice == False:
            choice = int(input("\nChoose a question between 1 and 5: "))
            if self.sp_questions_answered[choice - 1] == True:
                print('This question has already been answered. Please choose another question')
                print('Questions left are:')
                for i in range(self.num_sp_ques):
                    if self.sp_questions_answered[i] == False:
                        print(i + 1)
            else:
                self.sp_questions_answered[choice - 1] = True
                self.sports_seg.getSportsQuestion(choice)
                self.questions_left -= 1
                self.sp_questions_left -= 1
                valid_choice = True

        if self.quiz.lives <= self.sports_seg.lives_used + self.history_seg.lives_used + self.cultural_seg.libes_used + self.food_seg.lives_used:
            print("All lives lost.")
            self.sp_questions_left = 0
            self.questions_left = 0


def category2(self):
    while self.h_questions_left > 0:
        valid_choice = False
        while valid_choice == False:
            choice = int(input("\nChoose a question between 1 and 5: "))
            if self.h_questions_answered[choice - 1] == True:
                print('This question has already been answered. Please choose another question')
                print('Questions left are:')
                for i in range(self.num_h_ques):
                    if self.h_questions_answered[i] == False:
                        print(i + 1)
                print()
            else:
                self.h_questions_answered[choice - 1] = True
                self.history_seg.getHistoryQuestion(choice)
                self.questions_left -= 1
                self.h_questions_left -= 1
                valid_choice = True

        if self.quiz.lives <= self.sports_seg.lives_used + self.history_seg.lives_used + self.cultural_seg.libes_used + self.food_seg.lives_used:
            print("All lives lost.")
            self.h_questions_left = 0
            self.questions_left = 0

def category3(self):
    while self.ct_questions_left > 0:
        valid_choice = False
        while valid_choice == False:
            choice = int(input("\nChoose a question between 1 and 5: "))
            if self.ct_questions_answered[choice - 1] == True:
                print('This question has already been answered. Please choose another question')
                print('Questions left are:')
                for i in range(self.num_ct_ques):
                    if self.ct_questions_answered[i] == False:
                        print(i + 1)
                print()
            else:
                self.ct_questions_answered[choice - 1] = True
                self.cultural_seg.getCulturalQuestion(choice)
                self.questions_left -= 1
                self.ct_questions_left -= 1
                valid_choice = True

        if self.quiz.lives <= self.sports_seg.lives_used + self.history_seg.lives_used + self.cultural_seg.libes_used + self.food_seg.lives_used:
            print("All lives lost.")
            self.ct_questions_left = 0
            self.questions_left = 0

def category4(self):
    while self.f_questions_left > 0:
        valid_choice = False
        while valid_choice == False:
            choice = int(input("\nChoose a question between 1 and 5: "))
            if self.f_questions_answered[choice - 1] == True:
                print('This question has already been answered. Please choose another question')
                print('Questions left are:')
                for i in range(self.num_f_ques):
                    if self.f_questions_answered[i] == False:
                        print(i + 1)
                print()
            else:
                self.f_questions_answered[choice - 1] = True
                self.food_seg.getFoodQuestion(choice)
                self.questions_left -= 1
                self.f_questions_left -= 1
                valid_choice = True

        if self.quiz.lives <= self.sports_seg.lives_used + self.history_seg.lives_used + self.cultural_seg.libes_used + self.food_seg.lives_used:
            print("All lives lost.")
            self.f_questions_left = 0
            self.questions_left = 0


def category5(self):
    print('End of game')
    self.questions_left = 0


def quizMain(self):
    print('Instructions:')
    print('Each question carries 1 mark each')
    print('A player has 3 lives. A life is lost when a player answers a question incorrectly.')
    print('When all lives are lost the game is over.')

    while self.questions_left > 0:
        print('\nCategories')
        print('1. Sports')
        print('2. History')
        print('3. Exit game')
        category = int(input("Choose a category (1-3): "))

        if self.choices_chosen[category - 1] == True:
            print("\nCategory was selected previously.")
            print(('Please choose another category.'))
            print('Choices left are:')
            for i in range(self.num_categories):
                if self.choices_chosen[i] == False:
                    print(i + 1)
        elif category == 1:
            self.choices_chosen[category - 1] = True
            self.category1()
        elif category == 2:
            self.choices_chosen[category - 1] = True
            self.category2()
        elif category == 3:
            self.choices_chosen[category - 1] = True
            self.category2()
        elif category == 4:
            self.choices_chosen[category - 1] = True
            self.category2()
        elif category == 5:
            self.category3()
        else:
            print('Invalid entry. Please try again')

    total_points = self.sports_seg.points_tally + self.history_seg.points_tally + self.cultural_seg.points_tally + self.food_seg.points_tally

    print('Total points is ', total_points)
    print("End of game.")


runQuiz = Main()
#runQuiz.quizMain()

