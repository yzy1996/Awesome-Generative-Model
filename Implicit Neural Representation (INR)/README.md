# <p align=center>`Implicit Neural Representation` </p>

[Neural Implicit Representations for 3D Vision and Beyond by Dr. Andreas Geiger](https://www.youtube.com/watch?v=jennURL-gtQ)

https://github.com/vsitzmann/awesome-implicit-representations

## 1. Introduction

*The original idea of augmenting neural networks with coordinates information was proposed in CPPN. The largest popularity of INRs is observed in 3D deep lesrning, where it provides a cheap and continuous way to represent a 3D shape compared to mesh/voxel/pointcloud-based ones.*[^ 1] 



也可以叫 neural implicit function



It's a powerful tool for reconstructing 3D structure from multi-view 2D supervision via fitting their 3D models to the multi-view images using differentiable rendering.



几个经典网络：

- Occupancy Networks

  They model a probability function of a voxel being occupied by a 3D shape and typically employ a coordinate-based decoder that operates on top of single-view images. They also use the multi-resolution surface extraction method.

- DeepSDF 

  It models a signed distance function 



shape and appearance of objects

local parts



Local deep implicit functions for3d shape

Learning shape templates with structured implicit functions



full 3D scenes

Deep local shapes: Learning local sdf priors for detailed 3d reconstruction

Neural unsigned distance fields for implicit function learning

Local implicit grid representations for 3d scenes

Convolutional occupancy networks





## 2. Research Branch/Direction

- Finding an efficient way to encode coordinates positions

Fourier features let networks learn high frequency functions in low dimensional domains

(SIREN )Implicit neural representations with periodic activation functions

> SIREN replaced the popular ReLU activation function withsine functions with modulated frequencies, showing greatsingle scene fitting results.

[](https://arxiv.org/abs/2004.04180)



- Accelerate 

> Implicit neural representations are a new and promising method to represent images and scenes. Implicit neural representations enable good performance on task like view synthesis. Those networks generate an image of scene pixel-by-pixel and are therefore computationally expensive. 





## 3. Literature

Occupancy networks: Learning 3d reconstruction in function space  
[CVPR 2019]

Convolutional occupancy networks  
[ECCV 2020]

3d u-net: learning dense volumetric segmentation from sparse annotation

Msg-gan: Multi-scale gradients for generative adversarial networks  
[CVPR 2020]



- [In-Place Scene Labelling and Understanding with Implicit Scene Representation](https://arxiv.org/pdf/2103.15875)  
  *Shuaifeng Zhi, Tristan Laidlow, Stefan Leutenegger, Andrew J. Davison*  
  **[` 2021`] (``)**

Compositional pattern producing networks: A novel abstraction of development

An intriguing failing of convolutional neural networks and the coordconv solution

Pix2pose: Pixel-wise coordinate regression of objects for 6d pose estimation

Hybridpose: 6d object pose estimation under hybrid representations

Solov2: Dynamic, faster and stronger

Location augmentation for cnn



Nerf:Representing scenes as neural radiance fields for view synthesis

Differentiable volumetric rendering: Learningimplicit 3d representations without 3d supervision

Scene representation networks: Continuous 3dstructure-aware neural scene representations.

Multiview neuralsurface reconstruction by disentangling geometry and appearance



[Adversarial Generation of Continuous Images](https://arxiv.org/abs/2011.12026)  
*Ivan Skorokhodov, Savva Ignatyev, Mohamed Elhoseiny*  
**[`CVPR 2021`] (``)** 



Learning implicit fields for generative shape modeling

Deep meta functionals for shape representation



[CoordX: Accelerating Implicit Neural Representation with a Split MLP Architecture](https://arxiv.org/abs/2201.12425)  
*Ruofan Liang, Hongyi Sun, Nandita Vijaykumar*  
**[`ICLR 2022`] (``)**





[^ 1]: INR-GAN