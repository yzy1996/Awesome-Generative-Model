The StyleGAN/StyleGAN2 generation process involves a number of latent spaces:

- $\mathcal{Z}$ Space
- $\mathcal{W}$ Space
- $\mathcal{W}+$ Space
- $\mathcal{S}$ Space



$\mathcal{W}+$ is mainly used for style mixing and image inversion.





几个疑问：

什么是 channel-wise activation statistics (means and variances)



## Background

> 都是作用在channel-wise activation statistics.

- BigGAN uses class-conditional BatchNorm

- StyleGAN uses AdaIN to modulatechannel-wise means and variances

- StyleGAN2 controlschannel-wise variances by modulating the weights ofthe convolution kernels



> 过去的经验，怎么解耦的效果比较好呢？

- the intermediatelatent space is more disentangled than the initialone



## Space

`latent space W` StyleGAN, StyleGAN2

`latent space W+` Image2StyleGAN

`latent space S` StyleSpace Analysis



StyleGAN2 分辨率 1024*1024，有18层layers

W是512维

W+是9216维

S是9088维，





首先是一个关于DCI (disentanglement | completeness | informativeness) metrics 





## Literature



> W+

A style-basedgenerator architecture for generative adversarial networks

Analyzing and improvingthe image quality of StyleGAN

Indomain GAN inversion for real image editing







perceptual loss







## Code

如何获得W空间



Z空间就直接随机生成就好了，10000张图

```python
```



参考[interfacegan](https://github.com/genforce/interfacegan)













**解读 StyleSpace Analysis**

<img src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/image-20220410163940204.png" alt="image-20220410163940204" style="zoom:50%;" />

核心是要找到一个新的S空间，而这个空间是怎么找出来的呢







