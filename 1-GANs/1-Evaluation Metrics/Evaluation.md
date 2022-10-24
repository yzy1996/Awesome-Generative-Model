## Manual GAN Evaluation

*Visual examination of samples by humans is one of the common and most intuitive ways to evaluate GANs.   -- Pros and Cons of GAN Evaluation Measures, 2018*



## Qualitative GAN Evaluation

1. Nearest Neighbors.
2. Rapid Scene Categorization.
3. Rating and Preference Judgment.
4. Evaluating Mode Drop and Mode Collapse.
5. Investigating and Visualizing the Internals of Networks.



### Rapid Scene Categorization

Images are presented to human judges for a very limited amount of time (e.g a second)

Images are often presented in pairs and the human judge is asked which image they prefer



## Quantitative GAN Evaluation

1. Average Log-likelihood
2. Inception Score (IS)
3. **Frechet Inception Distance (FID)**
4. Maximum Mean Discrepancy (MMD)



### Inception Score

proposed by [1]. 

Using a pre-trained model (**Inception v3**) to classify the generated images as one of 1000 known objects.

The classification results could both capture how much generated image looks like a known class and how diverse the set of images are across the known classes.

A higher IS indicates better-quality generated images.

The scores combine both the confidence of the conditional class predictions for each synthetic image (quality) and the integral of the marginal probability of the predicted classes (diversity).

The calculation of the inception score on a group of images involves first using the inception v3 model to calculate the conditional probability for each image (p(y|x)). The marginal probability is then calculated as the average of the conditional probabilities for the images in the group (p(y)).

The KL divergence is then calculated for each image as the conditional probability multiplied by the log of the conditional probability minus the log of the marginal probability.
$$
kl =
$$

The problem of IS is that it does not capture how synthetic images compare to real images.


$$
\mathrm{IS}=\exp \left(\mathbb{E}_{x \sim p_{g}} D_{K L}(p(y \mid x) \| p(y))\right)
$$



$$
D_{KL}(P\|Q) = -\sum_i P(i) \ln \frac{Q(i)}{P(i)} 
$$



### Frechet Inception Distance (FID)

The Fréchet distance between two multivariate Gaussians $X_1 \sim N(\mu_1, \sigma_1)$ and $X_2 \sim N(\mu_2, \sigma_2)$ is:
$$
d^2 = ||\mu_1 - \mu_2||^2 + \Tr(\sigma_1 + \sigma_2 - 2\sqrt{\sigma_1\sigma_2}).
$$

> sample 数量应该比网络层的维度大，Inception pool_3 的维度是 2048，所以应该大于 2048，一般推荐用大于 10,000 个样本。（原因是计算协方差矩阵至少得填满才能算平方根）



proposed by [2].

It's an improvement over the existing Inception Score. 

*FID performs well in terms of discriminability, robustness and computational efficiency.  -- Pros and Cons of GAN Evaluation Measures, 2018*

用 inception v3 最后一层

The activations for each real and generated image are summarized as a multivariate Gaussian by calculating the mean and covariance of the images. These statistics are then calculated for the activations across the collection of real and generated images. The distance between these two distributions is then calculated using the Frechet distance, also called the Wasserstein-2 distance.

A lower FID score indicates more realistic images that match the statistical properties of real images.



[GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium](https://arxiv.org/pdf/1706.08500.pdf)  
**[`NeurIPS 2017`] (`LIT AI Lab`)** [[Tensorflow](https://github.com/bioinf-jku/TTUR)] [[Pytorch](https://github.com/mseitzer/pytorch-fid)] 
*Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter*



Pytorch pip Usage

```python
pip install pytorch-fid

python -m pytorch_fid path/to/dataset1 path/to/dataset2
```





## Reference

[1] Improved Techniques for Training GANs, 2016

[2] GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium, 2017

[3] Pros and Cons of GAN Evaluation Measures, 2018

[4] An empirical study on evaluation metrics of generative adversarial networks, 2018







interpolation quality and disentanglement





https://github.com/GaParmar/clean-fid
