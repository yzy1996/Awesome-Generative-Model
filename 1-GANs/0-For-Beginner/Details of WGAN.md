参考：https://medium.com/@jonathan_hui/gan-wasserstein-gan-wgan-gp-6a1a2aa1b490





# WGAN

Instead of using a discriminator to classify or predict the probability of generated images as being real or fake, the WGAN changes or replaces the discriminator model with a critic that scores the realness or fakeness of a given image.



The differences in implementation for the WGAN are as follows:

1. Use a linear activation function in the output layer of the critic model (instead of sigmoid).
2. Use -1 labels for real images and 1 labels for fake images (instead of 1 and 0).
3. Use Wasserstein loss to train the critic and generator models.
4. Constrain critic model weights to a limited range after each mini batch update (e.g. [-0.01,0.01]).
5. Update the critic model more times than the generator each iteration (e.g. 5).
6. Use the RMSProp version of gradient descent with a small learning rate and no momentum (e.g. 0.00005).



critic model

> 输入28*28 image，输出[-1,1] score





DCGAN设计最好的是使用**LeakyReLU activation function** with a **slope of 0.2**, **batch normalization**, and using a **2×2 stride** to downsample.





# Earth-Mover (EM) distance/ Wasserstein Metric





WGAN提出用 Wasserstein 距离取代之前的KL和JS散度
$$
W\left(P_{r}, P_{g}\right)=\inf _{\gamma \sim \prod\left(P_{r}, P_{g}\right)} \mathbb{E}_{(x, y) \sim \gamma}\|x-y\|
$$
其中 $P_r, P_g$ 分别为真实数据和生成的数据的分布函数，Wasserstein 距离衡量了这两个分布函数的差异性。直观地理解，就是根据这两个分布函数分别生成一堆数据 $x_1, x_2, \dots, x_n$ 和另一堆数据 $y_1, y_2, \dots, y_n$，然后计算这两堆数据之间的距离。距离的算法是找到一种一一对应的配对方案$\gamma \sim \prod\left(P_{r}, P_{g}\right)$ ，把 $x_i$ 移动到 $y_i$ ，求总移动距离的最小值。由于在 GAN 中， $P_r$ 和 $P_g$  都没有显式的表达式，只能是从里面不停地采样，所以不可能找到这样的 $\gamma$，无法直接优化公式 (2) 。所以作者根据 Kantorovich-Rubinstein duality，将公式 (2) 转化成公式 (3)，过程[详见](https://vincentherrmann.github.io/blog/wasserstein/)
$$
W\left(P_{r}, P_{g}\right)=\sup _{\|f\|_{L} \leq 1} \mathbb{E}_{x \sim P_{r}}[f(x)]-\mathbb{E}_{y \sim P_{g}}[f(y)]
$$
其中 $f$ 为判别器函数，只有当判别器函数满足 1-Lipschitz 约束时，(2) 才能转化为 (3)。除此之外，正如上文所说，Lipschitz continuous 的函数的梯度上界被限制，因此函数更平滑，在神经网络的优化过程中，参数变化也会更稳定，不容易出现梯度爆炸，因此Lipschitz continuity 是一个很好的性质。

为了让判别器函数满足 1-Lipschitz continuity，WGAN 和之后的 WGAN-GP 分别采用了 weight-clipping 和 gradient penalty 来约束判别器参数。





