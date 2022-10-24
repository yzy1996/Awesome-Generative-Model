评价指标是两个，一个是质量，一个是多样性。

质量好意味着生成的数据和原数据像；多样性强意味着生成的数据种类多，不是只生成了一类图片。





因为我们是根据真实数据生成的样本，而原数据是带有类别标签的，所以我们可以通过新生成的数据是否能被很好的判断出类别，来衡量生成数据的质量。



对于一个新生成的样本，我们可以获得预测某一标签的概率 $p(y|x=G(z))$  

我们希望这个概率尽可能大，更好预测，熵更低



同时，我们可以获得类别的边际概率，$P(y) = \int_{z} p(y \mid x=G(z)) d z$

我们希望这个概率尽可能服从均匀分布，即生成的每个类别数量都差不多



因此我们写出了IS标准


$$
\operatorname{IS}(G)=\exp \left(\mathbb{E}_{\mathbf{x} \sim p_{g}} D_{K L}(p(y \mid \mathbf{x}) \| p(y))\right)
$$
关于KL散度，参考：





这个方法的缺点是：





## Fréchet Inception Distance (FID)

前面方法是预测出结果了再比较

现在我们直接在一层网络上做文章



我们使用一个多元高斯分布来建模特征，就分别有均值 $\mu$ 和协方差 $\Sigma$ 
$$
\operatorname{FID}(x, g)=\left\|\mu_{x}-\mu_{g}\right\|_{2}^{2}+\operatorname{Tr}\left(\Sigma_{x}+\Sigma_{g}-2\left(\Sigma_{x} \Sigma_{g}\right)^{\frac{1}{2}}\right)
$$




越低越好



对模式崩塌很敏感





LPIPS distance

