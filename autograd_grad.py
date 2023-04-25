import torch

if __name__ == '__main__':
    # 对y=x**2进行二阶梯度求导
    # x = torch.tensor(data=[3.],requires_grad=True)
    # y = torch.pow(input=x,exponent=2)

    # grad_1 = torch.autograd.grad(outputs=y,inputs=x,create_graph=True)
    # print(grad_1) # type(grad_1) is tuple 

    # grad_2 = torch.autograd.grad(outputs=grad_1[0],inputs=x)
    # print(grad_2)

    # 梯度不自动清零示例(需要手动进行清零)
    # w = torch.tensor(data=[1.],requires_grad=True)
    # x = torch.tensor(data=[2.],requires_grad=True)

    # for i in range(2):
    #     a = torch.add(w,x)
    #     b = torch.add(w,1)
    #     y = torch.mul(a,b)

    #     y.backward()
    #     print(w.grad)

    #     w.grad.zero_()

    # autograd中依赖于叶子结点的结点，requires_grad默认为True
    w = torch.tensor(data=[1.],requires_grad=True)
    x = torch.tensor(data=[2.],requires_grad=True)

    a = torch.add(w,x)
    b = torch.add(w,1)
    y = torch.mul(a,b)

    print(a.requires_grad,b.requires_grad,y.requires_grad)