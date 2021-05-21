### Using Anytime Algorithms in Intelligent Systems

Author: Shlomo Zilberstein

 - Anytime algorithms give intelligent systems the capability to trade deliberation time for quality of results. 
 - This capability is essential for successful operation in domains such as signal interpretation, real-time diagnosis and repair, and mobile robot control. 
 - **What characterizes these domains is that it is not feasible (computationally) or desirable (economically) to compute the optimal answer.** 
 - This article surveys the main control problems that arise when a system is composed of several anytime algorithms. These problems relate to optimal management of uncertainty and precision. 
 - After a brief introduction to anytime computation, I outline a wide range of existing solutions to the metalevel control problem and describe current work that is aimed at increasing the applicability of anytime computation.

#### **Three metrics** useful in anytime algorithm construction
 - **certainty**: a measure of the degree of certainty that the result is correct
 - **accuracy**: a measure of the degree of accuracy, or how close the approximate result is to the exact answer
 - **specificity**: a metric of the level of detail of the result

#### **Desired Properties** of Anytime Algorithms
 - **measurable quality**: The quality of an approximate result can be determined precisely.
 - **recognizable quality**: The quality of an approximate result can easily be determined at run time (that is, within a constant time).
 - **monotonicity**: The quality of the result is a nondecreasing function of time and input quality.
 - **consistency**: The quality of the result is correlated with computation time and input quality.
 - **diminishing returns**: The improvement in solution quality is larger at the early stages of the computation, and it diminishes over time.
 - **interruptibility**: The algorithm can be stopped at any time and provide some answer.
 - **preemptability**: The algorithm can be suspended and resumed with minimal overhead.
#### **Performance Profilers**
 - Definition 1 : A PP (Performance Profiles) of an anytime algorithm, Q(t), denotes the expected output quality with execution time t.
 - Definition 2 : A CPP (Conditional Performance Profiles) of an anytime algorithm, Pr(q<sub>out</sub> | q<sub>in</sub>, t), denotes the probability of getting a solution of quality when the algorithm is activated with input of quality q<sub>in</sub> and execution time t.
 - Definition 3 : A dynamic performance profile (DPP) of an anytime algorithm, Pr(q<sub>j</sub>|q<sub>i</sub>, ∆t), denotes the probability of getting a solution of quality q<sub>j</sub> by resuming the algorithm for time interval ∆t when the currently available solution has quality q<sub>i</sub>.

**Anytime algorithm composition problem**: how much time to allocate to each component to maximize the output quality of the complete system.

#### Compilation
Given a system composed of anytime algorithms, the compilation process is designed to (1) determine the optimal PP of the complete system and (2) prepare any additional control information that would simplify the run-time monitoring task.