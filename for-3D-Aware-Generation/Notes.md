# <p align=center>`3D Understanding`</p>

> 我们总希望机器能做到人能做到的事情，甚至要比人做得更好。



[RGBD-GAN](#RGBD-GAN)

---

<span id="RGBD-GAN"></span>
[RGBD-GAN: Unsupervised 3D Representation Learning From Natural Image Datasets via RGBD Image Synthesis](https://arxiv.org/pdf/1909.12573.pdf)  
**[`ICLR 2020`] (`U Tokyo, RIKEN`)**  
*Atsuhiro Noguchi, Tatsuya Harada*

<details><summary>Click to expand</summary>

<div align=center><img width="500" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210709115756.png"/></div>

> **Summary**

They hope to understand **3D geometries** from 2D images by disentangling **object identity** (shape and texture) and **camera pose** (camera rotation, translation, and intrinsics). 

> **Details**

$T(x)$ donates a stochastic data augmentation function. $D(x)$ donates the last layer before the activation function. The proposed regularization is given by:

</details>

---

[Do 2D GANs Know 3D Shape? Unsupervised 3D shape reconstruction from 2D Image GANs](https://arxiv.org/pdf/2011.00844.pdf)  
**[`ICLR 2021`] (`CUHK, NTU`)**  
*Xingang Pan, Bo Dai, Ziwei Liu, Chen Change Loy, Ping Luo*

<details><summary>Click to expand</summary><p>

ss

> **Summary**

重点是弄清楚 project 是如何做到的

</p></details>

---

[Image GANs meet Differentiable Rendering for Inverse Graphics and Interpretable 3D Neural Rendering](https://arxiv.org/pdf/2010.09125.pdf)  
**[`ICLR 2021`] (`NVIDIA, Toronto`)**  
*Yuxuan Zhang, Wenzheng Chen, Huan Ling, Jun Gao, Yinan Zhang, Antonio Torralba, Sanja Fidler*







### BlockGAN

[BlockGAN: Learning 3D Object-aware Scene Representations from Unlabelled Images](https://arxiv.org/abs/2002.08988)

**`[NeurIPS 2020]`**	**`(Adobe)`**	**`[Thu Nguyen-Phuoc, Christian Richardt]`**	**[[Paper](https://github.com/thunguyenphuoc/BlockGAN)]**

<details><summary>Click to expand</summary>

<div align=center><img width="600" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201214151442.png"/></div>

> **Summary**

learns 3D object-oriented scene representations directly from unlabeled 2D images

> **Method**

divide an 3D feature into background and foreground

a noise vector $\mathbb{z}_i$ and the object's 3D pose $\theta_i = (s_i, \mathbf{R}_i, \mathbf{t}_i)$

3D feature $O_i = g_i(\mathbb{z}_i, \theta_i)$
$$
\mathbf{x}=p\left(f(\underbrace{O_{0},}_{\text {background }} \underbrace{O_{1}, \ldots, O_{K}}_{\text {foreground }})\right)
$$

</details>

---
