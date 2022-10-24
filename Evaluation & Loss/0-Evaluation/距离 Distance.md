[toc]



# 距离 Distance

收集整理多种刻距离，用来刻画概率等



## 欧氏空间



### 棋盘距离

$$
|x_1 - x_2| + |y_1 - y_2|
$$

### 城市街区距离

$$
\max(|x_1 - x_2|, |y_1 - y_2|)
$$





## 两分布之间

### DL 



### JS



### W



### Hausdorff distance

$$
d_{\mathrm{HD}}\left(S_{1}, S_{2}\right)=\max \left\{\max _{x_{i} \in S_{1}} \min _{y_{j} \in S_{2}}\left\|x_{i}-y_{j}\right\| \max _{y_{j} \in S_{2}} \min _{x_{i} \in S_{1}}\left\|x_{i}-y_{j}\right\|\right\}
$$



- not robust to outliers

### 倒角距离 Chamfer Distance

> The Chamfer distance is a sum of positive distances and is defined for unsigned distance functions. In the case of two-dimensional template matching using Chamfer distance, the reference image and the template are both binary edge images which can be obtained using an edge filter on the original images.

2D
$$
D_{chamfer}(T, I) \equiv \frac{1}{|T|} \sum_{t \in T} d_{I}(t)
$$
where $T$ is the set of points on template, $I$ is the  set of points in image, $d_I(t)$ is the minimum distance between point $t$ and some point in $I$.

3D
$$
d_{\mathrm{CD}}\left(S_{1}, S_{2}\right)=\frac{1}{S_{1}} \sum_{x \in S_{1}} \min _{y \in S_{2}}\|x-y\|_{2}^{2}+\frac{1}{S_{2}} \sum_{y \in S_{2}} \min _{x \in S_{1}}\|y-x\|_{2}^{2}
$$




### Earth Mover's distance

$$
d_{E M D}\left(S_{1}, S_{2}\right)=\min _{\phi: S_{1} \rightarrow S_{2}} \sum_{x \in S_{1}}\|x-\phi(x)\|_{2}
$$

where $\phi: S_{1} \rightarrow S_{2}$ is a bijection



### Chamfer Distance

