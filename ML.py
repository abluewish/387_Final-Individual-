import pandas as pd
import numpy as np



# Your code here
def blight_model():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score
    
    train_data=pd.read_csv('./train.csv',encoding = 'ISO-8859-1' )
    train_data=train_data[pd.notnull(train_data.compliance)]
    test_data=pd.read_csv('./test.csv',encoding='ISO-8859-1')
    test_data=test_data.set_index('id')
    
    target=['pattern']
    
    features=['gender',
     'weight',
     'height',
     'exercise_amount']
    clf =RandomForestClassifier(n_estimators=100,max_depth=8,random_state=0)
    X_train,X_valid,y_train,y_valid = train_test_split(train_data[features],train_data[target],test_size= 0.2,)
    clf.fit(train_data[features],train_data[target])
    test_data['pattern'] = clf.predict_proba(test_data[features])[:,1]
    return test_data['pattern']
