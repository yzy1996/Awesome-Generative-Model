<h1 <p align=center> Diffusion Model</h1>
<div align="center">


有关学习资料，可以看我写的[知乎文章](https://zhuanlan.zhihu.com/p/565901160)；[Awesome-Diffusion-Models](https://github.com/heejkoo/Awesome-Diffusion-Models)
</div>


https://scorebasedgenerativemodeling.github.io/

## Introduction

From DDPM, a diffusion probabilistic model (which we call ‘diffusion model’ for brevity) is a **parameterized Markov chain trained using variational inference to produce samples matching the data after finite time**.

Diffusion models are straightforward to define and efficient to train, but are not capable of generating high quality samples.



Diffusion models consist of two processes: forward diffusion and parametrized reverse. A forward diffusion process maps data to noise by gradually perturbing the input data. At each step of this process, Gaussian noise is incrementally added to the data. The second process is a parametrized reverse process that undoes the forward diffusion and performs iterative denoising.









## Branch

- [Sample-Efficiency](./Sample-Efficiency)



## Selected Literature

> To see full list, please see the subfolder.

- [(DDPM)Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)  
  **[`NeurIPS 2020`]** *Jonathan Ho, Ajay Jain, Pieter Abbeel*  

- [(DDIM)Denoising Diffusion Implicit Models](https://arxiv.org/abs/2010.02502)
  **[`ICLR 2021`]** *Jiaming Song, Chenlin Meng, Stefano Ermon*

- [Improved Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2102.09672)  
  **[`ICML 2021`]** *Alex Nichol, Prafulla Dhariwal*  

- [(Stable)High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)  
  **[`CVPR 2022`]** *Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer*  

- 





综述

https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy







**关于 Score-based generative model 宋飏博士的几个承接工作：**

- [Sliced Score Matching: A Scalable Approach to Density and Score Estimation](https://arxiv.org/abs/1905.07088)
  **[`UAI 2019`]** *Yang Song, Sahaj Garg, Jiaxin Shi, Stefano Ermon*
- [Generative Modeling by Estimating Gradients of the Data Distribution](https://arxiv.org/abs/1907.05600)
  **[`NeurIPS 2019`]** *Yang Song, Stefano Ermon*
- [Improved Techniques for Training Score-Based Generative Models](https://arxiv.org/abs/2006.09011)  
  **[`NeurIPS 2020`]** *Yang Song, Stefano Ermon*
- [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456)
  **[`ICLR 2021`]** *Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, Ben Poole*

