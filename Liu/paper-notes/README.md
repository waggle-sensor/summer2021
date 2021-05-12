## Notes from Nicola:

1. Can improve inference time by statically reducing neural network model size (network compression) or using smaller capsule networks.  But this is a static solution. (have papers but didn’t include b/c not relevant)
 
2. There are adaptive inference methods that skip execution of parts of a network, based on an estimate of relevance computed for each input (e.g. McGill & Perona 2017) – these seem to be very specific to the application.
 
3. Anytime predictors is an idea from 1990s (Zilberstein, 1996).  Prediction available at “any” compute time but with variable accuracy/confidence for the resulting prediction. 
    -Can use ensemble methods (Dietterich 2000) or cascade (as in Zilberstein).
    -NN using anytime predictors:
        1. FractalNet, BranchyNet, …
        2. Hu et al 2019, Huang et al 2017, Teerapittayanon et al 2016, McGill 2017, Wan et al