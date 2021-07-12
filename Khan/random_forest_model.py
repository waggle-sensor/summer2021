from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
import pandas as pd
import numpy as np
from detect_features import add_features
from detect_features import append_df_to_excel

np.random.seed(0)



def categorize_ratings(rating):
    '''
        replace ratings into catergories ( can add more categories once this works)
        [1, 3)   --> 0    (most disorderly)
        [3, 5) --> 1
        [5, 7) --> 2      (most orderly)

        :param rating:
        :return: new rating
    '''

    if (rating >= 1 and rating < 4):
        rating = 0
    elif (rating >= 4 and rating < 6):
        rating = 1
    elif (rating >= 6 and rating < 7):
        rating = 2

    return rating

def check_num_per_classification(df, train, test):

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

    '''
    
        [1, 3) --> 0    (most disorderly)
        [3, 5) --> 1
        [5, 7) --> 2      (most orderly)
        
        total:
        zero count: 159
        one count: 418
        two_count: 528

        train:
        zero count: 150
        one count: 397
        two_count: 499

        test:
        zero count: 9
        one count: 21
        two_count: 29
        
        63 percent accuracy
    '''

    '''
        
        [1, 4)   --> 0    (most disorderly)
        [4, 6) --> 1
        [6, 7) --> 2      (most orderly)
        
        total:
        zero count: 258
        one count: 682
        two_count: 165
        
        train:
        zero count: 248
        one count: 640
        two_count: 158
        
        test:
        zero count: 10
        one count: 42
        two_count: 7
        
        73 percent accuracy  
    '''

    '''
        [1, 4.5)   --> 0    (most disorderly)
        [4.5, 5.5) --> 1
        [5.5, 7) --> 2      (most orderly)
        
        total:
        zero count: 396
        one count: 389
        two_count: 320
        
        train:
        zero count: 378
        one count: 363
        two_count: 305
        
        test:
        zero count: 18
        one count: 26
        two_count: 15    
        
        47 percent accuracy
    '''


def create_random_forest():
    df = pd.read_excel(
        r'C:\Users\SamaahMachine\Documents\Argonne\Images with Ratings\training_data.xlsx')

    # categorize ratings
    df['Order'] = df['Order'].apply(categorize_ratings)

    # normalize all values
    column_names = ['SED', 'Entropy', 'sdValue', 'sdSat', 'sdHue', 'Mean Value', 'Mean Hue', 'Mean Sat', 'ED']

    for i in range(len(column_names)):
        df[column_names[i]] = (df[column_names[i]] - df[column_names[i]].min()) / (df[column_names[i]].max() - df[column_names[i]].min())

    # shuffle data set so that the training and test data can have a mix of all labels
    df = shuffle(df)

    # assign 80 percent of the data as training data,
    # assign 20 percent of the data for testing later
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.80

    # creating dataframes with test rows and training rows
    train = df[df['is_train'] == True]
    test = df[df['is_train'] == False]

    # TODO: check how many samples I have in each class

    # check_num_per_classification(df, train, test)

    # create a list of the feature columns

    # deleting edge density and entropy is making no difference
    # deleting sdValue increases accuracy
    # deleting sdSat increases accuracy even more
    # deleting mean value increases accuracy
    #

    # del df['Mean Value']
    # del df['sdSat']
    # del df['sdValue']
    del df['ED']
    features = df.columns[2:10]
    print(features)

    features_train = train[features]
    labels_train = train['Order']
    features_test = test[features]
    labels_test = test['Order']

    # Creating a random forest classifier
    # look up which parameters would be the best (1000 , 5, 6, 3) max_features = 3
    model = RandomForestClassifier(n_estimators = 1000, max_features = "log2", criterion = "entropy", min_samples_split = 6)
        #n_estimators = 1000, max_features = 5, max_depth = 6, min_samples_leaf = 3, min_samples_split = 8)

    # Training the classifier
    model.fit(features_train, labels_train)

    accuracy = model.score(features_test, labels_test)
    print(accuracy) # 81.46 percent accuracy

def main():
    create_random_forest()

if __name__ == '__main__':
    main()