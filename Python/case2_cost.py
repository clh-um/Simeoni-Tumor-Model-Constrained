import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the new data
try:
    df = pd.read_csv('D:/Ryan/UM/Academic/Y4S2/KIE4024 OPTIMIZATION METHODS/Assignment/case2_cost_data.csv')
except FileNotFoundError:
    print("Please ensure 'case2_cost_data.csv' is saved in the same directory.")
    exit()

# 2. Calculate the instantaneous cost rate at each time step
# Formula: 0.5 * [1000*(z0^2 + z1^2 + z2^2 + z3^2) + 0.04*q^2 + 25*u^2]
cost_rate = 0.5 * (
    1000 * (df['z0']**2 + df['z1']**2 + df['z2']**2 + df['z3']**2) + 
    0.04 * df['q']**2 + 
    25 * df['u']**2
)

# 3. Integrate using the Trapezoidal rule to get Cumulative Cost J(t)
cumulative_cost = np.zeros(len(df))
for i in range(1, len(df)):
    dt = df['time'].iloc[i] - df['time'].iloc[i-1]
    # Area of trapezoid = base * average height
    cumulative_cost[i] = cumulative_cost[i-1] + dt * (cost_rate.iloc[i] + cost_rate.iloc[i-1]) / 2.0

# 4. Plot the graph
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(10, 5))

# Plot the cumulative cost curve
plt.plot(df['time'], cumulative_cost, color='purple', linewidth=2)

# Formatting to match your Case I report
plt.title('Cumulative Cost: Integral J(t) [Case II]', fontweight='bold')
plt.ylabel('Cumulative Cost')
plt.xlabel('Time t (days)')

# Add a text box to display the final optimal value
final_cost = cumulative_cost[-1]
plt.text(80, final_cost * 0.85, f'Final J = {final_cost:.3f}', 
         fontsize=12, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='purple'))

plt.tight_layout()
plt.savefig('Case2_Cumulative_Cost.png', dpi=300)
plt.show()