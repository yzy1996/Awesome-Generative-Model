# <p align=center>`Latent Interpolation & Optimization`</p>



## Introduction



**Definition of interpolation:** (convex combination of data points)

Given a dataset sampled from a target domain $\mathcal{X}$. We are interested in interpolating between two data points $x_i$ and $x_j$ from $\mathcal{X}$. Let the interpolated points between be $\hat{x} = \alpha x_1 + (1 - \alpha)x_2$ for $\alpha \in [0, 1]$. We hope it is highly probable that the interpolated data points $\hat{x}$ belong to $\mathcal{X}$.

  

**Why Bad - underlying theory:**

- due to the structure of the latent space and such naively interpolated latent vectors deviate from the data manifold.
- due to the un-clustered latent points  If the interpolation is not smooth, there may be “discontinuities” in latent space which could result in the representation being less useful as a learned feature.



**Impact**

- widespread use of interpolation as a qualitative measure of autoencoder performance

- faithful data interpolation can be seen as a measure of the generalisation capacity of the a learning system (model + latent space)



## Methods

The core is to shape the latent representation but the specific methods are different. Driving the manifold to be smooth and locally convex.



**For multimodal data:**

- Decode the interpolated latent vectors to fool the discriminator.

- Using an critic network to predict the interpolation parameter $\alpha \in [0, 1]$ while an autoencoder is trained to fool the critic

  > The motivation behind this approach is that the interpolation parameter $\alpha$ can be estimated for badly-interpolated images, while it is unpredictable for faithful interpolation. The data will provide some hint about the interpolation factor.

**For unimodal data / continuous manifold:**







## Literature

- [Generative adversarial interpolative autoencoding: adversarial training on latent space interpolations encourage convex latent distributions](https://arxiv.org/pdf/1807.06650.pdf)  
  *Tim Sainburg, Marvin Thielk, Brad Theilman, Benjamin Migliori, Timothy Gentner*  
  **[`arXiv 2018`] (`UCSD`)**

- [The Riemannian Geometry of Deep Generative Models](https://arxiv.org/pdf/1711.08014.pdf)  
  *Hang Shao, Abhishek Kumar, P. Thomas Fletcher*  
  **[`CVPRW 2018`] (`University of Utah`)**

- [On Adversarial Mixup Resynthesis](https://arxiv.org/pdf/1903.02709.pdf)  
  *Christopher Beckham, Sina Honari, Vikas Verma, Alex Lamb, Farnoosh Ghadiri, R Devon Hjelm, Yoshua Bengio, Christopher Pal*  
  **[`NeurIPS 2019`] (`Mila, Montréal`)**

- [Understanding and Improving Interpolation in Autoencoders via an Adversarial Regularizer](https://arxiv.org/pdf/1807.07543.pdf)  
  *David Berthelot, Colin Raffel, Aurko Roy, Ian Goodfellow*  
  **[`ICLR 2019`] (`Google Brain`)**

- [Avoiding Latent Variable Collapse With Generative Skip Models](https://arxiv.org/pdf/1807.04863.pdf)  
  *Adji B. Dieng, Yoon Kim, Alexander M. Rush, David M. Blei*  
  **[`AISTATS 2019`] (`Columbia, Harvard`)**

- [Learning Flat Latent Manifolds with VAEs](https://arxiv.org/pdf/2002.04881.pdf)  
  *Nutan Chen, Alexej Klushyn, Francesco Ferroni, Justin Bayer, Patrick van der Smagt*  
  **[`ICML 2020`] (`Volkswagen `)**

- [Autoencoder Image Interpolation by Shaping the Latent Space](https://arxiv.org/pdf/2008.01487.pdf)  
  *Alon Oring, Zohar Yakhini, Yacov Hel-Or*  
  **[`ICML 2021`] (`Israel`)**

- [Learning low bending and low distortion manifold embeddings](https://arxiv.org/pdf/2104.13189.pdf)  
  *Juliane Braunsmann, Marko Rajković, Martin Rumpf, Benedikt Wirth*  
  **[`CVPRW 2021`] (`Univerity of Munster`)**





## How to measure the performance of interpolation?

