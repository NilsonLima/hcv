# from .SelectKBest import SelectKBest
# from .PCA import PCA

from sklearn.feature_selection import SelectKBest, chi2, RFE
from sklearn.svm import SVR

def get_feature_reducer_and_transform(feature_reducer, X, y):
    if (feature_reducer['method'] == 'chi2'):
        return SelectKBest(chi2, k=feature_reducer['k']).fit_transform(X, y)

    if (feature_reducer['method'] == 'rfe'):
        return RFE(SVR(kernel='linear'), feature_reducer['k'], step=1).fit_transform(X, y)

    raise Exception('Invalid feature reducer method')