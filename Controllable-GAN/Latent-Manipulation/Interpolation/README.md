## Introduction

interpolation or extrapolation



why do we care about:

faithful data interpolation can be seen as a measure of the generalisation capacity of the a learning system (model + latent space)



The task of data interpolation is to extra new samples between known data samples.



The interpolation often leads to artifacts or produce unrealistic results during reconstruction.

This is because the naively interpolated latent vectors deviate from the data manifold.



We can regard the interpolate manifold as S1

we hope is consistent with the training images 

the manifold is smooth and locally convex



so we need to consider the geometry and shape of the manifold



[Understanding and Improving Interpolation in Autoencoders via an Adversarial Regularizer](https://arxiv.org/pdf/1807.07543.pdf)  
*David Berthelot, Colin Raffel, Aurko Roy, Ian Goodfellow*  
**[`ICLR 2019`] (`Google Brain`)**

[Autoencoder Image Interpolation by Shaping the Latent Space](https://arxiv.org/pdf/2008.01487.pdf)  
*Alon Oring, Zohar Yakhini, Yacov Hel-Or*  
**[`ICML 2021`] (`Israel`)**

[Learning low bending and low distortion manifold embeddings](https://arxiv.org/pdf/2104.13189.pdf)  
*Juliane Braunsmann, Marko Rajković, Martin Rumpf, Benedikt Wirth*  
**[`CVPRW 2021`] (`Univerity of Munster`)**







## How to measure the performance of interpolation?

