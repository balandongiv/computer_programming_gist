import pandas as pd
import matplotlib.pyplot as plt


results_df=pd.read_excel("simulation_results.xlsx")

# Box Plot: dirt_collected for each num_bots

results_df.boxplot(column='dirt_collected', by='num_bots')
plt.title('Box Plot of Dirt Collected by Number of Bots')
plt.suptitle('')
plt.xlabel('Number of Bots')
plt.ylabel('Dirt Collected')
plt.grid(True)
plt.show()

# Line Plot: average dirt_collected vs. num_bots
avg_dirt = results_df.groupby('num_bots')['dirt_collected'].mean().reset_index()

plt.figure()
plt.plot(avg_dirt['num_bots'], avg_dirt['dirt_collected'], marker='o')
plt.title('Average Dirt Collected vs Number of Bots')
plt.xlabel('Number of Bots')
plt.ylabel('Average Dirt Collected')
plt.grid(True)
plt.show()
