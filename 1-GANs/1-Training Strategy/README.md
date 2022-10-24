# <p align=center>`GAN Training Strategy`</p>

GAN require a careful **architecture**, **parameter initialisation** and selection of **hyper-parameters**.

This fragility is due to the gap between the model distribution and the data distribution.



the instability in GAN training

[Feature Quantization Improves GAN Training]()



applying orthogonal regularization to teh generator renders 

truncation trick of bigGAN





[(BigGAN) Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/pdf/1809.11096)  
*Andrew Brock, Jeff Donahue, Karen Simonyan*  
**[`arXiv 2018`] (``)**



- Regularisation approches

  

Wasserstein metric makes it easier to converge.





[Seeing What a GAN Cannot Generate](https://arxiv.org/pdf/1910.11626.pdf)  
David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba  
**[`ICCV 2019`]  (`MIT, CUHK`)**  [[Code](https://github.com/davidbau/ganseeing)]



[Projected GANs Converge Faster](https://arxiv.org/pdf/2111.01007.pdf)  
*Axel Sauer, Kashyap Chitta, Jens Müller, Andreas Geiger*  
**[`NeurIPS 2021`] (`MPI`)**

> They find the discriminator cannot fully exploit features from deeper layers of the pretrained model, so they project generated and real samples into a fixed, pretrained feature space.





