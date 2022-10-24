如何让discriminator能够比较稳定的学习出一种feature提取方法，而不是不断忘记旧方法、学习新方法？



**Unsupervised Representation Learning by Predicting Image Rotations**

2018 ICLR

> 在discriminator中加入了判断图片旋转的无监督分类器，来引导discriminator学出来一个好一点的feature提取方法，提升GAN的稳定性。



**Self-Supervised GANs via Auxiliary Rotation Loss**

2019 CVPR

> Discriminator 按之前的方法，输出true、real的判别结果
>
> 取Discriminator倒数第二层的输出，作为feature，加上一个Linear层，预测出旋转的类型



《Unsupervised Representation Learning by Predicting Image Rotations》论文的作者假设：**如果网络不能很好的理解图片中包含的信息，网络就不可能很好的判断出图片旋转的角度。**

在GAN中，对于discriminator来说，**通过约束discriminator让它能识别出旋转角度，有助于让discriminator更好、更全面的理解图片中包含的信息，从而间接引导discriminator学出来一个通用、稳定的feature提取方法。**







