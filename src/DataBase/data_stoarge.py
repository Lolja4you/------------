import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyze:
    def __init__(self):
        self.res_name_conf = self.load_res_name_conf()
        self.data = pd.DataFrame({
            'T': [None],
            **{f'R{i+1}({self.res_name_conf[i]})': [None] for i in range(6)}
        })
    
    def load_res_name_conf(self, arg=True):
        if not arg:
            return [None] * 6
        return [i+1 for i in range(6)]

    def add_data(self, *args):
        in_df = pd.DataFrame({
            'T': [args[0]],
            **{f'R{i}({self.res_name_conf[i-1]})': [args[i]] for i in range(1, 7)}
        })

        # Exclude empty or all-NA columns before concatenating
        columns_to_include = in_df.columns[~in_df.isnull().all()]
        in_df = in_df[columns_to_include]

        self.data = pd.concat([self.data, in_df], ignore_index=True)

    def get_format(self):
        return self.data
