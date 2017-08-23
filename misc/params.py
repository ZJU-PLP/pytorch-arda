"""Parameters for ARDA."""

# params for dataset and data loader
data_root = "data"
dataset_mean_value = 0.5
dataset_std_value = 0.5
dataset_mean = (dataset_mean_value, dataset_mean_value, dataset_mean_value)
dataset_std = (dataset_std_value, dataset_std_value, dataset_std_value)
batch_size = 50
image_size = 64
src_dataset = "MNIST"
tgt_dataset = "USPS"

# params for critic
d_input_dims = 500
d_hidden_dims = 500
d_output_dims = 2
d_model_restore = None

# params for generator
g_model_restore = None

# params for classifier
c_model_restore = None

# params for training network
num_gpu = 1
num_epochs_pre = 100
num_epochs = 2000
log_step = 100
save_step = 100
manual_seed = None
model_root = "snapshots"

# params for optimizing models
learning_rate = 1e-4
beta1 = 0.5
beta2 = 0.9
