[without Notes](./README.md) | with Notes

# <p align=center>`CLIP` </p>



## Introduction

[Contrastive Language-Image Pre-training (CLIP)](https://distill.pub/2021/multimodal-neurons/) was trained on 400 million text-images pairs, collected from a variety of publicly available sources on the Internet. 



## Literature



### CLIP + GAN

[(StyleCLIP)-Text-Driven Manipulation of StyleGAN Imagery](https://arxiv.org/pdf/2103.17249.pdf)  
**[`Arxiv 2021`] (`TAU`)** *Or Patashnik, Zongze Wu, Eli Shechtman, Daniel Cohen-Or, Dani Lischinski*

<details><summary>Click to expand</summary>

> **Summary**

<div align="center">
<img src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210504143826.png" width="600"/>
</div>

They combine the generative power of **StyleGAN** with the rich joint vision-language representation learned by **CLIP**. They leverage these tech to develop a text-based interface for manipulating generated and real images that does not require manual effort (manual annotation). Their method mainly control the **latent spaces** of StyleGAN. 


> **Details**

They explore three ways for text-driven image manipulation:

- latent optimization (a given latent code of an image is optimized by minimizing a loss computed in CLIP space).
  $$
  \underset{w \in \mathcal{W}+}{\arg \min } D_{\mathrm{CLIP}}(G(w), t)+\lambda_{\mathrm{L} 2}\left\|w-w_{s}\right\|_{2}+\lambda_{\mathrm{ID}} \mathcal{L}_{\mathrm{ID}}(w)
  $$

- latent mapper (mapping network is trained to infer a manipulation step in latent space).

- global direction (transforms a given text prompt into an input agnostic mapping direction).

</details>

---

### CLIP + NeRF

[(DietNeRF)-Putting NeRF on a Diet Semantically Consistent Few-Shot View Synthesis](https://arxiv.org/pdf/2104.00677.pdf)  
**[`Arxiv 2021`] (`UCB`)** *Ajay Jain, Matthew Tancik, Pieter Abbeel*

<details><summary>Click to expand</summary>

> **Summary**

- **Task:** render a scene from novel poses given just a few photos.
- [Neural Radiance Fields (NeRF)](https://www.matthewtancik.com/nerf) generate crisp renderings with 20-100 photos, but overfit with only a few.
- **Problem:** NeRF is only trained to render observed poses, leading to artifacts when few are available.
- **Key insight:** Scenes share high-level semantic properties across viewpoints, and pre-trained 2D visual encoders can extract these semantics. *"An X is an X from any viewpoint."*
- Our proposed DietNeRF supervises NeRF from *arbitrary* poses by ensuring renderings have consistent high-level semantics using the CLIP Vision Transformer.
- We generate plausible novel views given 1-8 views of a test scene.

> **Details**



</details>

---

