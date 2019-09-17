import torch
import os
from rectifai.settings import POSTURENET_PATH
from .network import PostureNetwork


def load_model():
    model = PostureNetwork()
    load_dict = torch.load(POSTURENET_PATH)
    model.load_state_dict(load_dict)

    return model