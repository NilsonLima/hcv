from sklearn.model_selection import train_test_split

class Select:
    def __init__(self, X, y, test_size):
        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test
        ) = train_test_split(X, y, stratify=y, test_size=test_size, random_state=42)