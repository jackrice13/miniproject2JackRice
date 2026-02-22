### INF601 - Advanced Programming in Python
### Jack Rice
### Mini Project 2

# This project will be using Pandas dataframes. This isn't intended to be full blown data science project. The goal here is to come up with some question and then see what API or datasets you can use to get the information needed to answer that question. This will get you familar with working with datasets and asking questions, researching APIs and gathering datasets. If you get stuck here, please email me!
#
#     x(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#     x(5/5 points) Proper import of packages used.
#     (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#     Think of some question you would like to solve such as:
#     "How many homes in the US have access to 100Mbps Internet or more?"
#     "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#     Here are some other great datasets: https://www.kaggle.com/datasets
#     x(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
#     x(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
#     x(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#     x(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#     x(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#     (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#Creates /charts/ if it does not exsist
chart = Path('charts')
if not chart.exists():
    Path('charts').mkdir()

df = pd.read_csv('data/tech_employment_2000_2025.csv', index_col=0, low_memory=False)
df = df.reset_index()
#print(df.head())

company = df[['company','year','layoffs','new_hires']]
#print(company.value_counts())

#AMD Data
amd_data = df[df['company'] == 'AMD'].groupby('year').sum()
# amd_layoffs = df.loc[df['company'] == 'AMD', 'layoffs']
# print(amd_layoffs.head())
# amd_hires = df.loc[df['company'] == 'AMD', 'new_hires']
# print(amd_hires.head())

#Adobe Data
adobe_layoffs = df.loc[df['company'] == 'Adobe', 'layoffs']
#print(adobe_layoffs.head())
adobe_hires = df.loc[df['company'] == 'Adobe', 'new_hires']
#print(adobe_hires.head())

adobe_data = df[df['company'] == 'Adobe'].groupby('year').sum()

# plt.plot(amd_data.index, amd_data['layoffs'], label='Layoffs', color='crimson', marker='o', linewidth=2)
# plt.plot(amd_data.index, amd_data['new_hires'], label='New Hires', color='seagreen', marker='s', linewidth=2)
# plt.title('AMD Layoffs and New Hires by Year')
# plt.xlabel('Year')
# plt.ylabel('Employment')
# plt.legend()
# plt.savefig(f'charts/AMD.png')
# plt.show()
# print(f'saving image to charts/AMD.png')



amd_data[['layoffs', 'new_hires']].plot(
    kind='bar',
    color=['crimson', 'seagreen'],
    label=['Layoffs', 'New Hires'],
    rot=45
)

plt.title('AMD Layoffs and New Hires by Year')
plt.xlabel('Year')
plt.ylabel('Employment')
plt.grid(color='grey', linestyle=':', linewidth=1.0, axis='y', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('charts/AMD.png')
#plt.show()
print('Saving image to charts/AMD.png')


#Stacked Bar Chart
years = amd_data.index
#sets position so bars are stacked instead of side by side.
x = range(len(years))

plt.bar(x, amd_data['new_hires'], color='seagreen', label='New Hires')
plt.bar(x, -amd_data['layoffs'], color='crimson', label='Layoffs')

# Trend lines
hires_trend = amd_data['new_hires'].rolling(2, min_periods=1).mean()
layoffs_trend = amd_data['layoffs'].rolling(2, min_periods=1).mean()

plt.plot(x, hires_trend, color='darkgreen', linewidth=2, label='New Hires Trend')
plt.plot(x, -layoffs_trend, color='darkred', linewidth=2, label='Layoffs Trend')

plt.axhline(0, color='black', linewidth=2)
plt.xticks(x, years, rotation=45)
plt.title('AMD Layoffs and New Hires by Year')
plt.xlabel('Year')
plt.ylabel('Employment')
plt.grid(color='grey', linestyle=':', linewidth=1.0, axis='y', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('charts/AMD_diverging.png')
#plt.show()
print('Saving image to charts/AMD_diverging.png')


# AMD vs Adobe Layoffs Comparison
all_years = sorted(set(amd_data.index) | set(adobe_data.index))
x = range(len(all_years))

amd_layoffs_aligned = amd_data['layoffs'].reindex(all_years, fill_value=0)
adobe_layoffs_aligned = adobe_data['layoffs'].reindex(all_years, fill_value=0)

plt.bar([i - 0.2 for i in x], amd_layoffs_aligned, width=0.4, color='crimson', label='AMD Layoffs')
plt.bar([i + 0.2 for i in x], adobe_layoffs_aligned, width=0.4, color='steelblue', label='Adobe Layoffs')

plt.xticks(x, all_years, rotation=45)
plt.title('AMD vs Adobe Layoffs by Year')
plt.xlabel('Year')
plt.ylabel('Layoffs')
plt.grid(color='grey', linestyle=':', linewidth=1.0, axis='y', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('charts/AMD_vs_Adobe_layoffs.png')
#plt.show()
print('Saving image to charts/AMD_vs_Adobe_layoffs.png')
print ('All Work Complete')
