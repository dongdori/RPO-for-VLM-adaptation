import easydict
from easydict import EasyDict as edict

cfg = edict()

cfg.model = edict()
cfg.model.ctx_len = 16
cfg.model.h_dim = 512