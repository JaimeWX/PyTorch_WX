import torch

if __name__ == '__main__':
    # # torch.cat()
    # tensor1 = torch.ones(size=(2,3))
    # tensor_cat1 = torch.cat(tensors=[tensor1,tensor1],dim=0)
    # tensor_cat2 = torch.cat(tensors=[tensor1,tensor1],dim=1)
    # tensor_cat3 = torch.cat(tensors=[tensor1,tensor1,tensor1],dim=1)
    # print(tensor_cat1)
    # print(tensor_cat1.shape) #(4,3)
    # print(tensor_cat2)
    # print(tensor_cat2.shape) #(2,6)
    # print(tensor_cat3)
    # print(tensor_cat3.shape) #(2,9)

    # # troch.stack()
    # tensor2 = torch.ones(size=(4,3))
    # tensor2_stack1 = torch.stack(tensors=[tensor2,tensor2],dim=2)
    # tensor2_stack2 = torch.stack(tensors=[tensor2,tensor2],dim=0)
    # tensor2_stack3 = torch.stack(tensors=[tensor2,tensor2,tensor2],dim=0)
    # print(tensor2_stack1)
    # print(tensor2_stack1.shape) # (4,3,2)
    # print(tensor2_stack2.shape) # (2,4,3)
    # print(tensor2_stack3.shape) # (3,4,3)

    # # torch.chunk()
    # tensor3 = torch.ones(size=(2,5))
    # tensor3_chunk1 = torch.chunk(input=tensor3,chunks=2,dim=1)
    # for idx,tensor in enumerate(tensor3_chunk1):
    #     print(idx,tensor,tensor.shape)

    # # torch.split()
    # tensor4 = torch.ones(size=(2,5))
    # tensor4_split1 = torch.split(tensor=tensor4,split_size_or_sections=2,dim=1)
    # for idx,tensor in enumerate(tensor4_split1):
    #     print(idx,tensor,tensor.shape)
    # tensor4_split2 = torch.split(tensor=tensor4,split_size_or_sections=[2,1,2],dim=1)
    # for idx,tensor in enumerate(tensor4_split2):
    #     print(idx,tensor,tensor.shape)

    # # torch.index_select()
    # tensor5 = torch.randint(low=0,high=9,size=(3,3))
    # idx = torch.tensor(data=[0,2],dtype=torch.long)
    # tensor5_index_select1 = torch.index_select(input=tensor5,dim=0,index=idx) #dim为0表示从行的角度
    # print(tensor5)
    # print(tensor5_index_select1)

    # # torch.masked_select()
    # tensor6 = torch.randint(low=0,high=9,size=(3,3))
    # mask = tensor6.ge(5) # ge: 大于等于 gt: 小于等于
    # tensor6_masked_select = torch.masked_select(input=tensor6,mask=mask)
    # print(tensor6)
    # print(mask)
    # print(tensor6_masked_select)

    # # torch.reshape()
    # tensor7 = torch.randperm(n=8)
    # tensor7_reshape1 = torch.reshape(input=tensor7, shape=(2,4))
    # tensor7_reshape2 = torch.reshape(input=tensor7,shape=(-1,2,2))
    # print(tensor7)
    # print(tensor7_reshape1)
    # print(tensor7_reshape2)
    # print(tensor7_reshape2.shape)

    # # torch.transpose()
    # tensor8 = torch.rand(size=(2,3,4))
    # tensor8_transpose1 = torch.transpose(input=tensor8,dim0=1,dim1=2)
    # print(tensor8.shape)
    # print(tensor8_transpose1.shape)

    # # torch.t()
    # tensor9 = torch.rand(size=(2,3))
    # tensor9_t1 = torch.t(input=tensor9)
    # print(tensor9.shape)
    # print(tensor9_t1.shape)

    # torch.squeeze()
    # tensor10 = torch.rand(size=(1,2,3,1))
    # tensor10_squeeze1 = torch.squeeze(input=tensor10)
    # tensor10_squeeze2 = torch.squeeze(input=tensor10,dim=0)
    # tensor10_squeeze3 = torch.squeeze(input=tensor10,dim=1)
    # print(tensor10_squeeze1.shape,tensor10_squeeze2.shape,tensor10_squeeze3.shape)

    # torch.unsqueeze()
    tensor11 = torch.rand(size=(2,3))
    tensor11_unsqueeze1 = torch.unsqueeze(input=tensor11,dim=0)
    tensor11_unsqueeze2 = torch.unsqueeze(input=tensor11,dim=1)
    tensor11_unsqueeze3 = torch.unsqueeze(input=tensor11,dim=2)
    print(tensor11_unsqueeze1.shape,tensor11_unsqueeze2.shape,tensor11_unsqueeze3.shape)
    