from baselines.deepq import models  # noqa
from baselines.deepq.build_graph import build_act, build_train, build_act_eps  # noqa
from baselines.deepq.simple import learn, load  # noqa
from baselines.deepq.replay_buffer import ReplayBuffer, PrioritizedReplayBuffer  # noqa

def wrap_atari_dqn(env):
    from baselines.common.atari_wrappers import wrap_deepmind
    return wrap_deepmind(env, frame_stack=True, scale=True)
