import torch

if __name__ == '__main__':
    tensor1 = torch.randn(size=(3,3))
    tensor2 = torch.ones_like(input=tensor1)
    tensor_add = torch.add(input=tensor1,alpha=10,other=tensor2)
    print(tensor1)
    print(tensor2)
    print(tensor_add)