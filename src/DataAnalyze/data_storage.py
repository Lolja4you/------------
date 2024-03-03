import pandas as pd


class DataAnalyze:
    def __init__(self):
        self.res_name_conf = self.load_res_name_conf()
        self.data = pd.DataFrame({
            'T': [None],
            **{f'R{i+1}({self.res_name_conf[i]})': [None] for i in range(6)}
        })
    
    def load_res_name_conf(self, arg = True):
        if not arg:
            return [None] * 6
        return [i+1 for i in range(6)]

    def add_data(self, *args):
        in_df = pd.DataFrame({
            'T': [args[0]],
            **{f'R{i}({self.res_name_conf[i-1]})': [args[i]] for i in range(1,7)}
        })

        self.data = pd.concat([self.data, in_df], ignore_index=True)

    def get_format(self):
        return self.data
    

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