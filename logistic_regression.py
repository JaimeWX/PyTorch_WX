import torch
from torch import nn

# 数据
sample_nums = 100
mean_value = 1.7
bias = 1
n_data = torch.ones(size=(sample_nums,2))
x0 = torch.normal(mean=mean_value*n_data,std=1) + bias
y0 = torch.zeros(sample_nums)
x1 = torch.normal(mean=-mean_value*n_data,std=1) + bias
y1 = torch.ones(sample_nums)
train_x = torch.cat(tensors=(x0,x1),dim=0)
train_y = torch.cat(tensors=(y0,y1),dim=0)
print(train_x.shape)
print(train_y.shape)
# print(train_y.size(0))

# 模型
class LR(nn.Module):
    def __init__(self):
        super(LR, self).__init__()
        self.features = nn.Linear(2,1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self,x):
        x = self.features(x)
        x = self.sigmoid(x)
        return x
    
LR_net = LR()

# 损失函数
loss_fn = nn.BCELoss()

# 优化器
lr = 0.01
optimizer = torch.optim.SGD(params=LR_net.parameters(),lr=lr, momentum=0.9)

# 模型训练
for idx,iteration in enumerate(range(1000)):
    ## 前向传播
    y_pred = LR_net(x=train_x)

    ## 计算损失
    loss = loss_fn(input=y_pred.squeeze(),target=train_y)
    
    ## 反向传播
    loss.backward()

    ## 更新参数
    optimizer.step()

    ## 计算准确率
    mask = y_pred.ge(0.5).float().squeeze()
    correct = (mask == train_y).sum()
    acc = correct.item() / train_y.size(0)

    print(idx, acc)
    if acc > 0.99:
        break
