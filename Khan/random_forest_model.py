from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
from detect_features import add_features

np.random.seed(0)



def categorize_ratings(rating):
    '''
        replace ratings into catergories
        [0, 0.5)   --> 0    (most disorderly)
        [0.5, 1.5) --> 1
        [1.5, 2.5) --> 2
        [2.5, 3.5) --> 3
        [3.5, 4.5) --> 4
        [4.5, 5.5) --> 5
        [5.5, 6.5) --> 6
        [6.5, 7.5) --> 7    (most orderly)

        :param rating:
        :return: new rating
    '''

    if (rating >= 0 and rating < 0.5):
        rating = 0
    elif (rating >= 0.5 and rating < 1.5):
        rating = 1
    elif (rating >= 1.5 and rating < 2.5):
        rating = 2
    elif (rating >= 2.5 and rating < 3.5):
        rating = 3
    elif (rating >= 3.5 and rating < 4.5):
        rating = 4
    elif (rating >= 4.5 and rating < 5.5):
        rating = 5
    elif (rating >= 5.5 and rating < 6.5):
        rating = 6
    elif (rating >= 6.5 and rating < 7.5):
        rating = 7

    return rating

def create_random_forest():
    df = add_features()

    # categorize ratings
    df['Order'] = df['Order'].apply(categorize_ratings)

    # check how many samples I have in each class


    # shuffle data set so that the training and test data can have a mix of all labels
    df = shuffle(df)

    # assign 75 percent of the data as training data,
    # assign 25 percent of the data for testing later
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.8

    # creating dataframes with test rows and training rows

    train = df[df['is_train'] == True]
    test = df[df['is_train'] == False]


    # create a list of the feature columns

    # I can delete columns and check how the accuracy compares to see which
    # features matter the most and which matter the least
    # del df['LRSymm']
    # del df['UDSymm']
    # del df['NSED']

    features = df.columns[1:13]

    features_train = train[features]
    labels_train = train['Order']
    features_test = test[features]
    labels_test = test['Order']

    # Creating a random forest classifier
    # look up which parameters would be the best
    model = RandomForestClassifier(n_estimators = 1000, max_features = 10, max_depth = 6, min_samples_leaf = 3)

    # Training the classifier
    model.fit(features_train, labels_train)

    accuracy = model.score(features_test, labels_test)
    print(accuracy) # 51 percent accuracy


def main():
    create_random_forest()

if __name__ == '__main__':
    main()