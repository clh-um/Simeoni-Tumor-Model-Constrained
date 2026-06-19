import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data exported from NEOS AMPL
try:
    df = pd.read_csv('D:/Ryan/UM/Academic/Y4S2/KIE4024 OPTIMIZATION METHODS/Assignment/case2_results.csv')
except FileNotFoundError:
    print("Please ensure 'case2_results.csv' is saved in the same directory.")
    exit()

t = df['time']
w = df['w']
q = df['q']
u = df['u']
lam_z0 = df['lambda_z0']
lam_q = df['lambda_q']
phi = df['Phi']

# 2. Set up the figure styling
plt.style.use('seaborn-v0_8-whitegrid')
fig, axs = plt.subplots(3, 2, figsize=(15, 15))
fig.tight_layout(pad=6.0)

# --- Row 1: States ---
# Tumor Weight w(t)
axs[0, 0].plot(t, w, color='teal', linewidth=2)
axs[0, 0].set_title('State: Total Tumor Weight w(t)', fontweight='bold')
axs[0, 0].set_ylabel('Weight (g)')
axs[0, 0].set_xlabel('Time t (days)')

# Drug Concentration q(t)
axs[0, 1].plot(t, q, color='darkorange', linewidth=2)
axs[0, 1].axhline(y=0.4, color='red', linestyle='--', label='Toxicity Limit (0.4 mg/kg)')
axs[0, 1].set_title('State: Drug Concentration q(t)', fontweight='bold')
axs[0, 1].set_ylabel('Concentration (mg/kg)')
axs[0, 1].set_xlabel('Time t (days)')
axs[0, 1].legend()

# --- Row 2: Control & Switching Condition ---
# Optimal Control u(t)
axs[1, 0].stem(t, u, linefmt='darkred', markerfmt='D', basefmt=' ')
axs[1, 0].set_title('Optimal Control: Drug Dose u(t)', fontweight='bold')
axs[1, 0].set_ylabel('Dose (mg/kg)')
axs[1, 0].set_xlabel('Time t (days)')

# Switching Condition Phi(t)
axs[1, 1].plot(t, phi, color='steelblue', linewidth=1.5)
axs[1, 1].axhline(y=0, color='black', linestyle='-', linewidth=1)
axs[1, 1].set_title('Switching Condition Φ(t)', fontweight='bold')
axs[1, 1].set_ylabel('Φ(t)')
axs[1, 1].set_xlabel('Time t (days)')

# --- Row 3: Co-States ---
# Tumor Co-State lambda_z0(t)
axs[2, 0].plot(t, lam_z0, color='purple', linewidth=2)
axs[2, 0].set_title('Costate Variable λ_z0(t) [Proliferating Core]', fontweight='bold')
axs[2, 0].set_ylabel('Costate λ_z0(t)')
axs[2, 0].set_xlabel('Time t (days)')

# Drug Co-State lambda_q(t)
axs[2, 1].plot(t, lam_q, color='gray', linewidth=2)
axs[2, 1].axhline(y=0, color='black', linestyle=':', linewidth=1)
axs[2, 1].set_title('Costate Variable λ_q(t) [Drug Toxicity]', fontweight='bold')
axs[2, 1].set_ylabel('Costate λ_q(t)')
axs[2, 1].set_xlabel('Time t (days)')

# Show and save the plot for the report
plt.savefig('Case2_Graphical_Evaluation.png', dpi=300, bbox_inches='tight')
plt.show()