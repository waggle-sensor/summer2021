### Using Anytime Algorithms in Intelligent Systems

Author: Shlomo Zilberstein

 - Anytime algorithms give intelligent systems the capability to trade deliberation time for quality of results. 
 - This capability is essential for successful operation in domains such as signal interpreta- tion, real-time diagnosis and repair, and mobile robot control. 
 - **What characterizes these domains is that it is not feasible (computationally) or desirable (economically) to compute the optimal answer.** 
 - This article surveys the main control problems that arise when a system is composed of several anytime algorithms. These problems relate to optimal management of uncertainty and precision. 
 - After a brief introduction to anytime computation, I outline a wide range of existing solutions to the metalevel control problem and describe current work that is aimed at increasing the applicability of anytime computation.

#### Three metrics useful in anytime algorithm construction
 - **certainty**: a measure of the degree of certainty that the result is correct
 - **accuracy**: a measure of the degree of accuracy, or how close the approximate result is to the exact answer
 - **specificity**: a metric of the level of detail of the result

#### Desired Properties of Anytime Algorithms
 - 1. **measurable quality**: The quality of an approximate result can be determined precisely.
 - 2. **recognizable quality**: The quality of an approximate result can easily be determined at run time (that is, within a constant time).
 - 3. **monotonicity**: The quality of the result is a nondecreasing function of time and input quality.
 - 4. **consistency**: The quality of the result is correlated with computation time and input quality.
 - 5. **diminishing returns**: The improvement in solution quality is larger at the early stages of the computation, and it diminishes over time.
 - 6. **interruptibility**: The algorithm can be stopped at any time and provide some answer.
 - 7. **preemptability**: The algorithm can be suspended and resumed with minimal overhead.