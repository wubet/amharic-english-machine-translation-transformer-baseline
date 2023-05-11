import os

import matplotlib.pyplot as plt

# Get the current working directory
current_dir = os.getcwd()


def visualize_learningrate(steps, learning_rate, source_language, target_language, model_name):
    """
    :param steps:
    :param learning_rate:
    :param source_language:
    :param target_language:
    :param model_name:
    :return:
    """
    learning_rate_path = 'tf-transformer/output/temp_learning_rate'

    plt.plot(steps, learning_rate)
    plt.title(source_language + " to " + target_language + " " + model_name + " Learning Rate")
    plt.ylabel("Learning Rate")
    plt.xlabel("Train Step")
    # plt.show()
    plt.savefig(os.path.join(current_dir, learning_rate_path))


def visualize_transformer_training(epoch, accuracies, losses, source_language, target_language, model_name):
    """
    Draw plot of the training history for a deep learning model
    :param history: history object of the training
    :param model_name: name of the deep learning model
    :return: none
    """
    accuracy_path = 'tf-transformer/output/' + model_name + '_accuracy_hist.png'
    loss_path = 'tf-transformer/output/' + model_name + '_loss_hist.png'

    plt.figure()
    # visualize the training history
    plt.plot(epoch, accuracies)
    plt.title(source_language + " to " + target_language + " " + model_name + " Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.savefig(os.path.join(current_dir, accuracy_path))
    # plt.show()

    plt.figure()
    plt.plot(epoch, losses)
    plt.title(source_language + " to " + target_language + " " + model_name + " Model Loss")
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.savefig(os.path.join(current_dir, loss_path))
    # plt.show()
