from onpolicy.scripts.train.train_sd import get_config, parse_args, main
from onpolicy.scripts.train_sd_scripts.experiment_name import get_experiment_name
import numpy as np
import os
os.environ["WANDB__SERVICE_WAIT"] = "300"

parser = get_config()
all_args = parse_args([], parser)

all_args.experiment_name = get_experiment_name("beta", "drop2-step2")
all_args.env_name = "search-deliver"
all_args.user_name = "ideas-mas"

all_args.num_agents = 4
all_args.agent_speed = 40.0
all_args.action_method = "neighbors"
all_args.observe_method = "pyg"
all_args.observe_method_global = "adjacency"
all_args.observation_radius = np.inf
all_args.observation_bitmap_size = 40
all_args.communication_model = "bernoulli"
all_args.communication_probability = 1.0
all_args.alpha = 1.0
all_args.beta = 10.0


all_args.drop_reward = 2.0
all_args.load_reward = 1.0
all_args.step_reward = 1.0
all_args.state_reward = 1.0
all_args.step_penalty = 0.2
all_args.agent_max_capacity = 1
# all_args.reward_method_terminal = "averageAverage"
all_args.reward_method_terminal = "average"
# all_args.reward_interval = 1

# all_args.graph_random = True
# all_args.graph_random_nodes = 9
all_args.graph_name = "9nodes"
all_args.graph_file = f"../../../../sdzoo/env/{all_args.graph_name}.graph"
# all_args.num_env_steps = 10000 #total number of steps
all_args.num_env_steps = 1e5 * 5 #total number of steps
all_args.episode_length = 1000 #number of steps in a training episode
all_args.max_cycles = all_args.episode_length / 5 #number of steps in an environment episode

all_args.algorithm_name = "rmappo"
all_args.use_gnn_policy = True
all_args.use_gnn_mlp_policy = True
all_args.gnn_layer_N = 8
all_args.gnn_hidden_size = 128
all_args.gnn_skip_connections = True
all_args.use_recurrent_policy = True
all_args.use_naive_recurrent_policy = False
all_args.use_centralized_V = True
all_args.use_gae = False
all_args.use_gae_amadm = True
all_args.share_policy = True
all_args.sep_share_policy = False
all_args.share_reward = False
all_args.skip_steps_sync = False # these need to be false to use max cycles
all_args.skip_steps_async = False
all_args.use_ReLU = True
# all_args.lr = 1e-3
# all_args.entropy_coef = 0.1
all_args.hidden_size = 512

all_args.n_rollout_threads = 1
all_args.save_interval = 1000
all_args.cuda = True
all_args.cuda_idx = 2

all_args.use_wandb = True

if __name__ == "__main__":
    main([], parsed_args = all_args)