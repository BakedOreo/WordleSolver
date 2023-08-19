# WordleSolver
## Overview

This was a project that I made in conjunction with Jane Street's Academy Of Math and Programming in the Summer of 2023. The project with the purpose of creating an efficient solver for the popular game [Wordle](https://www.nytimes.com/games/wordle/index.html).

In this project I implemented three different solvers:
  - A random solver, which chooses possible words randomly for each guess
  - A "brute force" solver, which inputs five preset guesses that cover 25 letters, with the last guess being chosen randomly
  - An entropy solver, which uses the [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html) library to generate the best possible guess


## Takeaways
From this project I learned about shannon entropy, a tool used to determine how much information you can gain from a given distribution. I also learned how to write experiments in code, as I was able to compare all three of my solvers against each other. This project also improved on my ability to write robust test-cases that are relevant to the project.

## Credits
Thanks you so much to Eric Campbell and Justin Wu for giving me feedback throughout this project.
