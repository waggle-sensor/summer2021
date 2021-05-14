### Ensemble Methods in Machine Learning

Author: Thomas G. Dietterich

 - Ensemble methods are learning algorithms that construct a set of classifiers and then classify new data points by taking a (weigh- ted) vote of their predictions. 
 - The original ensemble method is Bayesian averaging, but more recent algorithms include error-correcting output coding, Bagging, and boosting. 
 - This paper reviews these methods and explains why ensembles can often perform better than any single classi- fier. Some previous studies comparing ensemble methods are reviewed, and some new experiments are presented to uncover the reasons that Adaboost does not overfit rapidly.

#### Three reasons to construct very good ensembles:
 - statistical
 - computational
 - representational

#### Methods for constructing ensembles:
 - Bayesian Voting: Enumerating the Hypotheses
 - Manipulating the Training Examples
   - manipulates the training examples to generate multiple hypotheses
   - The learning algorithm is run several times, each time with a different subset of the training examples
   - works especially well for unstable learning algorithms—algorithms whose output classifier undergoes major changes in response to small changes in the training data
     - unstable algorithms: decision-tree, neural network, and rule learning algorithms
     - stable algorithms: linear regression, nearest neighbor, and linear threshold algorithms
   - Three ways:
     - Bagging (bootstrap aggregation): the learning algorithm with a training set that consists of a sample of m training examples drawn randomly with replacement from the original training set of m items.
     - Cross-validated committee: construct the training sets by leaving out disjoint subsets of the training data
     - AdaBoost: maintains a set of weights over the training examples; place more weight on training examples that were misclassified and less weight on examples that were correctly classified.
 - Manipulating the Input Features
   - manipulate the set of input features available to the learning algorithm
   - only works well when the input features are highly redundent
 - Manipulating the Output Targets: error-correcting output coding
 - Injecting Randomness

#### Comparisions of different ensemble methods
 - Data sets have little or no noise: AdaBoost often gives the best results. Bagging and randomized trees give similar performance, although randomization is able to do better in some cases than Bagging on very large data sets.
 - Data sets with 20% synthetic class label noise: AdaBoost overfits the data badly while Bagging is shown to work very well in the presence of noise. Randomized trees did not do very well.