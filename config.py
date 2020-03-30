# paths
import platform
import os

if platform.system() == 'Windows':
    root_dir = './'
else:
    root_dir = '/ssdmnt'
    
task = 'OpenEnded'
dataset = 'vqainsta'

qa_path = os.path.join(root_dir, dataset, 'vqa')  # directory containing the question and annotation jsons
train_path = os.path.join(root_dir, dataset, 'train2014')  # directory of training images
val_path = os.path.join(root_dir, dataset, 'val2014')  # directory of validation images
test_path = os.path.join(root_dir, dataset, 'test2015')  # directory of test images
preprocessed_path = os.path.join(root_dir, dataset, 'resnet-14x14.h5')  # path where preprocessed features are saved to and loaded from
vocabulary_path = 'embedding/vocab.json'  # path where the used vocabularies for question and answers are saved to

# preprocess config
preprocess_batch_size = 4
image_size = 448  # scale shorter end of image to this size and centre crop
output_size = image_size // 32  # size of the feature maps after processing through a network
output_features = 2048  # number of feature maps thereof
central_fraction = 0.875  # only take this much of the centre when scaling and centre cropping

# training config
epochs = 50
batch_size = 128
initial_lr = 1e-3  # default Adam lr
lr_halflife = 50000  # in iterations
data_workers = 8 # cause error in python 3.6
max_answers = 12
