import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample NBA player data (Player, PPG, APG, RPG)
data = {
    'Player': ['LeBron James', 'Giannis Antetokounmpo', 'Stephen Curry', 'Luka Doncic', 'Kevin Durant'],
    'PPG': [25.0, 29.9, 30.0, 27.2, 29.1],
    'APG': [7.9, 5.9, 6.3, 8.6, 5.3],  # Assists per game
    'RPG': [7.4, 11.8, 5.2, 8.6, 6.7]  # Rebounds per game
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set the style of the plot
sns.set(style="whitegrid")

# Reshape the data to long format for easier plotting with Seaborn
df_melted = pd.melt(df, id_vars=["Player"], value_vars=["PPG", "APG", "RPG"],
                    var_name="Stat", value_name="Value")

# Create the grouped bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Player', y='Value', hue='Stat', data=df_melted, palette='Set2')

# Add titles and labels
plt.title('NBA Players: Points, Assists, and Rebounds Comparison', fontsize=16)
plt.xlabel('Player', fontsize=12)
plt.ylabel('Value', fontsize=12)

# Rotate player names for readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.show()