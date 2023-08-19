# WordleSolver
## Overview

This was a project that I made in conjunction with Jane Street's Academy Of Math and Programming in the Summer of 2023. The project with the purpose of creating an efficient solver for the popular game [Wordle](https://www.nytimes.com/games/wordle/index.html).

In this project I implemented three different solvers:
  - A random solver, which chooses possible words randomly for each guess
  - A "brute force" solver, which inputs five preset guesses that cover 25 letters, with the last guess being chosen randomly
  - An entropy solver, which uses the [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html) library to generate the best possible guess

After running some tests, I found that my entropy solver was the most efficient, with an average of 3.51 guesses per game. My random solver had an average of 4.3 guesses per game, and my "brute force" solver had an average of 6.0.

## Takeaways
From this project I learned how to:
  - Use Shannon Entropy, a tool used to quantify the amount of information that can be gained from a given distribution
  - Run experiments in code; I learned how to test my solvers against each other and gather relevant data in doing so
  - Write more robust test cases

I also learned that one of the best starting words in Wordle is "raise" 🤔.

One challenge I faced making this project was in connecting all of my functions together. This has been one of my largest projects thus far, so organization was more difficult than usual. In the future I want to try to implement a solver that uses decision trees, as I think it may be possible to reach an average guess count of less than 3.5 using one.

## Credits
Thanks you so much to Eric Campbell and Justin Wu for giving me feedback throughout this project.
