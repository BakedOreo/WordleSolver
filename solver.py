#!/usr/bin/env python3

from wordle import Player, GameManager
from scipy.stats import entropy
from wordlist import WordList
from information import patterns
from time import time

class Solver(Player):
    """
    "Solving" Wordle

    Your task is to fill in this class to automatically play the game.
    Feel free to modify any of the starter code.

    You Should write at least three subclasses of Player.
    1. A Random Player -- guess a random word each time!
    2. A Player that uses Matt Parker's 5 Words. 
       2a. How do you leveage the info gained from these 5 words?
       2b. Do always you have to guess all of these words?
       3b. What order should you guess these words in?
    3. Entropy Player (You are welcome to use the scipy above)
    4. Better and Better Players!

    Your goal is not just to Write the BEST SOLVER YOU CAN, but scientifically
    show that your solver is better than the others. 

    Note that the GameManager class returns the number of guesses a player makes.
    Compute 3 statistics:
    (1) the average number of guesses
    (2) the max number of guesses
    (3) the minimum number of guesses

    Think deeply about how you should design this experiments. How should you select the
    experimental inputs? Is it better for the two algorithms youre comparing to have the
    same or different test sets between experiments?
    
    Please use objects and inheritance to structure your experiments.

    Here's an outline of the rest of the code in this project.
    - wordle.py.
      Hit play when VSCode is focused on this file to play
      a game of wordle against the computer! There are 3 classes
      of interest to the Solver:
      +  `Wordle` manages the world game state itself
      +  `Player` Provides a Human interface at the CLI to play the game
          Your Solver exposes the same interface as this class       
      +  `Game Manager` runs the main control loop for Wordle

    - information.py
      This file defines how information is propagated to the player. The relevant
      classes are `Information` and `Pattern`.
      + Pattern records a list `pattern` that represents the outcomes. 
        For instance
            [hit, miss, miss, mem, hit]
        Means the first and last letters of a guess are correct, the second two
        are not in the word, and the penultimate is in the word but not
        in the right spot. These codes are defined in `Code`.

      + Pattern provides a useful method `pattern.matches(guess, word)` which
        checks that the current pattern is consistent with guessing `guess` when
        `word` is the goal word

      + Information is constructed by passing it a player-provided `guess` and
        the `goal` word. 
        
      + Information provides an important method `info.matches(word)` which 
        returns true if `info.pattern == Information(info.guess, word)`

      + IMPORTANT. The `patterns()` function returns a list of all 3^5 patterns.

    - `wordlist.py`
       This file defines the `WordList` class, which is not actually a `list`,
       but wraps a list, defining some helpful wordle-specific features.
       + wordlist.get_random_word() gets a random word from the wordlist
       + wordlist.refine(info) keeps only those words consistent with `info`
       + wordlist.matching(pattern, guess) produces a literal `list`
         of words that such that if they had been the goal word, would have 
         produced pattern in responds to a player guessing `guess.

    
    IN GENERAL. FEEL FREE TO MAKE ANY MODIFICATIONS/ADDITIONS TO THIS CODE.
    You shouldn't neeeed to but of course please do if it makes your solution
    more elegant
    """

    def __init__(self):
        """
        Initialize the solver.
        """
        self.num_guesses = 0
        self.wordlist = WordList()

    def make_guess(self):
        """
        the make_guess function makes a guess.

        Currently, it always guesses "salty". Write code here to improve your solver.
        """
        return "salty"

    def update_knowledge(self, info):
        self.wordlist.refine(info)
        print(info)

class Random(Solver):
    def __init__(self):
        super().__init__()
    
    def make_guess(self):
        return self.wordlist.get_random_word()

class Five(Solver):
    def __init__(self):
        super().__init__()
    
    def make_guess(self):
        words = ["fjord", "gucks", "nymph", "vibex", "waltz"]
        self.num_guesses += 1
        if self.num_guesses < 6:
          return words[self.num_guesses - 1]
        else:
          return self.wordlist.get_random_word()
          

class Entropy(Solver):
    def __init__(self):
        super().__init__()
    
    def find_probs(self, word):
        probs = [0] * 3**5
        combos = patterns()
        # for word in self.wordlist:
        for j in range(len(combos)):
            valids = self.wordlist.matching(combos[j], word)
            probs[j] += (float(len(valids)))/len(self.wordlist)

        return entropy(probs,base=2)


    def make_guess(self):
      if self.num_guesses == 0:
        self.num_guesses += 1
        return "raise"
      high = 0
      guess = ""
      for word in self.wordlist:
          entropy = self.find_probs(word)
          if entropy >= high:
              high = entropy
              guess = word
      return guess

class Benchmark():
    def __init__(self, *solver):
        self.tests = [method for method in solver]
        self.wordlist = WordList()
        self.words = [self.wordlist.get_random_word() for _ in range(50)]
    
    def test(self, words, method):
        total = 0
        start = time()
        for word in words:
          manager = GameManager(method(), word)
          n_guess = manager.play_game()
          total += n_guess
        end = time()
        return (f"Average guesses: {total/len(words)}" + 
                f"\nAverage time: {(end - start)/len(words)}\n")

    def test_edge_cases(self, method):
        cases = ["boxer", "slyly", "glean", "angle", "angel", "proxy", "jazzy"]
        return self.test(cases, method)

    def run_sim(self):
        # normal_data = self.test(self.wordlist)
        # edge_data = self.test_edge_cases()

        res = ""
        for idx, method in enumerate(self.tests):
            res += (f"\nMETHOD {idx + 1} \n")
            res += "\nNormal Cases:\n"
            res += self.test(self.words, method)
            res += "\nEdge Cases:\n"
            res += self.test_edge_cases(method)
        print(res)

def main():
    solver1 = Random
    solver2 = Five
    solver3 = Entropy

    game = Benchmark(solver1, solver2, solver3)
    game.run_sim()

if __name__ == "__main__": main()
