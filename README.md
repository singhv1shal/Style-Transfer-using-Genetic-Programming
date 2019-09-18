# Style-Transfer-using-Genetic-Programming
This project tests the applicability of Genetic Algorithm in Style Transfer

Genetic algorithm is capable of evolving a solution for optimization problems. Intuitively, if in any way we can define style transfer as an optimization problem, it is possible that image evolves to the target style.

We need to define the problem in terms of Genetic evolution. Every genetic algorithmic problem has the following outline:

Generate the initial population of the random solutions.

Go to each possible solution and objectively say how good is this solution in solving our problem by providing some reward or penalty to rate them among each other.

Check whether we have solved the problem well enough. If not, we will mimic the biological concepts of evolution: Discard the worst half of the solutions, 'breed' the best half together and mutate them by introducing some variance to the solutions.

Iteratively repeat all the process to selectively breed to the solution which solves the problem to an acceptable extent.

## To test the hypothesis
Give command:
python GeneticDriver.py --content_image path-to-content-image --style_image path-to-style-image
