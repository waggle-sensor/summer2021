import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from plotnine import *

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

from sklearn.metrics import silhouette_score
from sklearn.utils import shuffle




def createGuassianMixtureModel():
    df = pd.read_excel(
        r'C:\Users\SamaahMachine\Documents\Argonne\Images with Ratings\training_data.xlsx')

    # normalize all values
    column_names = ['SED', 'Entropy', 'sdValue', 'sdSat', 'sdHue', 'Mean Value', 'Mean Hue', 'Mean Sat', 'ED']

    for i in range(len(column_names)):
        df[column_names[i]] = (df[column_names[i]] - df[column_names[i]].min()) / (df[column_names[i]].max() - df[column_names[i]].min())

    features = df.columns[2:11]
    print(features)
    x = df[features]

    # n_componenets -> number of clusters
    EM = GaussianMixture(n_components = 3)

    EM.fit(x)

    cluster = EM.predict(x)
    print(cluster)

    # cluster_p = EM.predict_proba(x)

    print("Silhouette:", silhouette_score(x, cluster))  # 0.10 - 0.16 [0.15887342438101767]
    #
    aic_score = EM.aic(x)
    print(aic_score)

    # df['cluster'] = cluster
    # print(ggplot(x, aes(x = "Order", y = "Mean Hue", color = "cluster")) + geom_point())

    # 0.15887342438101767


def main():
    createGuassianMixtureModel()

if __name__ == '__main__':
    main()