## Notes from Nicola:

1. Can improve inference time by statically reducing neural network model size (network compression) or using smaller capsule networks.  But this is a static solution. (have papers but didn’t include b/c not relevant)
 
2. There are adaptive inference methods that skip execution of parts of a network, based on an estimate of relevance computed for each input (e.g. McGill & Perona 2017) – these seem to be very specific to the application.
 
3. Anytime predictors is an idea from 1990s (Zilberstein, 1996). Prediction available at “any” compute time but with variable accuracy/confidence for the resulting prediction. 
    - Can use ensemble methods (Dietterich 2000) or cascade (as in Zilberstein).
    - NN using anytime predictors:
      - FractalNet, BranchyNet, …
      - Hu et al 2019, Huang et al 2017, Teerapittayanon et al 2016, McGill 2017, Wan et al

## Updates from 05/11/21 to 05/21/21
 - Read papers on anytime DNN ([Zilberstein-AAAI-1996](../Liu/paper-notes/Zilberstein-AAAI-1996.md), [Dietterich-MCS-2000](paper-notes/Dietterich-MCS-2000.md), [BranchNet-ICPP-2016](paper-notes/BranchNet-ICPP-2016.md), [DistributedDNN-ICDCS-2017](paper-notes/DistributedDNN-ICDCS-2017.md), and [Lee-Arxiv-2018](paper-notes/Lee-Arxiv-2018.md))
 - Train the Anytime DNN model for IResNext and BranchNet based on their codes
 - Pick up neural network and deep learning knowledges by reviewing the [book](http://neuralnetworksanddeeplearning.com/) chapter1 to chapter3
   - stochastic gredient decent, backpropogation's prove
   - slow learning issue for quadratic loss function: cross-entropy, softmax with log-likelihood's prove
   - regularization to reduce overfitting: L1, L2 regularizations
   - dropout
   - weights and bias initilization
   - Hessian technique, Momentum-based gredient decent
   - other neurons: sigmoid, tanh, ReLU

## Questions to discuss (05/21/21)
 - Motivation of Anytime DNN: Compared with research activities in building more powerful hardware/accelerators and architectures to speed up the DNN’s inference time, anytime DNN seems to be less competitive. The usage of it seems to be limited to **resource-constraint scenarios** and there is **no penalty for performance degradation**.
   - Any specific application requirements from SAGE
 - Contradictions in building anytime DNN: According to Zilberstein’s paper (AAAI-1996), I think one of the core part of anytime algorithm is to set up the relationship between time/resources and results qualities, statistically or theoretically. On the other hand, as a black-box based approach, it is hard to explain how DNN learns, especially **the impact of intermediate results from sub layers**, which makes it hard to set up this kind of relationship between time/resources and results qualities for DNN.
   - How can we explain the DNN's learning?
   - Can we set up this relationship based on **explainable machine learning algorithms** (or ensembling explanable algorithms)
 - Decompose with applications and dataset: Customized designs for specific application and dataset to make it possible to be anytime is feasible. **The real challenge is to propose a general approach which decomposes with applications and datasets**.
