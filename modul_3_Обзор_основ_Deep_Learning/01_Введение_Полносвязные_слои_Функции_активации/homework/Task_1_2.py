import torch


def function02(x: torch.Tensor):
    x_size = x.shape[1]
    return torch.rand(x_size, dtype=torch.float32, requires_grad=True)
