# ⚔🛡 **Blades**: A simulator for Byzantine-robust federated Learning with Attacks and Defenses Experimental Simulation

<!-- <p align="center">
  <img width = "450" height = "150" src="https://github.com/
" alt="banner"/>
  <br/>
</p> -->

<p align=center>
  <a href="https://www.python.org/downloads/release/python-360/">
    <img src="https://img.shields.io/badge/Python->=3.9-3776AB?logo=python" alt="Python">
  </a>    
  <a href="https://github.com/pytorch/pytorch">
    <img src="https://img.shields.io/badge/PyTorch->=1.8-FF6F00?logo=pytorch" alt="pytorch">
  </a>   
  <!-- <a href="https://pypi.org/project/graphwar/">
    <img src="https://badge.fury.io/py/graphwar.png" alt="pypi">
  </a>        -->
  <a href="https://github.com/EdisonLeeeee/GraphWar/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/EdisonLeeeee/GraphWar" alt="license">
    <img src="https://img.shields.io/badge/Contributions-Welcome-278ea5" alt="Contrib"/>    
  </a>       
</p>
                                                                   

> Know thy self, know thy enemy. A thousand battles, a thousand victories.
> 
> 「知己知彼，百战百胜」 ——《孙子兵法•谋攻篇》


NOTE: Blade is still in the early stages and the API are subject to change.
If you are interested in this project, don't hesitate to contact me or make a PR directly.

# 🚀 Installation

Please make sure you have installed [PyTorch](https://pytorch.org) and [Ray](https://docs.ray.io/en/latest/).


```bash
# Coming soon
pip install blades
```

<!-- or

```bash
# Recommended
git clone https://github.com/EdisonLeeeee/GraphWar.git && cd GraphWar
pip install -e . --verbose
``` -->

<!-- where `-e` means "editable" mode so you don't have to reinstall every time you make changes. -->

# ⚡ Get Started


## How fast can we train and evaluate your own GNN?
Take `GCN` as an example:
```python
import ray
from blades.simulator import Simulator
from blades.datasets import CIFAR10
from blades.models.cifar10 import CCTNet

cifar10 = CIFAR10(num_clients=20, iid=True) # built-in federated cifar10 dataset

# configuration parameters
conf_params = {
    "dataset": cifar10,
    "num_byzantine": 5,  # number of byzantine clients
    "attack": "IPM",     # attack strategy
    "aggregator": "Krum",# defense: robust aggregation
    "num_actors": 4,     # number of training actors
    "seed": 1            # reproducibility
}

ray.init(num_gpus=2)
simulator = Simulator(**conf_params)

# runtime parameters
run_params = {
    "model": CCTNet(),         # global model
    "server_optimizer": 'SGD', # server optimizer
    "client_optimizer": 'SGD', # client optimizer
    "loss": "crossentropy",    # loss function
    "global_rounds": 400,      # number of global rounds
    "local_steps": 20,         # number of steps per round
}
simulator.run(**run_params)
```


# 👀 Implementations

In detail, the following methods are currently implemented:

## ⚔ Attack

#### Untargeted Attack

| Methods          | Descriptions                                                                                                                                           | Examples                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **NoiseAttack** | Put random noise to the updates. | [[**Example**]](https://github.com/bladesteam/blades/blob/master/src/blades/attackers/noiseclient.py) |
| **NoiseAttack** | Put random noise to the updates. | [[**Example**]](https://github.com/bladesteam/blades/blob/master/src/blades/attackers/noiseclient.py) |
<!-- | **DICEAttack**   | *Waniek et al.* [Hiding Individuals and Communities in a Social Network](https://arxiv.org/abs/1608.00375), *Nature Human Behavior'16*                 | [[**Example**]](https://github.com/EdisonLeeeee/GraphWar/blob/master/examples/attack/targeted/dice_attack.py)   |
| **Nettack**      | *Zügner et al.* [Adversarial Attacks on Neural Networks for Graph Data](https://arxiv.org/abs/1805.07984), *KDD'18*                                    | [[**Example**]](https://github.com/EdisonLeeeee/GraphWar/blob/master/examples/attack/targeted/nettack.py)       |
| **FGAttack**     | *Chen et al.* [Fast Gradient Attack on Network Embedding](https://arxiv.org/abs/1809.02797), *arXiv'18*                                                | [[**Example**]](https://github.com/EdisonLeeeee/GraphWar/blob/master/examples/attack/targeted/fg_attack.py)     |
| **GFAttack**     | *Chang et al*.  [A Restricted Black - box Adversarial Framework Towards Attacking Graph Embedding Models](https://arxiv.org/abs/1908.01297), *AAAI'20* | [[**Example**]](https://github.com/EdisonLeeeee/GraphWar/blob/master/examples/attack/targeted/gf_attack.py)     |
| **IGAttack**     | *Wu et al.* [Adversarial Examples on Graph Data: Deep Insights into Attack and Defense](https://arxiv.org/abs/1903.01610), *IJCAI'19*                  | [[**Example**]](https://github.com/EdisonLeeeee/GraphWar/blob/master/examples/attack/targeted/ig_attack.py)     |
| **SGAttack**     | *Li et al.* [ Adversarial Attack on Large Scale Graph](https://arxiv.org/abs/2009.03488), *TKDE'21*                                                    | [[**Example**]](https://github.com/EdisonLeeeee/GraphWar/blob/master/examples/attack/targeted/sg_attack.py)     | -->




## 🛡 Defense

### Robust Aggregation

| Methods   | Descriptions                                                                                                                               | Examples                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Krum**   | *Blanchard et al.* [Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent](https://proceedings.neurips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html), *NIPS'17*              | [[**Example**]](https://github.com/EdisonLeeeee/GraphWar/blob/master/examples/models/gcn.py)   |
| **GeoMed**   | *Blanchard et al.* [Distributed Statistical Machine Learning in Adversarial Settings: Byzantine Gradient Descent](https://arxiv.org/abs/1705.05491), *NIPS'17*              | [[**Example**]](https://github.com/EdisonLeeeee/GraphWar/blob/master/examples/models/gcn.py)   |

<!-- 
# ❓ Known Issues
+ Despite our best efforts, we still had difficulty reproducing the results of [GNNGUARD](https://arxiv.org/abs/2006.08149) in the paper. If you find any problems, please don't hesitate to contact me.
+ Untargeted attacks are suffering from performance degradation, as also in DeepRobust, when a validation set is used during training with model picking. Such phenomenon has also been revealed in [Black-box Gradient Attack on Graph Neural Networks: Deeper Insights in Graph-based Attack and Defense](https://arxiv.org/abs/2104.15061). -->
