**Task1: Generate multi-view images from a single-view input**



**impact**

> broad applications in vision, graphics, and robotics



**related work**

> model-driven synthesis: 
>
> data-driven generation: [^Zhu et al., 2014]
>
> combination of the both [^Peng et al., 2017]
>
> GAN: [^Tran et al., 2017] [^Zhao et al., 2017]



**GAN pipeline in this problem**

```mermaid
graph LR
    A(input image) --> B(Encoder) --> C(latent code) --> D(Decoder) --> E(output image)
    F(Discriminator) --> B
    F --> D
    
```





disentangle pose and identity factors by cross-reconstruction [^Peng et al., 2017][^Zhu et al., 2014]





[^Peng et al., 2017]:Reconstruction-based disentanglement for pose-invariant face recognition
[^Zhu et al., 2014]:Multi-view perceptron: a deep model for learning face identity and view representations
[^Tran et al., 2017]:Disentangled Representation Learning GAN for Pose-Invariant Face Recognition
[^Zhao et al., 2017]: Multi-view image generation from a single-view





## CR-GAN

[CR-GAN: Learning Complete Representations for Multi-view Generation]()

**`[IJCAI 2018]`**	**`(Rutgers University)`**	**`[Yu Tian, Xi Peng]`**	**([:memo:]())**	**[[:octocat:](https://github.com/bluer555/CR-GAN)]**

<details><summary>Click to expand</summary><p>


<div align=center><img width="800" src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20201209160238.png" /></div>

> **Keywords**

Two-pathway



> **Novelty**

maintain the completeness of the learned embedding space.



> **Pipeline**

The generator![](https://latex.codecogs.com/svg.latex?%5Cinline%20G) produces a synthesis image  with a random noise![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{z}) under a view label![](https://latex.codecogs.com/svg.latex?%5Cinline%20v).

The discriminator![](https://latex.codecogs.com/svg.latex?%5Cinline%20D) contains two parts![](https://latex.codecogs.com/svg.latex?%5Cinline%20(D_s, D_v)).![](https://latex.codecogs.com/svg.latex?%5Cinline%20D_s) estimates the image quality, i.e., how real the image is,![](https://latex.codecogs.com/svg.latex?%5Cinline%20D_v) predict the view of given image.



The encoder![](https://latex.codecogs.com/svg.latex?%5Cinline%20E) reconstructs a latent vector![](https://latex.codecogs.com/svg.latex?%5Cinline%20\bar{\boldsymbol{z}}) from an image, in other words,![](https://latex.codecogs.com/svg.latex?%5Cinline%20E) will be learned as an inverse of![](https://latex.codecogs.com/svg.latex?%5Cinline%20G) and the latent space could represent the total image space.

In this problem, the output of![](https://latex.codecogs.com/svg.latex?%5Cinline%20E) should preserve the same identity and we hope![](https://latex.codecogs.com/svg.latex?%5Cinline%20E) could disentangle the viewpoint from the identity.

To be specific, we first sample a pair of real images![](https://latex.codecogs.com/svg.latex?%5Cinline%20(\boldsymbol{x}_{i}, \boldsymbol{x}_{j})) which are the same identity but different views![](https://latex.codecogs.com/svg.latex?%5Cinline%20v_i,v_j). The goal is to reconstruct![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{x}_j) from![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{x}_i). To achieve this,![](https://latex.codecogs.com/svg.latex?%5Cinline%20E) takes![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{x}_i) as an input and outputs an identity-preserved representation![](https://latex.codecogs.com/svg.latex?%5Cinline%20\bar{\boldsymbol{z}}) together with the view estimation![](https://latex.codecogs.com/svg.latex?%5Cinline%20\bar{\boldsymbol{v}}):![](https://latex.codecogs.com/svg.latex?%5Cinline%20(\bar{\boldsymbol{z}}, \bar{\boldsymbol{v}}) = E(\boldsymbol{x}_i)).![](https://latex.codecogs.com/svg.latex?%5Cinline%20G) takes![](https://latex.codecogs.com/svg.latex?%5Cinline%20\bar{\boldsymbol{z}}) and![](https://latex.codecogs.com/svg.latex?%5Cinline%20v_j) as input, then produce![](https://latex.codecogs.com/svg.latex?%5Cinline%20\tilde{\boldsymbol{x}}_{j}) which should be the reconstruction of![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{x}_{j}). 



在第一轮训练中，训练![](https://latex.codecogs.com/svg.latex?%5Cinline%20G) 和![](https://latex.codecogs.com/svg.latex?%5Cinline%20D)，![](https://latex.codecogs.com/svg.latex?%5Cinline%20G) 想尽可能生成与真图像的假图，![](https://latex.codecogs.com/svg.latex?%5Cinline%20D) 想尽可能分辨出真图和假图。 

![](https://latex.codecogs.com/svg.latex?%5Cinline%20\{D_s(\boldsymbol{x}), D_s(G(\boldsymbol{z}, v))\}) 和![](https://latex.codecogs.com/svg.latex?%5Cinline%20\{D_v(\boldsymbol{x}), v\}) 差距要尽可能小

> 只能同时识别身份和角度，建立的是真图和假图之间的关系，还缺乏同一身份不同角度真图或者假图之间的关系

在第二轮训练中，训练![](https://latex.codecogs.com/svg.latex?%5Cinline%20E) 和![](https://latex.codecogs.com/svg.latex?%5Cinline%20D)，希望弥补上面的缺陷，![](https://latex.codecogs.com/svg.latex?%5Cinline%20E) 想尽可能解码出身份信息和角度信息，所以只要解开了，![](https://latex.codecogs.com/svg.latex?%5Cinline%20G) 就能继续生成，但![](https://latex.codecogs.com/svg.latex?%5Cinline%20D) 需要重新训练别让把相同身份不同位置的



|                                                              |                                                              |      |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :--: |
| ![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{x}_i) | real image![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{x}) with view![](https://latex.codecogs.com/svg.latex?%5Cinline%20v_i) |      |
| ![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{x}_j) | real image![](https://latex.codecogs.com/svg.latex?%5Cinline%20\boldsymbol{x}) with view![](https://latex.codecogs.com/svg.latex?%5Cinline%20v_j) |      |
| ![](https://latex.codecogs.com/svg.latex?%5Cinline%20(\bar{\boldsymbol{z}}, \bar{\boldsymbol{v}}) = (E_{\boldsymbol{z}}(\boldsymbol{x}_i), E_v(\boldsymbol{x}_i) )) |                                                              |      |
| ![](https://latex.codecogs.com/svg.latex?%5Cinline%20\tilde{\boldsymbol{x}}_{j} = G(E_{\boldsymbol{z}}(\boldsymbol{x}_{i}),v_j)) |                          fake image                          |      |

- 





</p></details>

---



