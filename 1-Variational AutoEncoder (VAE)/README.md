# Variational Auto-Encoder (VAE)

The goal of VAEs is to train a genrative model in the form of $p(x, z) = p(z) p(x|z)$ where $p(z)$ is a prior distribution over latent variables $z$ and $p(x|z)$ is the likelihood function or decoder that generates data $x$ given latent variables $z$. 

Since the true posterior $p(z|x)$ is in general intractable, the generative model is trained with the aid of an approximate posterior distribution or encoder $q(z|x)$.



The majority of the research efforts on improving VAEs is dedicated to the statistical challenges, such as:

- reducing the gap between approximate and true posterior distribution
- formulatig tighter bounds
- reducing the gradient noise
- extending VAEs to discrete variables
- tackling posterior collapse
- designing special network architectures
  - previous work just borrows the architectures from the classification tasks



<details><summary><b>介绍</b></summary><p>

有一个mean和一个log_var

当目标分布是 $\mathcal{N}(0,1^2)$ 时，mean=0, log_var=0

当目标分布是 $\mathcal{N}(0,0.01^2)$ 时，mean=0, log_var=-9

而当mean和log_var也是分布的时候，比如初始化都是 $\mathcal{N}(0, 1^2)$

就应该分别变化到，$\mathcal{N}(0, 0.01^2)$ $\mathcal{N}(-9, 0.01^2)$ 波动小比较好



VAEs maximize the mutual information between the input and latent variables, requiring the networks to retain the information content of the input data as much as possible.

Information maximization in noisy channels: A variational approach  
**[`NeurIPS 2017`]**

Deep variational information bottleneck  
**[`ICLR 2017`]**



参考：

https://www.jeremyjordan.me/variational-autoencoders/

https://www.jeremyjordan.me/autoencoders/

https://jaan.io/what-is-variational-autoencoder-vae-tutorial/

</p></details>



## Literature

- [Variational Inference: A Review for Statisticians](https://arxiv.org/abs/1601.00670)  
  **[`arXiv 2016`]** *David M. Blei, Alp Kucukelbir, Jon D. McAuliffe* 
- [Tutorial on Variational Autoencoders](https://arxiv.org/abs/1606.05908)  
  **[`arXiv 2016`]** *Carl Doersch* 
- [A Tutorial on VAEs: From Bayes' Rule to Lossless Compression](https://arxiv.org/abs/2006.10273)  
  **[`arXiv 2020`]** *Ronald Yu* 



- [Neural Algebra of Classifiers](https://arxiv.org/abs/1801.08676)  
  **[`arXiv 2018`]** *Rodrigo Santa Cruz, Basura Fernando, Anoop Cherian, Stephen Gould* 
- [Autoencoding beyond pixels using a learned similarity metric](https://arxiv.org/abs/1512.09300)  
  **[`arXiv 2015`]** *Anders Boesen Lindbo Larsen, Søren Kaae Sønderby, Hugo Larochelle, Ole Winther* 
- [Ladder Variational Autoencoders](https://arxiv.org/abs/1602.02282)  
  **[`arXiv 2016`]** *Casper Kaae Sønderby, Tapani Raiko, Lars Maaløe, Søren Kaae Sønderby, Ole Winther* 
- [Neural Discrete Representation Learning](https://arxiv.org/abs/1711.00937)  
  **[`NeurIPS 2017`]** *Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu* 
- [Avoiding Latent Variable Collapse With Generative Skip Models](https://arxiv.org/abs/1807.04863)  
  **[`arXiv 2018`]** *Adji B. Dieng, Yoon Kim, Alexander M. Rush, David M. Blei* 
- [Inference Suboptimality in Variational Autoencoders](https://arxiv.org/abs/1801.03558)  
  **[`arXiv 2018`]** *Chris Cremer, Xuechen Li, David Duvenaud* 
- [Understanding disentangling in $β$-VAE](https://arxiv.org/abs/1804.03599)  
  **[`arXiv 2018`]** *Christopher P. Burgess, Irina Higgins, Arka Pal, Loic Matthey, Nick Watters, Guillaume Desjardins, Alexander Lerchner* 
- [Wasserstein Auto-Encoders](https://arxiv.org/abs/1711.01558)  
  **[`ICLR 2018`]** *Ilya Tolstikhin, Olivier Bousquet, Sylvain Gelly, Bernhard Schoelkopf* 
- [Concrete Autoencoders for Differentiable Feature Selection and Reconstruction](https://arxiv.org/abs/1901.09346)  
  **[`ICML 2019`]** *Abubakar Abid, Muhammad Fatih Balin, James Zou* 
- [Generating Diverse High-Fidelity Images with VQ-VAE-2](https://arxiv.org/abs/1906.00446)  
  **[`arXiv 2019`]** *Ali Razavi, Aaron van den Oord, Oriol Vinyals* 
- [An Introduction to Variational Autoencoders](https://arxiv.org/abs/1906.02691)  
  **[`arXiv 2019`]** *Diederik P. Kingma, Max Welling* 
- [BIVA: A Very Deep Hierarchy of Latent Variables for Generative Modeling](https://arxiv.org/abs/1902.02102)  
  **[`arXiv 2019`]** *Lars Maaløe, Marco Fraccaro, Valentin Liévin, Ole Winther* 
- [Evidential Sparsification of Multimodal Latent Spaces in Conditional Variational Autoencoders](https://arxiv.org/abs/2010.09164)  
  **[`NeurIPS 2020`]** *Masha Itkina, Boris Ivanovic, Ransalu Senanayake, Mykel J. Kochenderfer, Marco Pavone* 
- [A Contrastive Learning Approach for Training Variational Autoencoder Priors](https://arxiv.org/abs/2010.02917)  
  **[`NeurIPS 2021`]** *Jyoti Aneja, Alexander Schwing, Jan Kautz, Arash Vahdat* 
- [NVAE: A Deep Hierarchical Variational Autoencoder](https://arxiv.org/abs/2007.03898)  
  **[`NeurIPS 2020`]** *Arash Vahdat, Jan Kautz* 
- [PatchVAE: Learning Local Latent Codes for Recognition](https://arxiv.org/abs/2004.03623)  
  **[`CVPR 2020`]** *Kamal Gupta, Saurabh Singh, Abhinav Shrivastava* 
- [AASAE: Augmentation-Augmented Stochastic Autoencoders](https://arxiv.org/abs/2107.12329)  
  **[`arXiv 2021`]** *William Falcon, Ananya Harsh Jha, Teddy Koker, Kyunghyun Cho* 
- [Variational autoencoders in the presence of low-dimensional data: landscape and implicit bias](https://arxiv.org/abs/2112.06868)  
  **[`ICLR 2022`]** *Frederic Koehler, Viraj Mehta, Chenghui Zhou, Andrej Risteski* 
