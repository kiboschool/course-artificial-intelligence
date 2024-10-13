# Exercise: One-variable Linear Regression

Here is a sample dataset that contains the mid-term and final exam scores of 10 students. The goal is to predict the final exam score based on the mid-term exam score.

| Mid-term | Final |
|----------|-------|
| 70       | 80    |
| 80       | 90    |
| 90       | 100   |
| 60       | 70    |
| 50       | 65    |
| 40       | 50    |
| 30       | 40    |
| 20       | 30    |
| 10       | 20    |
| 0        | 10    |

Questions:
1. What is the number of features in this dataset?
2. What is the number of data points (m) in this dataset?
3. Which of these `w` and `b` values will give the smallest cost function?
    - `w = 1` and `b = 10`
    - `w = 0.5` and `b = 20`
    - `w = 3` and `b = 7`

4. Write a simple Python code to calculate the cost function for each set of `w` and `b` values and try different values to find the smallest cost function.

<Details>
<Summary>Answer</Summary>

1. There is only **one** feature (X) in this dataset which is the mid-term exam score. The final exam score is the label (Y) that we are trying to predict.

2. The number of data points (m) is 10. There are 10 students in this dataset.

3. `w = 1` and `b = 10` will give the smallest cost function. You can try that manually or use this code to calculate the cost function for each set of values:

```python
import numpy as np

# Given dataset
mid_term_scores = np.array([70, 80, 90, 60, 50, 40, 30, 20, 10, 0])
final_scores = np.array([80, 90, 100, 70, 65, 50, 40, 30, 20, 10])

# # Calculate the mean squared error (MSE) for given values of w and b

def calculate_mse(w, b):
    predicted_final = w * mid_term_scores + b
    m = len(mid_term_scores)
    mse = (1/(2*m)) * np.sum((predicted_final - final_scores)**2)
    return predicted_final, mse

# Test cases
w_values = [1, 0.5, 3]
b_values = [10, 20, 7]

for w, b in zip(w_values, b_values):
    predicted_final, mse = calculate_mse(w, b)
    print(f"For w = {w} and b = {b}:")
    print("Predicted Final Scores:", predicted_final)
    print("Mean Squared Error (MSE):", mse)
    print()
```
</Details>



