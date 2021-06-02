import torchvision.models as models
import torch
from ptflops import get_model_complexity_info

with torch.cuda.device(0):
  net = models.densenet161(pretrained=True)
  # print(net.eval())
  macs, params = get_model_complexity_info(net, (3, 448, 448), as_strings=True,
                                           print_per_layer_stat=False, verbose=True)
  # macs, params = get_model_complexity_info(net, (3, 224, 224), as_strings=True,
  #                                          print_per_layer_stat=False, verbose=True)
  print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
  print('{:<30}  {:<8}'.format('Number of parameters: ', params))