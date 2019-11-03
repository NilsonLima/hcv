from pprint import pprint
from dataset import Dataset
from config import Config
from encoder import get_encoder
from feature_reducer import get_feature_reducer_and_transform
from model import Select, Classifier, Scoring
from writer import *

def main():
    dataset = Dataset()
    config = Config()

    experiments = {}
    total_scores = []
    row_names = []
    col_names = Scoring.get_score_names()
    config_keys = config.get_keys()
    
    for index, prod in enumerate(config.get_product(), start=1):
        (
            target,
            encoding,
            feature_reducer,
            test_size,
            clf_info
        ) = prod

        df = dataset.filter_df_by_targets(target['negative'] + target['positive'])
        X = dataset.extract_X(df)
        y = dataset.extract_y(df)

        X = get_encoder(encoding).encode(X)
        y = y.map(lambda x: 1 if x in target['positive'] else 0)

        X = get_feature_reducer_and_transform(feature_reducer, X, y)

        data_split = Select(X, y, test_size)
        classifier = Classifier(
            clf_info['clf'],
            data_split.X_train,
            data_split.y_train,
            clf_info['param_grid'],
            clf_info['cv']
        )
        clf = classifier.perform()
        
        scores = Scoring(clf).get_scores(data_split.X_test, data_split.y_test)

        total_scores.append(scores)
        row_names.append(f'experiment_{index}')
        experiments[f'experiment_{index}'] = dict(zip(config_keys, (
            target,
            encoding,
            feature_reducer,
            test_size,
            { 'clf': clf_info['clf'], 'best_params': classifier.best_params }
        )))

    write_data_into_xlsx_file(total_scores, col_names, row_names)
    write_data_into_json_file(experiments)

    return

if __name__ == '__main__':
    main()