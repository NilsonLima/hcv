from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, roc_auc_score, recall_score, f1_score

class Scoring:
    def __init__(self, clf):
        self.clf = clf

    def get_scores(self, X_test, y_test):
        y_pred = self.clf.predict(X_test)
        return [
            accuracy_score(y_test, y_pred),
            precision_score(y_test, y_pred),
            roc_auc_score(y_test, y_pred),
            recall_score(y_test, y_pred),
            f1_score(y_test, y_pred),
            confusion_matrix(y_test, y_pred)
        ]