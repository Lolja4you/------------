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
    
#     def plot_data(self):
#         fig, axs = plt.subplots(2, 3, figsize=(15, 10))
#         print('----\n', self.data)
#         for i, ax in enumerate(axs.flat):
#             col = f'R{i+1}({self.res_name_conf[i]})'
#             ax.plot(self.data['T'], self.data[col], marker='o')
#             ax.set_title(col)
#             ax.set_xlabel('T')
#             ax.set_ylabel('Values')
#         plt.tight_layout()
#         plt.show()


# # Использование:
# data_analyze = DataAnalyze()
# data_analyze.add_data(322.372, 297.925, 295.925, 311.925, 297.925, 294.925, 345.925)
# data_analyze.plot_data()
    

'''data = DataAnalyze()
data.add_data(100, 10, 20, 30, 40, 50, 60)
data.add_data(110, 11, 21, 31, 41, 51, 61)
data.add_data(120, 12, 22, 32, 42, 52, 62)
data.add_data(130, 13, 23, 33, 43, 53, 63)
data.add_data(140, 14, 24, 34, 44, 54, 64)
data.add_data(150, 15, 25, 35, 45, 55, 65)
print(data.get_format())

plt.figure(figsize=(15, 10))
for i, column in enumerate(data.data.columns[1:]):
    plt.plot(data.data['T'], data.data[column], label=column)

plt.xlabel('T')
plt.ylabel('Value')
plt.legend()
plt.title('Data Analysis')
plt.show()'''