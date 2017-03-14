#   First time using a class in python
#   Relative Python noob
#   Would appreciate feedback on usage, efficiency etc.  
#   Somethings are out of laziness though. 
from string import ascii_lowercase
import sys
import os
from time import sleep 
from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS) -1 #  We start with the base right?
PLACEHOLDER = '_'


class Hangman():
    ''' 
    Self contained Hangman Game 
    Start game by providing a word. 
    Should probably return game result for higher up score keeping
     '''
    def __init__(self, solution):
        ''' Start initial conditions and trigger main loop'''
        self.guess_no = 0
        self.guesses = []
        self.solution = solution
        while self.loop() :
            self.get_input_guess()    

    def word(self):
        ''' Build world from guesses'''
        word_array = []
        for i in self.solution.lower():
          if( i in self.guesses or i not in ASCII ):
            word_array.append( i)
          else:
            word_array.append(PLACEHOLDER)
        return "".join(word_array)
    
    def get_input_guess(self):
        ''' get input and keep it if it's new, if it's wrong increment guess count'''
        print("\t*  ",self.word() )
        print("\t*   Enter a letter:\n" )
        new_guess = str(input("\t*   ")).lower()
        if(new_guess not in self.guesses and new_guess in ASCII):
            self.guesses.append(new_guess)
            if( new_guess not in self.solution.lower()):
                self.guess_no += 1
        else:
            print("\t*  You've already guessed that one silly")
            sleep(1)  

    def check_win(self):
        ''' does guess word equal solution, print output if so'''
        if( self.word() == self.solution.lower() ):
            print("\t*  ",self.solution)
            print("\t*  Congrats! You Win!")
            self.result = True
            return True
        else:
            return False

    def check_loss(self):
        ''' did we run out of guesses, print loser output'''
        if( self.guess_no == ALLOWED_GUESSES ):
            print("\t*  Sorry! You Lose")
            print("\t*  The correct word was:")
            print("\t*  ",self.solution )
            self.result = False
            return True
        else:
            return False
    
    def loop( self ):
        ''' Main output loop return True while game continues'''
        os.system("clear")
        print("\t**********************************************")
        print("\t***         Terminal Movie Hangman         ***")
        print("\t**********************************************")
        print("\t*                                            *")
        print("\t*  Incorrect Guesses: ",str(self.guess_no),"/",str(ALLOWED_GUESSES),"                *")
        print("\t*  ",HANG_GRAPHICS[self.guess_no]  )
        print("\n")
        if( self.check_win() ):
            return False
        elif( self.check_loss() ):
            return False
        else:
            return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        solution = sys.argv[1]
    else:
        solution = get_word()
    
    while True:
        game = Hangman(solution)
        play_again = input("\t*  Would You Like to Play again [yY/nN] ? ")
        if play_again not in ["Y","y"]:
            if play_again not in ["N","n"]:
                print("\t*   You failed a simple question, no games for you!")
                exit()
            else:
                print("\t*   Thanks For Playing.")
                exit()
        else:
            solution = get_word()
                    
    

