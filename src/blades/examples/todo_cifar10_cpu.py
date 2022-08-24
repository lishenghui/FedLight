"""
"This" is my example-script
===========================

This example doesn't do much, it just makes a simple plot
"""


import ray
import torch.optim

from blades.datasets import CIFAR10
from blades.models.cifar10 import CCTNet
from blades.simulator import Simulator

cifar10 = CIFAR10(num_clients=40, iid=True)  # built-in federated cifar10 dataset

# configuration parameters
conf_params = {
    "dataset": cifar10,
    "aggregator": "mean",  # defense: robust aggregation
    "num_byzantine": 5,  # number of byzantine input
    "attack": "alie",  # attack strategy
    "attack_kws": {"num_clients": 20,  # attacker parameters
                    "num_byzantine": 5},
    "num_actors": 4,  # number of training actors
    "seed": 1,  # reproducibility
}

ray.init(num_gpus=0)
# ray.init(num_gpus=0, local_mode=True)
simulator = Simulator(**conf_params)

model = CCTNet()
server_opt = torch.optim.Adam(model.parameters(), lr=0.01)
# runtime parameters
run_params = {
    "model": model,  # global model
    "server_optimizer": 'SGD',  # ,server_opt  # server optimizer
    "client_optimizer": 'SGD',  # client optimizer
    "loss": "crossentropy",  # loss function
    "global_rounds": 400,  # number of global rounds
    "local_steps": 2,  # number of steps per round
    "server_lr": 1,
    "client_lr": 0.1,  # learning rate
}
simulator.run(**run_params)
