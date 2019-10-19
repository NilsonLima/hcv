from sklearn import feature_selection

class SelectKBest:
    @staticmethod
    def transform(X, y, k):
        return feature_selection.SelectKBest(feature_selection.chi2, k=k).fit_transform(X, y)