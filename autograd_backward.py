import torch

if __name__ == '__main__':
    # retain_graph的使用示例
    w = torch.tensor(data=[1.],requires_grad=True)
    x = torch.tensor(data=[2.],requires_grad=True)

    a = torch.add(w,x)
    b = torch.add(w,1)
    y = torch.mul(a,b)

    y.backward(retain_graph=True)
    y.backward()
    print(w.grad)

    # grad_tensors的使用示例
    w = torch.tensor(data=[1.],requires_grad=True) 
    x = torch.tensor(data=[2.],requires_grad=True)  

    a = torch.add(w,x) 
    b = torch.add(w,1) 

    y0 = torch.mul(a,b) # y0 = (w+x) * (w+1)
    y1 = torch.add(a,b) # y1 = (w+x) + (w+1)

    loss = torch.cat(tensors=[y0,y1],dim=0)
    grad_tensors = torch.tensor([1.,2.])

    loss.backward(gradient=grad_tensors)

    print(w.grad)