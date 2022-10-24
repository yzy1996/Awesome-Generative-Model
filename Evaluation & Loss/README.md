# Evaluation & Loss for Generative Model





## For 3D Point Clouds

There are two setpoints clouds A and B, and we hope to use some useful metrics to measure the accurancy.

- JSD (Jensen-Shannon Divergence)
  $$
  J S D\left(P_{A} \| P_{B}\right)=\frac{1}{2} D\left(P_{A} \| M\right)+\frac{1}{2} D\left(P_{B} \| M\right)
  $$
  where $M = \frac{1}{2} (P_A + P_B)$



### Chamfer Distance



[github](https://github.com/ThibaultGROUEIX/ChamferDistancePytorch)





