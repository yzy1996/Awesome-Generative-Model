# <p align=center>`Style-Transfer & Image2image`</p>



[CR-GAN](#CR-GAN)

---

<span id="CR-GAN"></span>
[Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/pdf/1703.10593)  
*Jun-Yan Zhu, Taesung Park, Phillip Isola, Alexei A. Efros*  
**[`ICCV 2017`] (`UCB`)**

<details><summary>Click to expand</summary>
> **Summary**

这里的generator跟*Perceptual losses for real-time style transfer and super-resolution*是一样的。他们使用了Instance Normalization。判别器使用的和pix2pix一样(PatchGAN on 70x70 patches). 为了稳定GAN的训练，他们使用了最小二乘gan（least square gan）和 Replay buffer。不像pix2pix，他们的模型没有任何的随机性。（没有随机输入z，没有dropout）这里的生成器更像是一个deteministic的style transfer模型，而不是一个条件GAN。他们使用了L1距离作为cycle consistency.
DualGAN:他们的生成器和判别器都和pix2pix一样 (没有随机输入z，但是有dropout的随机)。 他们用了wgan来训练。cycle consistency同样选用了l1。
DiscoGAN:他们用了conv，deconv和leaky relu组成了生成器，然后一个conv+leaky relu作为判别器。他们用l2作为cycle consistency。

> https://zhuanlan.zhihu.com/p/26332365

</details>

---

