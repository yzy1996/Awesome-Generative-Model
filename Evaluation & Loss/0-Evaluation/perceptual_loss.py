__author__ = 'zhiyuan Yang'

import torch

# Calculate Gram matrix
def gram(x):
    (bs, ch, h, w) = x.size()
    f = x.view(bs, ch, w * h)
    f_T = f.transpose(1, 2)
    G = f.bmm(f_T) / (ch * h * w)
    return G


tensor1 = torch.randn(10, 3, 4)
tensor2 = torch.randn(10, 4, 5)

# using matmul
result1 = torch.matmul(tensor1, tensor2)


# using bmm
result2 = torch.bmm(tensor1, tensor2)

print(result1==result2)


def perceptual_loss():
