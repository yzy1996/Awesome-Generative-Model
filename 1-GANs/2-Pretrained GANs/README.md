# <p align=center>`Pretrained GANs`</p>



Can be related to controllable GAN and GAN inversion.





## Introduction

Some methods finetune pretrained GANs on new datasets, which typically results in higher performance coompared to training from scratch, especially in the limited-data regime.

To extend the success of GANs to the limited-data regime, it is common to use pretraining.



image-to-image translation can be done by injecting encoded features to StyleGANs

image inpainting and outpainting can realized by locating the appropriate codes in the latent space



design different latent optimizationmethods to do inpainting, style transfer, morphing, colorization,denoising and super resolution



use the generator as a fixeddecoder, and facilitate disentanglement by training an encoderfor identity and another encoder for pose.



Richardsonet al. do image translation by training encoders fromsketches or semantic maps into StyleGAN’s W space.



This is built upon the foundation that recent GANs provides a naturally disentangled latet space for generation.



In contrast to training-based methods, pre-trained GANs are proved to naturally have good disentanglement property. Manipulation in the latent space causing directly semantic changes into the image space.



## Code

[lucidrains/stylegan2-pytorch](lucidrains/stylegan2-pytorch)

[rosinality/stylegan2-pytorch](rosinality/stylegan2-pytorch)

[NVlabs/stylegan2-ada-pytorch](NVlabs/stylegan2-ada-pytorch)



the pre-trained model contains



## Literature



### Using pertained-gan for classification

[This dataset does not exist: training models from generated images](https://arxiv.org/pdf/1911.02888.pdf)  
Victor Besnier, Himalaya Jain, Andrei Bursuc, Matthieu Cord, Patrick Pérez  
[ICASSP 2020]

[Ensembling with Deep Generative Views](https://arxiv.org/pdf/2104.14551.pdf)  
Lucy Chai, Jun-Yan Zhu, Eli Shechtman, Phillip Isola, Richard Zhang  
[CVPR 2021]

[Generative Interventions for Causal Learning](https://arxiv.org/pdf/2012.12265.pdf)  
Chengzhi Mao, Augustine Cha, Amogh Gupta, Hao Wang, Junfeng Yang, Carl Vondrick  
[CVPR2021]

[Data Augmentation Using GANs](https://arxiv.org/pdf/1904.09135.pdf)  
Fabio Henrique Kiyoiti dos Santos Tanaka, Claus Aranha  
[ACML 2019]

[Conditional Infilling GANs for Data Augmentation in Mammogram Classification](https://arxiv.org/pdf/1807.08093.pdf)  
Eric Wu, Kevin Wu, David Cox, William Lotter  
[MICCAI 2018]





### Using pertained-gan for segmentation

[Finding an Unsupervised Image Segmenter in Each of Your Deep Generative Models](https://arxiv.org/pdf/2105.08127.pdf)  
Luke Melas-Kyriazi, Christian Rupprecht, Iro Laina, Andrea Vedaldi  







## Literature

[Transferring GANs: generating images from limited data](https://arxiv.org/pdf/1805.01677.pdf)  
*Yaxing Wang, Chenshen Wu, Luis Herranz, Joost van de Weijer, Abel Gonzalez-Garcia, Bogdan Raducanu*  
**[`ECCV 2018`] (`UAB`)**

[Seeing What a GAN Cannot Generate](https://arxiv.org/pdf/1910.11626.pdf)  
David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba  
**[`ICCV 2019`]  (`MIT, CUHK`)**  [[Code](https://github.com/davidbau/ganseeing)]



[Projected GANs Converge Faster](https://arxiv.org/pdf/2111.01007.pdf)  
*Axel Sauer, Kashyap Chitta, Jens Müller, Andreas Geiger*  
**[`NeurIPS 2021`] (`MPI`)**





Image2stylegan:How to embed images into the stylegan latentspace?

Style generator inversionfor image enhancement and animation.

Image processingusing multi-code GAN prior

Exploiting deep generativeprior for versatile image restoration and manipulation

Disentangling in latent space by harnessing a pretrainedgenerator.

Encodingin style: a stylegan encoder for image-to-image translation
