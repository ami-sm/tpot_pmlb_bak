import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:1.0
exported_pipeline = RandomForestClassifier(bootstrap=True, criterion="entropy", max_depth=40, max_features="auto", min_samples_leaf=3, min_samples_split=14, n_estimators=600)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
