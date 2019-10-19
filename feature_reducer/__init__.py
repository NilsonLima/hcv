from .SelectKBest import SelectKBest
from .PCA import PCA

def get_feature_reducer_and_transform(feature_reducer):
    if (feature_reducer['method'] == 'pca'):
        return lambda X, _: PCA.transform(X, feature_reducer['k'])

    if (feature_reducer['method'] == 'k-best'):
        return lambda X, y: SelectKBest.transform(X, y, feature_reducer['k'])

    raise Exception('Invalid feature reducer method')