# Few-Shot & Limited Data

> See latex/pdf version for better view of citations.

The success of GANs heavily relies on big data.

Reducing the amount of training data leads to the overfitting of the discriminator -> Mode Collapse



## Introduction

On the one hand, we can utilize **transfer learning** with a pre-trained model.

On the other hand, we can 

Dynamic data-augmentation

not only the real images from the dataset but also the synthesized images by the generator



internal issues is **the overfitting of the discriminator**





### Data Augmentation 

[Differentiable Augmentation for Data-Efficient GAN Training](https://arxiv.org/pdf/2006.10738.pdf)  
**[`NeurIPS 2020`] (`MIT`)**  
*Shengyu Zhao, Zhijian Liu, Ji Lin, Jun-Yan Zhu, Song Han*

[Training Generative Adversarial Networks with Limited Data](https://arxiv.org/pdf/2006.06676.pdf)  
**[`NeurIPS 2020`] (`NVIDIA`)**  
*Tero Karras, Timo Aila*

[On data augmentation for GAN training](https://arxiv.org/pdf/2006.05338.pdf)  
**[`TIP 2021`] (`SUTD`)**  
*Ngoc-Trung Tran, Viet-Hung Tran, Ngoc-Bao Nguyen, Trung-Kien Nguyen, Ngai-Man Cheung*

[Image augmentations for GAN training](https://arxiv.org/pdf/2006.02595.pdf)  
**[`Arxiv 2020`] (`UC Irvine, Google`)**  
*Zhengli Zhao, Zizhao Zhang, Ting Chen, Sameer Singh, Han Zhang*

[Progressive Augmentation of GANs](https://arxiv.org/pdf/1901.10422.pdf)  
**[`NeurIPS 2019`] (`Bosch`)**
*Dan Zhang, Anna Khoreva*







<span id="InsGen"></span>
[Data-Efficient Instance Generation from Instance Discrimination](https://arxiv.org/pdf/2106.04566.pdf)  
**[`NeurIPS 2021`] (`CUHK, Byte`)**  
*Ceyuan Yang, Yujun Shen, Yinghao Xu, Bolei Zhou*



## Literature

[fastgan](#fastgan)

[DiffAugment](#DiffAugment)

---

[Training Generative Adversarial Networks with Limited Data](https://arxiv.org/pdf/2006.06676.pdf)  
**[`NeurIPS 2020`] (`NVIDIA`)** [[:octocat:](https://github.com/NVlabs/stylegan2-ada)] (*Tero Karras, Timo Aila*)

<details><summary>Click to expand</summary><p>


**Summary**

> Training generative adversarial networks (GAN) using too little data typically leads to discriminator overfitting, causing training to diverge




</p></details>

---

<span id="DiffAugment"></span>
[Differentiable Augmentation for Data-Efficient GAN Training](https://arxiv.org/pdf/2006.10738.pdf)  
**[`NeurIPS 2020`]** **(`MIT`)** [[:octocat:](https://github.com/mit-han-lab/data-efficient-gans)] (*Shengyu Zhao, Zhijian Liu, Ji Lin, Jun-Yan Zhu, Song Han*)



---

<span id="Fastgan"></span>
[Towards Faster and Stabilized GAN Training for High-fidelity Few-shot Image Synthesis](https://arxiv.org/pdf/2101.04775.pdf)  
**[`ICLR 2021`]** **(`Rutgers`)** [[:octocat:](https://github.com/odegeasslbc/FastGAN-pytorch)] (*Bingchen Liu, Yizhe Zhu, Kunpeng Song, Ahmed Elgammal*)

<details><summary>Click to expand</summary><p>


**Summary**

> Use a skip-layer channel-wise excitation module and a self-supervised discriminator trained as a feature-encoder.

</p></details>

---





- [Diverse Generation from a Single Video Made Possible](https://arxiv.org/pdf/2109.08591.pdf)  
  *Niv Haim, Ben Feinstein, Niv Granot, Assaf Shocher, Shai Bagon, Tali Dekel, Michal Irani*  
  **[`Arxiv 2021`] (`Weizmann Institute of Science`)**

