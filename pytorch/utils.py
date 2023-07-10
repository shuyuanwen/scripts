import numpy as np
import torch
import torch.nn as nn
import pandas as pd
import random
from torch.utils.data import Dataset, DataLoader

# 设置随机种子
seed = 0
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)

# 以类的方式定义超参数


class argparse():
    pass


args = argparse()
args.epochs, args.LR, args.patiance = [30, 0.01, 4]
args.hidden_size, args.input_size = [40, 30]
args.device = [torch.device("cuda:0" if torch.cuda.is_available() else "cpu")]


# 定义模型
class AAR(nn.Module):
    def __init__(self):
        super(AAR, self).__init__()
        pass

    def forward(self, x):
        pass
        return x


# 定义数据集
class AAR_Dataset(Dataset):
    def __init__(self, flag='train'):
        assert flag in ['train', 'test', 'valid']
        self.flag = flag
        self.lines = 1
        self.__load_data__()

    def __getitem__(self, index):
        label = 1
        context = 1
        return label, context

    def __len__(self):
        return len(self.lines)


AARtrain = AAR_Dataset(flag='train')
AARtrainloader = DataLoader(AARtrain, batch_size=2,
                            shuffle=True, num_workers=2)
AARtest = AAR_Dataset(flag='test')
AARtestloader = DataLoader(AARtest, batch_size=2, shuffle=True, num_workers=2)

# 实例化模型，设置loss 优化器设置
model = AAR().to(args.device)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(AAR.parameters, lr=args.LR)

train_loss = []
valid_loss = []
train_epochs_loss = []
valid_epochs_loss = []



for epoch in range(args.epochs):
    AAR.train()
    train_epoch_loss = []
    for idx, (data_x, data_y) in enumerate(train_dataloader, 0):
        data_x = data_x.to(torch.float32).to(args.device)
        data_y = data_y.to(torch.float32).to(args.device)
        outputs = AAR(data_x)
        optimizer.zero_grad()
        loss = criterion(data_y,outputs)
        loss.backward()
        optimizer.step()
        train_epoch_loss.append(loss.item())
        train_loss.append(loss.item())


        # ----------------valid--------------
        AAR.eval()
        