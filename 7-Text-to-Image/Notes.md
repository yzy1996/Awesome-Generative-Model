# <p align=center>`Text-to-Image` </p>



## Introduction





## Literature





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

