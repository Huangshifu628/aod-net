import torch
pthfile = r'D:\aod-net\snapshots\dehazer.pth'
net = torch.load(pthfile)
print(net)
