import pandas as pd
import matplotlib.pyplot as plt

# Load the results
results = pd.read_csv('result.csv')

# Plotting
plt.bar(results['Model'], results['Topsis Score'], color='skyblue')
plt.xlabel('Models')
plt.ylabel('Topsis Score')
plt.title('TOPSIS Scores for Pre-trained Models')
plt.show()
