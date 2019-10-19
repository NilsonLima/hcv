from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

class Classifier:
    def __init__(self, classifier_name, X, y, param_grid, cv):
        self.X = X
        self.y = y
        self.param_grid = param_grid
        self.cv = cv
        self.clf_class = None

        if (classifier_name == 'rfc'):
            self.clf_class = RandomForestClassifier
        elif (classifier_name == 'svc'):
            self.clf_class = SVC
        else:
            raise Exception('Invalid classifier name')

    def grid_search(self):
        clf = self.clf_class(random_state=42, class_weight='balanced')
        cv_clf = GridSearchCV(cv=self.cv, param_grid=self.param_grid, estimator=clf, n_jobs=-1)
        cv_clf = cv_clf.fit(self.X, self.y)
        return cv_clf.best_params_

    def perform(self):
        params = self.grid_search()
        clf = self.clf_class(class_weight='balanced', **params)
        clf = clf.fit(self.X, self.y)
        return clf
