# Evaluation

一些个重建loss等



### Reconstruction error 

- pSNR

$$
\operatorname{pSNR}(I, R)=-20 \log _{10} \frac{\operatorname{MAX}(I)}{\sqrt{\operatorname{MSE}(I, R)}}
$$

where MAX corresponds to the maximal value the image I can attain, and MSE is the Mean Squared Error.















Patch-Wise Minimal Pixels

Let an image $I \in \mathbb{R}^{m \times n \times c}$ be divided into $P$ non-overlapped patches with a patch size of $r \times r$, for with $P=\left\lceil\frac{m}{r}\right\rceil \cdot\left[\frac{n}{r}\right]$.
$$
\mathcal{P}(I)(i)=\min _{(x, y) \in \Omega_{i}}\left(\min _{c \in\{r, g, b\}} I(x, y, c)\right)
$$




Perceptual similarity metrics

[Generating images with perceptual similarity metrics based on deep networks](https://arxiv.org/pdf/1602.02644.pdf)  









## perceptual similarity distances

related papers:

`citation 4258` Perceptual losses for real-time style transfer and super-resolution

`citation 2431` Image Style Transfer Using Convolutional Neural Networks

`citation 698` Generating images with perceptual similarity metrics based on deep networks

