import ray

from blades.datasets.datasets import FLDataset


@ray.remote
class _RayActor(object):
    """Ray Actor"""
    
    def __init__(self, dataset: object, *args, **kwargs):
        """
       Args:
           aggregator (callable): A callable which takes a list of tensors and returns
               an aggregated tensor.
           log_interval (int): Control the frequency of logging training batches
           metrics (dict): dict of metric names and their functions
           use_cuda (bool): Use cuda or not
           debug (bool):
       """
        traindls, testdls = dataset.get_dls()
        self.dataset = FLDataset(traindls, testdls)
    
    def local_training(self, clients, model, local_round):
        update = []
        for i in range(len(clients)):
            clients[i].set_para(model)
            clients[i].on_train_round_start()
            data = self.dataset.get_train_data(clients[i].id(), local_round)
            clients[i].local_training(local_round, use_actor=True, data_batches=data)
            update.append(clients[i].get_update())
        return update
    
    def evaluate(self, clients, model, round_number, batch_size, metrics):
        update = []
        for i in range(len(clients)):
            clients[i].set_para(model)
            data = self.dataset.get_all_test_data(clients[i].id())
            result = clients[i].evaluate(
                round_number=round_number,
                test_set=data,
                batch_size=batch_size,
                metrics=metrics,
                use_actor=True,
            )
            update.append(result)
        return update

