import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data correctly (using read_csv)
file_path = r"D:\Piyal_DMV_Lab\football analysis\football.csv"
df = pd.read_csv(file_path)

# --- Replace 'Column_Name' with your actual column names below ---

# 1. Bar Chart (Great for comparing categories, like goals per team)
plt.figure(figsize=(8, 5))
df['PLAYER NAME'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Goals per Team')
plt.xlabel('Team Name')
plt.ylabel('Count')
plt.show()

# 2. Line Chart (Best for showing trends over time)
plt.figure(figsize=(8, 5))
plt.plot(df['Match_Date'], df['Score'], marker='o', linestyle='-')
plt.title('Score Trend Over Time')
plt.xticks(rotation=45)
plt.show()

# 3. Pie Chart (Shows proportions of a whole)
plt.figure(figsize=(7, 7))
df['Result'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Win/Loss/Draw Distribution')
plt.ylabel('') # Hides the column name on the side
plt.show()

# 4. Stair Chart (Step Plot - shows changes at specific intervals)
plt.figure(figsize=(8, 5))
plt.step(range(len(df)), df['Points'], where='post')
plt.title('Points Progression (Stair Chart)')
plt.show()

# 5. Histogram (Shows the distribution/frequency of numerical data)
plt.figure(figsize=(8, 5))
plt.hist(df['Player_Age'], bins=10, color='green', edgecolor='black')
plt.title('Age Distribution of Players')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()