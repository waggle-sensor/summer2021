import pandas as pd
from plotnine import *
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

def createGaussianMixtureModel():
    '''
    Creates a Gaussian mixture model based on Mean and standard
    deviation of hue, saturation, value, edge density, straight edge
    density, and entropy
    :return: void
    '''
    df = pd.read_excel(r'normalized_data.xlsx')

    features = df.columns[2:11]
    x = df[features]

    EM = GaussianMixture(n_components = 3)
    EM.fit(x)

    cluster = EM.predict(x)

    silhouette_score_model = silhouette_score(x, cluster)  # 0.10 - 0.16 [0.15887342438101767]

    aic_score = EM.aic(x)

    df['cluster'] = cluster

    print(ggplot(x, aes(x = "Order", y = "Mean Hue", color = "cluster")) + geom_point())