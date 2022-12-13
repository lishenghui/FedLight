
    | Know thy self, know thy enemy. A thousand battles, a thousand victories. --Sun Tzu

    | 知己知彼，百战百胜 ——孙武


.. raw:: html

    <p align=center>
        <img src="https://github.com/lishenghui/blades/blob/master/docs/source/_static/blades_logo.png" width="600" alt="Blades Logo">
    </p>

.. raw:: html

    <p align=center>
      <a href="https://www.python.org/downloads/release/python-397/">
        <img src="https://img.shields.io/badge/Python->=3.9-3776AB?logo=python" alt="Python">
      </a>
      <a href="https://github.com/pytorch/pytorch">
        <img src="https://img.shields.io/badge/PyTorch->=1.8-FF6F00?logo=pytorch" alt="pytorch">
      </a>
      <!-- <a href="https://pypi.org/project/graphwar/">
        <img src="https://badge.fury.io/py/graphwar.png" alt="pypi">
      </a>        -->
      <a href="https://github.com/lishenghui/blades/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/bladesteam/blades?style=plastic" alt="license">
        <img src="https://img.shields.io/badge/Contributions-Welcome-278ea5" alt="Contrib"/>
      </a>
    </p>



**Blades** is a simulator for **B**\ yzantine-robust federated **L**\ earning with **A**\ ttacks and **D**\ efenses
**E**\ xperimental **S**\ imulation.


**Blades** is designed to simulate attacks and defenses in federated learning with high performance and fast evaluation
of existing strategies and new techniques. Key features of **Blades** include:

   * **Specificity:** Different from existing federated learning simulators, **Blades** is specifically designed to simulate attacks and defenses. Thus we provide built-in implementations of representative attack strategies as well as robust aggregation schemes, so that users can efficiently validate their approaches and compare with existing solutions.

   * **Scalability:** **Blades** is scalable in terms of both clients and computing resources. In resource-constrained systems, it allows each trainer/actor to deal with multiple clients' requests sequentially, thus the scale of experiments is not limited by the number of trainers/actors. Based on Ray, **Blades** is deployable either on a single machine or a computing cluster.

   * **Extensibility:** **Blades** is highly compatible with Pytorch, allowing any combination of model, dataset and optimizer. It supports diverse federated learning  configurations, including standardized implementations such as **fedsgd** and **fedavg**, with Pytorch being the framework of choice for implementing the models. **Blades** allows the end users to incorporate new types of attacks, defenses, and optimization algorithms in a straightforward fashion.

NOTE: More features are under development and the APIs are subject to change.
If you are interested in this project, don't hesitate to contact me or make a PR directly.



..
    `Documentation <https://bladesteam.github.io/>`_ | `Examples <https://bladesteam.github.io/examples/index.html>`_ | `API Reference  <https://bladesteam.github.io/references/api_reference.html>`_


Installation
==================================================

..
    Option I. User Mode
    ---------------------------
..
    >>> pip install blades


..
    Option II (Recommended). Developer Mode
..
    -------------------------------------------

You can also develop your own attack/defense and evaluate it by cloning Blades:


.. code-block:: bash

    git clone https://github.com/lishenghui/blades.git
    cd src
    pip install -v -e .
    # "-v" means verbose, or more output
    # "-e" means installing a project in editable mode,
    # thus any local modifications made to the code will take effect without reinstallation.


Verify the installation
==============================

..
    Option I. User Mode
..
    ---------------------------
..
    TBD
..
    Option II. Developer Mode
..
    ---------------------------

.. code-block:: bash

    cd scripts
    python main.py --config_path ../config/example.yaml


..
    Get Started
    ==================================================
    How fast can we simulate attack and defense in federated learning?
    Take `ALIE Attack <https://github.com/bladesteam/blades/blob/master/src/blades/attackers/alieclient.py>`_ and
    `Trimmedmean Aggregation <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/trimmedmean.py>`_ as an `example <https://github.com/bladesteam/blades/blob/master/src/blades/examples/mini_example.py>`_.


.. include:: ../../src/blades/examples/mini_example.py
   :code: python


Built-in Implementations
==================================================
In detail, the following strategies are currently implemented:



Attacks
---------

General Attacks
^^^^^^^^^^^^^^^^^
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Strategy           | Description                                                                                                                                                                                              | Sourse                                                                                                    |
+====================+==========================================================================================================================================================================================================+===========================================================================================================+
| **Noise**          |  Put random noise to the updates.                                                                                                                                                                        | `Sourse <https://github.com/bladesteam/blades/blob/master/src/blades/attackers/noiseclient.py>`_          |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| **Labelflipping**  | `Fang et al. Local Model Poisoning Attacks to Byzantine-Robust Federated Learning <https://www.usenix.org/conference/usenixsecurity20/presentation/fang>`_, *USENIX Security' 20*                        | `Sourse <https://github.com/bladesteam/blades/blob/master/src/blades/attackers/labelflippingclient.py>`_  |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| **Signflipping**   | `Li et al. RSA: Byzantine-Robust Stochastic Aggregation Methods for Distributed Learning from Heterogeneous Datasets <https://ojs.aaai.org/index.php/AAAI/article/view/3968>`_, *AAAI' 19*               | `Sourse <https://github.com/bladesteam/blades/blob/master/src/blades/attackers/signflippingclient.py>`_   |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| **ALIE**           | `Baruch et al. A little is enough: Circumventing defenses for distributed learning <https://proceedings.neurips.cc/paper/2019/hash/ec1c59141046cd1866bbbcdfb6ae31d4-Abstract.html>`_ *NeurIPS' 19*       | `Sourse <https://github.com/bladesteam/blades/blob/master/src/blades/attackers/alieclient.py>`_           |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| **IPM**            | `Xie et al. Fall of empires: Breaking byzantine- tolerant sgd by inner product manipulation <https://arxiv.org/abs/1903.03936>`_, *UAI' 20*                                                              | `Sourse <https://github.com/bladesteam/blades/blob/master/src/blades/attackers/ipmclient.py>`_            |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

Adaptive Attacks
^^^^^^^^^^^^^^^^^
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Strategy                 | Description                                                                                                                                                                         | Sourse                                                                                                          |
+==========================+=====================================================================================================================================================================================+=================================================================================================================+
| **FangAttack**           |  `Fang et al. Local Model Poisoning Attacks to Byzantine-Robust Federated Learning <https://www.usenix.org/conference/usenixsecurity20/presentation/fang>`_, *USENIX Security' 20*  | `Sourse <https://github.com/bladesteam/blades/blob/master/src/blades/attackers/fangattackclient.py>`_           |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **DistanceMaximization** |  `Shejwalkar et al. Manipulating the byzantine: Optimizing model poisoning attacks and defenses for federated learning <https://par.nsf.gov/servlets/purl/10286354>`_, *NDSS' 21*   | `Sourse <https://github.com/bladesteam/blades/blob/master/src/blades/attackers/distancemaximizationclient.py>`_ |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+



Defenses
---------

Robust Aggregation
^^^^^^^^^^^^^^^^^^^

+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| Strategy              | Descriptions                                                                                                                                                                                                                                                | Source                                                                                                   |
+=======================+=============================================================================================================================================================================================================================================================+==========================================================================================================+
| **MultiKrum**         | `Blanchard et al. Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent <https://proceedings.neurips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html>`_, *NIPS'17*                                                       | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/multikrum.py>`_         |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **GeoMed**            | `Chen et al. Distributed Statistical Machine Learning in Adversarial Settings: Byzantine Gradient Descent <https://arxiv.org/abs/1705.05491>`_, *POMACS'18*                                                                                                 | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/geomed.py>`_            |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **AutoGM**            | `Li et al. Byzantine-Robust Aggregation in Federated Learning Empowered Industrial IoT <https://ieeexplore.ieee.org/abstract/document/9614992>`_, *IEEE TII'22*                                                                                             | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/autogm.py>`_            |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **Median**            | `Yin et al. Byzantine-robust distributed learning: Towards optimal statistical rates <https://proceedings.mlr.press/v80/yin18a>`_, *ICML'18*                                                                                                                | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/median.py>`_            |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **TrimmedMean**       | `Yin et al. Byzantine-robust distributed learning: Towards optimal statistical rates <https://proceedings.mlr.press/v80/yin18a>`_, *ICML'18*                                                                                                                | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/trimmedmean.py>`_       |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **CenteredClipping**  | `Karimireddy et al. Learning from History for Byzantine Robust Optimization <http://proceedings.mlr.press/v139/karimireddy21a.html>`_, *ICML'21*                                                                                                            | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/centeredclipping.py>`_  |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **Clustering**        | `Sattler et al. On the byzantine robustness of clustered federated learning <https://ieeexplore.ieee.org/abstract/document/9054676>`_, *ICASSP'20*                                                                                                          | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/clustering.py>`_        |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **ClippedClustering** | `Li et al. An Experimental Study of Byzantine-Robust sAggregation Schemes in Federated Learning <https://www.techrxiv.org/articles/preprint/An_Experimental_Study_of_Byzantine-Robust_Aggregation_Schemes_in_Federated_Learning/19560325>`_, *TechRxiv'22*  | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/clippedclustering.py>`_ |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **DnC**               | `Shejwalkar et al. Manipulating the Byzantine: Optimizing Model Poisoning Attacks and Defenses for Federated Learning <https://par.nsf.gov/servlets/purl/10286354>`_, *NDSS'21*                                                                             | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/dnc.py>`_               |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **SignGuard**         | `Xu et al. SignGuard: Byzantine-robust Federated Learning through Collaborative Malicious Gradient Filtering <https://arxiv.org/abs/2109.05872>`_, *ICDCS'22*                                                                                               | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/signguard.py>`_         |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+


Trust-based Strategies
^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| Strategy              | Description                                                                                                                                   | Source                                                                                                   |
+=======================+===============================================================================================================================================+==========================================================================================================+
| **FLTrust**           | `Cao et al. FLTrust: Byzantine-robust Federated Learning via Trust Bootstrapping <https://arxiv.org/abs/2012.13995>`_, NDSS'21                | `Source <https://github.com/bladesteam/blades/blob/master/src/blades/aggregators/fltrust.py>`_           |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+



Cluster Deployment
===================

To run **blades** on a cluster, you only need to deploy ``Ray cluster`` according to the `official guide <https://docs.ray.io/en/latest/cluster/user-guide.html>`_.


Citation
=========

Please cite our `paper <https://arxiv.org/abs/2206.05359>`_ (and the respective papers of the methods used) if you use this code in your own work:

::

   @article{li2022blades,
     title={Blades: A Simulator for Attacks and Defenses in Federated Learning},
     author= {Li, Shenghui and Ju, Li and Zhang, Tianru and Ngai, Edith and Voigt, Thiemo},
     journal={arXiv preprint arXiv:2206.05359},
     year={2022}
   }
