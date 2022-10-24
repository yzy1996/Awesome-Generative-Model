# Loss function of GANs



## Notation

|   symbol    |        mean        |
| :---------: | :----------------: |
|     $x$     |    real sample     |
| $\tilde{x}$ |    fake sample     |
|  $\hat{x}$  | interpolate sample |
|    $p_r$    | real distribution  |
|    $p_g$    | fake distribution  |



## Summary

A generalized form:
$$
\min_G \max_D V(G, D) = \mathbb{E}_{x \sim p_r}[f(D(x))] + \mathbb{E}_{\tilde{x} \sim p_g}[f(-D(\tilde{x}))]
$$
Vanilla GAN: $f(x) = -\log(1+\exp(-x))$

> 因为 Vanilla GAN 的 D 最后是有一个 sigmoid 的，所以上式其实是 $\log(\text{sigmoid})$ 的结果，同时 $\text{sigmoid}(-x) = 1-\text{sigmoid}(x)$，所以上式完美还原了。

WGAN: $f(x) = x$



> minimize*

|         Name          |                        Loss Function                         |
| :-------------------: | :----------------------------------------------------------: |
|    **Minimax GAN**    | $$\begin{aligned}&\mathcal{L}_D^{MMGAN} = -\mathbb{E}_{x \sim p_r} [\log (D(x))] - \mathbb{E}_{\tilde{x} \sim p_g} [\log (1-D(\tilde{x})] \\&\mathcal{L}_G^{MMGAN} = \mathbb{E}_{\tilde{x} \sim p_g} [\log (1 - D(\tilde{x}))]\end{aligned}$$ |
| **Non-Saturated GAN** | $$\begin{aligned}&\mathcal{L}_D^{NSGAN} = -\mathbb{E}_{x \sim p_r} [\log (D(x))] - \mathbb{E}_{\tilde{x} \sim p_g} [\log (1 - D(\tilde{x})] \\ &\mathcal{L}_G^{NSGAN} = -\mathbb{E}_{\tilde{x} \sim p_g} [\log (D(\tilde{x}))]\end{aligned}$$ |
|       **LSGAN**       | $$\begin{aligned}&\mathcal{L}_D^{LSGAN} = -\mathbb{E}_{x \sim p_r} [(D(x)-1)^2] + \mathbb{E}_{\tilde{x} \sim p_g} [D(\tilde{x})^2] \\&\mathcal{L}_G^{LSGAN} = -\mathbb{E}_{\tilde{x} \sim p_g} [(D(\tilde{x})-1)^2]\end{aligned}$$ |
|       **WGAN**        | $$\begin{aligned}&\mathcal{L}_{D}^{WGAN}=-\mathbb{E}_{x \sim p_r}[D(x)]+\mathbb{E}_{\tilde{x} \sim p_g}[D(\tilde{x})]\\&\mathcal{L}_{G}^{WGAN}=-\mathbb{E}_{\tilde{x} \sim p_g}[D(\tilde{x})]\\&W_D \leftarrow \text{clip\_by\_value}(W_D, -0.01, 0.01) \end{aligned}$$ |
|      **WGAN-GP**      | $$\begin{aligned}&\mathcal{L}_{D}^{WGAN-GP}=L_{D}^{WGAN} + \lambda {\mathbb{E}}_{\hat{x} \sim p_{\hat{x}}}\left[\left(\left\|\nabla_{\hat{x}} D(\hat{x})\right\|_{2}-1\right)^{2}\right] \\ &\mathcal{L}_{G}^{WGAN-GP}=L_{G}^{WGAN} \\ &\hat{x} = \alpha x + (1-\alpha) \tilde{x}\end{aligned}$$ |
|      **DRAGAN**       | $$\begin{aligned}&\mathcal{L}_{D}^{DRAGAN}=L_{D}^{GAN} + \lambda {\mathbb{E}}_{\tilde{x} \sim p_r+\mathcal{N}(0, c)}\left[\left(\left\|\nabla_{\hat{x}} D(\tilde{x})\right\|_{2}-1\right)^{2}\right] \\ &\mathcal{L}_{G}^{DRAGAN}=L_{G}^{GAN}\end{aligned}$$ |
|   **Geometric GAN**   | $$\begin{aligned}&\mathcal{L}_D^{GGAN} = \mathbb{E}_{x \sim p_r} [\max(0, 1-D(x))] + \mathbb{E}_{\tilde{x} \sim p_g} [\max(0, 1+D(\tilde{x}))] \\ &\mathcal{L}_G^{GGAN} = -\mathbb{E}_{\tilde{x} \sim p_g} [D(\tilde{x})]\end{aligned}$$ |



但是在具体实现的时候，我们经常用的是（针对不同任务会去尝试的）


## Details

### Vanilla GAN

$$
\min _{G} \max _{D} V(G, D)=\min _{G} \max _{D} \mathbb{E}_{x \sim p_r}[\log D(x)]+\mathbb{E}_{\tilde{x} \sim p_g}[\log (1-D(\tilde{x}))]
$$

原始GAN中的G_loss有两种形式

一种被称为 `saturating GAN loss` 
$$
\begin{aligned}
&\min_D \mathcal{L}(D) = -\mathbb{E}_{x \sim p_r} [\log D(x)] - \mathbb{E}_{\tilde{x} \sim p_g} [\log (1-D(\tilde{x}))] \\
&\min_G \mathcal{L}(G) = \mathbb{E}_{\tilde{x} \sim p_g} [\log (1 - D(\tilde{x}))]
\end{aligned}
$$
另一种被称为 `non-saturating GAN loss` 
$$
\begin{aligned}
&\min_D \mathcal{L}(D) = -\mathbb{E}_{x \sim p_r} [\log D(x)] - \mathbb{E}_{\tilde{x} \sim p_g} [\log (1-D(\tilde{x}))] \\
&\min_G \mathcal{L}(G) = -\mathbb{E}_{\tilde{x} \sim p_g} [\log D(\tilde{x})]
\end{aligned}
$$
两者的区别：在训练初期，判别器D很容易给 $\tilde{x}$ 打低分，饱和loss在低分区梯度较小，容易出现梯度消失的情况，而非饱和loss恰好相反。见下图，出自NIPS 2016 tutorial

<img src="https://raw.githubusercontent.com/yzy1996/Image-Hosting/master/20210330104532.png" alt="image-20210330104531371" style="zoom:50%;" />

### LSGAN



### Geometric GAN

又叫 Hinge loss:  $f(x) = \max(0, 1-tx)$，其中 $t$ 是真实标签，

[Geometric GAN](https://arxiv.org/abs/1705.02894)	[`arxiv2017`]	[`Jae Hyun Lim`, `Jong Chul Ye`]
$$
\begin{aligned}
&\min_D \mathcal{L}(D) = \mathbb{E}_{x \sim p_r} [\max(0, 1-D(x))] + \mathbb{E}_{\tilde{x} \sim p_g} [\max(0, 1+D(\tilde{x}))] \\
&\min_G \mathcal{L}(G) = -\mathbb{E}_{\tilde{x} \sim p_g} [D(\tilde{x})]
\end{aligned}
$$
在实现的时候，可以直接用 `ReLU` 函数去激活

```
dloss = (F.relu(1 - d_real) + F.relu(1 + d_fake)).mean()
gloss = -d_fake.mean()
```

>ReLU：$f(x) = \max(0, x)$



还有一种写法变形，其实是一模一样的，但我觉得不好，因为没有ReLU的直接。
$$
\begin{aligned}
&\min_D \mathcal{L}(D) = -\mathbb{E}_{x \sim p_r} [\min(0, -1+D(x))] - \mathbb{E}_{\tilde{x} \sim p_g} [\min(0, -1-D(\tilde{x}))] \\
&\min_G \mathcal{L}(G) = -\mathbb{E}_{\tilde{x} \sim p_g} [D(\tilde{x})]
\end{aligned}
$$






## 其他 trick

通常我们是希望判别器给真样本打高分，给假样本打低分



但也可以反过来，这样的好处

-1 real 1 fake



