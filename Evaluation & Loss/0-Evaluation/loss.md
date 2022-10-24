

pixel similarity loss

> (pixel space) pixel-wise loss: L1 L2



**Sinkhorn distance**

Sinkhorn's matrix scaling algorithm



Chamfer Distance CD or 
$$
d_{C D}\left(S_{1}, S_{2}\right)=\sum_{x \in S_{1}} \min _{y \in S_{2}}\|x-y\|_{2}+\sum_{x \in S_{2}} \min _{y \in S_{1}}\|x-y\|_{2}
$$


Earth Mover’s distance EMD: 
$$
d_{E M D}\left(S_{1}, S_{2}\right)=\min _{\phi: S_{1} \rightarrow S_{2}} \sum_{x \in S_{1}}\|x-\phi(x)\|_{2}^{2}
$$




如何去约束结果的几何一致性

follow RGBD-GAN





It's a key problem in statistical machine learning to choose a suitable distance to compare probabilities.

- Hellinger
- $\chi_{2}$
- total variation
- Kullback-Leibler divergences
- earth mover’s (EMD)









