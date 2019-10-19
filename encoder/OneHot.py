import category_encoders as ce

class OneHotEncoder:
    @staticmethod
    def encode(X):
        return ce.OneHotEncoder(handle_unknown='ignore', use_cat_names=True).fit_transform(X)