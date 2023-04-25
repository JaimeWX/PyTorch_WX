import torch

if __name__ == '__main__':
    torch.manual_seed(10)
    W_h = torch.randn(size=(20,20),requires_grad=True)
    W_x = torch.randn(size=(20,10),requires_grad=True)

    x = torch.randn(size=(1,10))
    prev_h = torch.randn(size=(1,20))

    # print(prev_h.t().shape) t()的作用是转置
    h2h = torch.mm(W_h,prev_h.t())
    i2h = torch.mm(W_x,x.t())
    next_h = h2h + i2h
    next_h = next_h.tanh()

    loss = next_h.sum()
    print(loss)
    loss.backward()
    print(W_h.grad,W_x.grad)

