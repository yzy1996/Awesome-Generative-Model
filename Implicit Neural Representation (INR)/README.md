# <p align=center>`Implicit Neural Representation` </p>

[Neural Implicit Representations for 3D Vision and Beyond by Dr. Andreas Geiger](https://www.youtube.com/watch?v=jennURL-gtQ)

https://github.com/vsitzmann/awesome-implicit-representations

## 1. Introduction

*The original idea of augmenting neural networks with coordinates information was proposed in CPPN. The largest popularity of INRs is observed in 3D deep lesrning, where it provides a cheap and continuous way to represent a 3D shape compared to mesh/voxel/pointcloud-based ones.*[^ 1] 



也可以叫 neural implicit function





几个经典网络：

- Occupancy Networks

  They model a probability function of a voxel being occupied by a 3D shape and typically employ a coordinate-based decoder that operates on top of single-view images. They also use the multi-resolution surface extraction method.

- DeepSDF 

  It models a signed distance function 



## 2. Research Branch/Direction

- Finding an efficient way to encode coordinates positions

Fourier features let networks learn high frequency functions in low dimensional domains

Implicit neural representations with periodic activation functions

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





Learning implicit fields for generative shape modeling

Deep meta functionals for shape representation



[^ 1]: INR-GAN