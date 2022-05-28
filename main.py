import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

names1882 = pd.read_csv('C:\\Users\\lenov\\Desktop\\Names\\yob1882.txt', names=['name', 'sex', 'births'])
print(names1882)
years = range(1880, 2021)
pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'C:\\Users\\lenov\\Desktop\\Names\\yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)
names

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_births

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year', 'sex']).apply(add_prop)

np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.reset_index(inplace=True, drop=True)
total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
subset = total_births[['Anna', 'Mary']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Кол-во Anna и Mary по годам")
all_names = top1000.name.unique()
mask = np.array(['anna' in x.lower() for x in all_names])
anna_like = all_names[mask]
anna_like
all_names = top1000.name.unique()
mask = np.array(['mary' in x.lower() for x in all_names])
mary_like = all_names[mask]
mary_like
filtered = top1000[top1000.name.isin(anna_like)]
filtered.groupby('name').births.sum()
anna = filtered.groupby('name').births.sum()
anna.plot(subplots=True, figsize=(12, 10), grid=False, title="Производные от имени anna")
filtered = top1000[top1000.name.isin(mary_like)]
filtered.groupby('name').births.sum()
mary = filtered.groupby('name').births.sum()
mary.plot(subplots=True, figsize=(12, 10), grid=False, title="Производные от имени Mary")
text_file = open('C:\\Users\\lenov\\Desktop\\Names\\yob1882.txt')
text = text_file.read()
unique = []

for word in names1882.name:
    unique.append(word)

unique.sort()
print(unique)
plt.show()
