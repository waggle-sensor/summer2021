import itertools
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def categorize_ratings(rating):
    '''
        replace ratings into catergories ( can add more categories once this works)

        :param rating:
        :return: new rating
    '''

    if (rating < 3.29):
        rating = 0
    elif (rating >= 3.29 and rating < 5.02):
        rating = 1
    elif (rating >= 5.02):
        rating = 2

    return rating

def check_num_per_classification(df, train, test):
    '''
    Helper method to check number of samples in each classification

    :param df:  dataframe with all data
    :param train:  dataframe with training data
    :param test:   datafame with test data
    :return: void
    '''

    zero_count = 0
    one_count = 0
    two_count = 0
    for val in test['Order']:
        if (val == 0):
            zero_count += 1
        elif (val == 1):
            one_count += 1
        elif (val == 2):
            two_count += 1

    print("zero count:", zero_count)
    print("one count:", one_count)
    print("two_count:", two_count)

def find_correlation_between_features(feature1, feature2):
    '''
    Finds correlation between 2 given features
    :param feature1: First feature to find correlation between
    :param feature2: Second feature to find correlation between
    :return: Correlation value between -1 and 1
    '''

    plt.scatter(feature1, feature2)
    plt.show()
    correlation = feature1.corr(feature2)

    return correlation

def print_all_correlations(df):
    '''
    Finds every combination in groups of 2 of features and finds correlation between them.
    :param df: dataframe
    :return: void
    '''

    column_names = ['SED', 'Entropy', 'sdValue', 'sdSat', 'sdHue', 'Mean Value', 'Mean Hue', 'Mean Sat', 'ED']

    correlations = []
    for comb in itertools.combinations(column_names, 2):
        correlation = find_correlation_between_features(df[comb[0]], df[comb[1]])

        correlations.append(correlation)

    correlations.sort()

def display_histogram(df, num_bars):
    '''
    displays histogram of data
    :param df: dataframe
    :param num_bars: number of bars that are shown in histogram
    :return: void
    '''

    plt.hist(df['Order'], num_bars)
    plt.show()

def normalize_values(df):
    '''
    normalize all values in dataframe from 0 - 1
    :param df: dataframe
    :return: void
    '''

    column_names = ['SED', 'Entropy', 'sdValue', 'sdSat', 'sdHue', 'Mean Value', 'Mean Hue', 'Mean Sat', 'ED']

    for i in range(len(column_names)):
        df[column_names[i]] = (df[column_names[i]] - df[column_names[i]].min()) / (df[column_names[i]].max() - df[column_names[i]].min())

    df.to_excel(r'normalized_data.xlsx', index=False)

def create_random_forest():
    '''
    Using data of ~3000 images, their features, and their order rating,
    created a random forest model. Assigned 20 percent of data for testing
    and 30 percent of data for training.
    :return: void
    '''

    df = pd.read_excel(r'normalized_data.xlsx')

    df['Order'] = df['Order'].apply(categorize_ratings)

    df = shuffle(df)

    df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.80

    train = df[df['is_train'] == True]
    test = df[df['is_train'] == False]

    features = df.columns[2:11]

    features_train = train[features]
    labels_train = train['Order']
    features_test = test[features]
    labels_test = test['Order']

    model = RandomForestClassifier(n_estimators = 2000, max_features = "log2", criterion = "entropy",
                                   min_samples_split = 8)

    model.fit(features_train, labels_train)

    # 71 percent accuracy when split into 3 categories
    accuracy = model.score(features_test, labels_test)

def main():
    create_random_forest()

if __name__ == '__main__':
    main()