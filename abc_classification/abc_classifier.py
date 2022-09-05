"""Module for ABC classification in business analysis."""
import pandas as pd
import numpy as np


class ABCClassifier:
    """ABC classification class"""

    def __init__(self, data: pd.DataFrame):
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Provided object is not pd.DataFrame')

        self.data = data
        self.abc_df = None

    def classify(self, abc_column: str, criterion: str) -> pd.DataFrame:
        """Make ABC classification for values from abc_column.
        Dataframe must be grouped by abc_column.
        Args:
            abc_column - column with values to classify.
            criterion - column with criterion for classification.
        Return:
            abc_df - classified dataframe."""
        if not isinstance(abc_column, str):
            raise ValueError(f'Column name must be string not {type(abc_column)}')
        if not isinstance(criterion, str):
            raise ValueError(f'Column name must be string not {type(criterion)}')

        self.abc_df = self.data[[abc_column, criterion]].copy()
        self.abc_df.sort_values(by=criterion, inplace=True, ascending=False)
        total = self.data[criterion].sum()
        self.abc_df['percentage'] = self.abc_df[criterion] / total
        self.abc_df[f'cumulative_{criterion}'] = self.abc_df['percentage'].cumsum()
        conditions = [(self.abc_df[f'cumulative_{criterion}'] <= 0.8),
                      (self.abc_df[f'cumulative_{criterion}'] <= 0.95),
                      (self.abc_df[f'cumulative_{criterion}'] > 0.95)]
        values = ['A', 'B', 'C']
        self.abc_df['class'] = np.select(conditions, values)

        return self.abc_df

    def brief_abc(self) -> pd.DataFrame:
        """Return aggregated by class dataframe with brief information about class."""
        return self.abc_df.groupby('class').sum()

    def to_csv(self, filename='abc_dataframe.csv', sep=',') -> None:
        """Save classified dataframe to csv.
        Args:
            filename - name of file for saving.
            sep - separator to use."""
        self.abc_df.to_csv(filename=filename, sep=sep)
