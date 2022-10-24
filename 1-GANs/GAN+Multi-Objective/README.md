# Multi-Objective GAN

We can construct a framework of Multi-Objective GAN with:
$$
\min \mathcal{L}_{G}(\mathbf{x})=\left[L_{1}(\mathbf{z}), L_{2}(\mathbf{z}), \ldots, L_{K}(\mathbf{z})\right]^{T}
$$
where each $L_{k}=-\mathbb{E}_{z \sim p_{z}} \log D_{k}(G(z))$ , $k \in {1, \dots, K}$



**Previous works were done around multiple discriminators including** 

[Durugkar, 2016, Generative multi-adversarial networks](./Literature/2016_Generative-Multi-Adversarial-Networks.pdf)

> The goal of using the proposed methods is to favor worse discriminators, thus providing more useful gradients to the generator during training.
>
> Using a softmax weighted average of K discriminators, 
> $$
> \mathcal{L}_{D_{k}}=-\mathbb{E}_{\mathbf{x} \sim p_{\text {data }}} \log D_{k}(\mathbf{x})-\mathbb{E}_{\mathbf{z} \sim p_{z}} \log \left(1-D_{k}(G(\mathbf{z}))\right)
> $$
> $$
> \mathcal{L}_{G}=\sum_{k=1}^{K} \alpha_{k} \mathcal{L}_{D_{k}}
> $$
> $$
> \alpha_k = \text{softmax}(l_{1:K})_k = \frac{e^{\beta l_k}}{\sum_{i=1}^K e^{\beta l_i}}
> $$
> $\beta$ is a hyperparameter, ($\beta$=0, 1 , $\infty$)
>

[Neyshabur, 2017, Stabilizing GAN Training with Multiple Random Projections](./Literature/2017_Stabilizing-GAN-Training-with-Multiple-Random-Projections.pdf)

> using average loss minimization
> 
> $$
> \mathcal{L}_{D_{k}}=-\mathbb{E}_{\mathbf{x} \sim p_{\text {data }}} \log D_{k}(\mathbf{x})-\mathbb{E}_{\mathbf{z} \sim p_{z}} \log \left(1-D_{k}(G(\mathbf{z}))\right)
> $$
> $$
> \mathcal{L}_{G}=-\sum_{k=1}^{K} \mathbb{E}_{\mathbf{z} \sim p_{z}} \log D_{k}(G(\mathbf{z}))
> $$
>
> $$
> \alpha_k = \frac{1}{K}
> $$

[Albuquerque, 2019, Multi-objective training of Generative Adversarial Networks with multiple
discriminators](./Literature/2019_Multi-objective-training-of-generative-adversarial-networks-with-multiple-discrimi.pdf)

> using hypervolume maximization
> $$
> \mathcal{L}_{G}=-\mathcal{V}=-\sum_{k=1}^{K} \log \left(\eta-l_{k}\right)
> $$
>
> $$
> \alpha_{k}=\frac{1}{T\left(\eta-l_{k}\right)}
> $$
>
> $$
> T=\sum_{k=1}^{K} \frac{1}{\eta-l_{k}}
> $$
>
> 



**These all methods consist two steps**:

- Step 1 - consolidate all gradients into a single update parameters in the direction(compute the set $\alpha_1, \dots, \alpha_K$)
- Step 2 - update parameters in the direction returned in Step 1