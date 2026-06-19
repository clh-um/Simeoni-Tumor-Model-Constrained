# Parameters
param N := 100;         
param dt := 1;          

param L0 := 0.14202;
param L1 := 0.07618;
param psi := 20;
param k1 := 0.2381;
param k2 := 4.22;
param k10 := 0.5;
param V := 1.0;
param Rs := 25;

# Decision Variables
var z0{0..N} >= 0;
var z1{0..N} >= 0;
var z2{0..N} >= 0;
var z3{0..N} >= 0;
var q{0..N}  >= 0;
var u{0..N}  >= 0;
var w{i in 0..N} = z0[i] + z1[i] + z2[i] + z3[i];

# Growth function substitute
var G{i in 0..N} = L0 / ((1 + (L0/L1 * w[i])^psi)^(1/psi));

# Objective Function
minimize Total_Cost:
    0.5 * sum{i in 0..N-1} (
        (1000*(z0[i]^2 + z1[i]^2 + z2[i]^2 + z3[i]^2) + 0.04*q[i]^2 + Rs*u[i]^2) + 
        (1000*(z0[i+1]^2 + z1[i+1]^2 + z2[i+1]^2 + z3[i+1]^2) + 0.04*q[i+1]^2 + Rs*u[i+1]^2)
    ) * dt / 2;

# Dynamic Constraints (Trapezoidal Rule)
subject to Dz0 {i in 0..N-1}:
    z0[i+1] - z0[i] = (dt/2) * ((G[i]*z0[i] - k2*(q[i]/V)*z0[i]) + (G[i+1]*z0[i+1] - k2*(q[i+1]/V)*z0[i+1]));

subject to Dz1 {i in 0..N-1}:
    z1[i+1] - z1[i] = (dt/2) * ((k2*(q[i]/V)*z0[i] - k1*z1[i]) + (k2*(q[i+1]/V)*z0[i+1] - k1*z1[i+1]));

subject to Dz2 {i in 0..N-1}:
    z2[i+1] - z2[i] = (dt/2) * ((k1*(z1[i] - z2[i])) + (k1*(z1[i+1] - z2[i+1])));

subject to Dz3 {i in 0..N-1}:
    z3[i+1] - z3[i] = (dt/2) * ((k1*(z2[i] - z3[i])) + (k1*(z2[i+1] - z3[i+1])));

subject to Dq {i in 0..N-1}:
    q[i+1] - q[i] = (dt/2) * ((-k10*q[i] + u[i]) + (-k10*q[i+1] + u[i+1]));

# Initial Conditions
subject to Init_z0: z0[0] = 0.5;
subject to Init_z1: z1[0] = 0.0;
subject to Init_z2: z2[0] = 0.0;
subject to Init_z3: z3[0] = 0.0;
subject to Init_q:  q[0]  = 0.0;

# 5-Day Pulsed Chemotherapy Window Constraint
subject to Pulse_Constraint {i in 0..N: i mod 5 != 0}:
    u[i] = 0;

# Case II Constraint: Toxicity Limit
subject to Toxicity_Limit {i in 0..N}: q[i] <= 0.4;