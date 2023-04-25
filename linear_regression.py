import torch
import matplotlib.pyplot as plt

if __name__ == '__main__':
    torch.manual_seed(10) # 设置CPU生成随机数的种子，方便下次复现实验结果。

    x = torch.rand(size=(20,1)) * 10
    y = 2*x + torch.randn(size=(20,1)) 
    
    # 初始化参数
    w = torch.randn((1), requires_grad=True)
    b = torch.zeros((1), requires_grad=True)

    lr = 0.05

    for iteration in range(100):
        # 前向传播 y = wx + b
        wx = torch.mul(input=w,other=x)
        y_pred = torch.add(input=wx,other=b)

        # 均方损失函数
        loss = (0.5 * (y-y_pred)**2).mean()

        # 反向传播
        loss.backward()

        # 更新参数
        b.data.sub_(other=lr*b.grad)
        w.data.sub_(other=lr*w.grad)

        # 清除tensor的梯度
        w.grad.data.zero_()
        b.grad.data.zero_()

        print(loss.data)
    print(w.data)
    print(b.data)




