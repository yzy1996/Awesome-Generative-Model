# High Quality GAN



## Introduction



Progressive-GAN is the **first** GAN that can generate realistic human faces at a high resolution of $$1024 \times 1024$$.









## Bibliography

[2018 PGGAN](#PGGAN)

[2019 BigGAN](#BigGAN)

[2019 StyleGAN](#StyleGAN)

---

### PGGAN

[Progressive growing of GANs for improved quality, stability, and variation](http://arxiv.org/pdf/1710.10196.pdf)

**[`ICLR 2018`]**	**(`NVIDIA`)**	**[[Code-Tensorflow](https://github.com/tkarras/progressive_growing_of_gans)]**	**[[Code-Pytorch](https://github.com/ptrblck/prog_gans_pytorch_inference)]**	**[[Code-Pytorch](https://github.com/nashory/pggan-pytorch)]**

**[`Tero Karras`, `Timo Aila`, `Samuli Laine`, `Jaakko Lehtinen`]**

<details><summary>Click to expand</summary><p>


> **Summary**

</p></details>

---

### BigGAN

[Large Scale GAN Training for High Fidelity Natural Image Synthesis](https://arxiv.org/abs/1809.11096)

**[`ICLR 2019`]**	**(`DeepMind`)**	**[[Code](https://github.com/ajbrock/BigGAN-PyTorch)]**

<details><summary>Click to expand</summary><p>


> **Details**

the intermediate layers take the latent vector as input:
$$
\mathbf{y}_{i}=G_{i}\left(\mathbf{y}_{i-1}, \mathbf{z}\right)
$$
which is called Skip-z inputs



Skip-z inputs

</p></details>

---

### StyleGAN

[A Style-Based Generator Architecture for Generative Adversarial Networks]()

**[`CVPR 2019`]**	**(`NVIDIA`)**	**[[Code](https://github.com/NVlabs/stylegan)]**

**`[Tero Karras, Samuli Laine]`**		

<details><summary>Click to expand</summary><p>


![image-20201031134802945](https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201031134812.png)

**need to know**:

- [ ] (AdaIN) adaptive instance normalization operation after each convolution layer

**summary**:

do not provide input layer with a latent code $z$, start from a learned constant and map $z$ to a intermediate latent space $w$, donated by $f: \mathcal{Z} \rightarrow \mathcal{W}$, where $f$ is an MLP.

> The intermediate latent space is much less entangled than the input latent space.

</p></details>

---