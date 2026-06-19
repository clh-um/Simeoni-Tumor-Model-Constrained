# KIE4024 Optimization Methods: Case II (Constrained TGI Model)

**Course:** KIE4024 Optimization Methods (2025/2026 Sem 2)
**Institution:** Universiti Malaya
**Topic:** Optimal Control of Tumor Growth Inhibition (TGI) using the Simeoni Model

This repository contains the simulation code, data, and visualizations for **Case II** of the assignment. 
*(Note: Case I was handled by my teammate and is hosted in a separate repository).*

---

## Project Overview

This project applies optimal control theory to the **Augmented Simeoni Tumor Growth Inhibition (TGI) Model** to determine an optimal 5-day pulsed chemotherapy schedule. 

While Case I explored the unconstrained optimal control problem, **Case II** introduces a critical clinical toxicity constraint. To protect the patient from acute drug poisoning, a hard state constraint was placed on the drug plasma concentration: 
**`q(t) ≤ 0.4 mg/kg`**.

This repository demonstrates how this constraint restricts the solver from using a massive initial dose, forcing a shift towards a prolonged, sub-lethal compensatory pulsing strategy, and driving the cumulative mathematical cost higher due to prolonged tumor survival.

---

## Repository Structure

* **`/AMPL/`**: Contains the mathematical formulation (`.mod`) and execution commands (`.run`). Due to solver limitations, the problem was solved using the **IPOPT solver via the NEOS Server**.
* **`/Python/`**: Contains the raw comma-separated data exported directly from the NEOS console, along with the Python scripts used to process the data and generate high-quality plots.
* **`/Images/`**: Contains the final output graphs included in the formal report.

---

## How to Reproduce the Results

### 1. AMPL (NEOS Server)
The optimal control problem was discretized using the Trapezoidal Collocation method and solved via the NEOS Server.
1. Navigate to the NEOS Server AMPL submission page.
2. Paste the contents of `AMPL/tumor_model.mod` into the **Model File** box.
3. Paste the contents of `AMPL/execution_script.run` into the **Commands File** box.
4. Execute to generate the optimal solution and CSV output streams.

### 2. Python Visualizations
The exported NEOS data was saved as CSV files to generate the report's graphical evaluations.
1. Ensure you have Python installed along with `pandas` and `matplotlib`.
2. Navigate to the `/Python/` directory.
3. Run `plot_evaluation.py` to generate the 3x2 grid showing States, Optimal Control, Switching Conditions, and Co-States.
4. Run `plot_cost.py` to calculate the integral of the objective function using the Trapezoidal rule and plot the Cumulative Cost curve.

---

## Key Findings (Case II)

* **Constraint Efficacy:** The drug concentration strictly hit the `q(t) = 0.4` ceiling at `t = 0` and subsequently escaped it, shifting to a consistent 0.15 mg/kg sawtooth pattern for the remainder of the 5-day intervals.
* **Objective Function:** Due to the restricted initial dose, the tumor survived longer compared to the unconstrained case. Consequently, the cumulative performance index climbed over an 80-day period, settling at a final optimal cost of **J = 731.748**.
