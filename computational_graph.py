import torch

if __name__ == '__main__':
    w = torch.tensor(data=[1.],requires_grad=True)
    x = torch.tensor(data=[2.],requires_grad=True)

    a = torch.add(w,x)
    b = torch.add(w,1)
    y = torch.mul(a,b)

    y.backward()
    print(w.grad)

    print(w.is_leaf,x.is_leaf,a.is_leaf,b.is_leaf,y.is_leaf)
    print(w.grad,x.grad,a.grad,b.grad,y.grad)
    print(w.grad_fn,x.grad_fn,a.grad_fn,b.grad_fn,y.grad_fn)