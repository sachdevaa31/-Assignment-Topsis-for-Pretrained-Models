import pandas as pd
import numpy as np
import sys

def topsis(datafile, weights, impacts, resultfile):
    try:
        print("Step 1: Reading dataset...")
        
        # Try to read the CSV with a specified encoding and handle bad lines
        data = pd.read_csv(datafile, encoding='ISO-8859-1', delimiter=',', on_bad_lines='skip')

        print("Data loaded successfully:")
        print(data.head())

        data_values = data.iloc[:, 1:].values
        
        print("Step 2: Processing weights and impacts...")
        
        # Convert weights to integers and impacts to a list of strings
        weights = [float(w) for w in weights.split(',')]  # Changed to float for better precision
        impacts = impacts.split(',')
        print(f"Weights: {weights}, Impacts: {impacts}")

        # Ensure that the number of weights matches the number of criteria
        if len(weights) != data_values.shape[1]:
            raise ValueError("The number of weights must match the number of criteria in the dataset.")
        
        if len(impacts) != data_values.shape[1]:
            raise ValueError("The number of impacts must match the number of criteria in the dataset.")
        
        # Step 3: Normalize the data
        print("Step 3: Normalizing data...")
        norm_data = data_values / np.sqrt((data_values**2).sum(axis=0))

        # Step 4: Apply weights
        weighted_data = norm_data * weights
        print("Weighted data calculated.")

        # Step 5: Identify ideal best and ideal worst
        ideal_best = np.max(weighted_data, axis=0) if '+' in impacts else np.min(weighted_data, axis=0)
        ideal_worst = np.min(weighted_data, axis=0) if '-' in impacts else np.max(weighted_data, axis=0)
        print(f"Ideal Best: {ideal_best}, Ideal Worst: {ideal_worst}")

        # Step 6: Calculate distances
        dist_best = np.sqrt(((weighted_data - ideal_best)**2).sum(axis=1))
        dist_worst = np.sqrt(((weighted_data - ideal_worst)**2).sum(axis=1))
        print("Distances calculated.")

        # Step 7: Calculate TOPSIS score
        score = dist_worst / (dist_best + dist_worst)
        data['Topsis Score'] = score
        data['Rank'] = data['Topsis Score'].rank(ascending=False)

        # Save the results
        print(f"Saving results to {resultfile}...")
        data.to_csv(resultfile, index=False)
        print(f"Result saved to {resultfile}")

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 topsis.py <inputfile> <weights> <impacts> <outputfile>")
    else:
        topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
