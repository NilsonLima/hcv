from sklearn import decomposition

class PCA:
    @staticmethod
    def transform(X, k):
        return decomposition.PCA(n_components=k).fit_transform(X)