from pprint import pprint
from dataset import Dataset
from config import Config
from encoder import get_encoder
from feature_reducer import get_feature_reducer_and_transform
from model import Select, Classifier, Scoring
from writer import write_data_into_xlsx_file

def main():
    dataset = Dataset()
    config = Config()

    total_scores = []
    row_names = []
    
    for index, prod in enumerate(config.get_product()):
        (
            classes,
            encoding_method,
            feature_reducer,
            test_size,
            clf_info
        ) = prod

        df = dataset.filter_df_by_targets(classes['negative'] + classes['positive'])
        X = dataset.extract_X(df)
        y = dataset.extract_y(df)

        X = get_encoder(encoding_method).encode(X)
        X = get_feature_reducer_and_transform(feature_reducer)(X, y)
        y = y.map(lambda x: 1 if x in classes['positive'] else 0)

        data_split = Select(X, y, test_size)
        classifier = Classifier(
            clf_info['clf'],
            data_split.X_train,
            data_split.y_train,
            clf_info['param_grid'],
            clf_info['cv']
        ).perform()
        
        scores = Scoring(classifier).get_scores(data_split.X_test, data_split.y_test)
        total_scores.append(scores)

    
    pprint(total_scores)

    return

if __name__ == '__main__':
    main()