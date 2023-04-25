import torch

if __name__ == '__main__':
    a = torch.ones(size=(1,))
    print(id(a),a)

    # a = a + torch.ones(size=(1,))
    # print(id(a),a)

    a += torch.ones(size=(1,))
    print(id(a),a)
                    