import matplotlib.pyplot as plt


def visualize_learningrate(steps, learning_rate, source_language, target_language, model_name):
    plt.plot(steps, learning_rate)
    plt.title(source_language + " to " + target_language + " " + model_name + " Learning Rate")
    plt.ylabel("Learning Rate")
    plt.xlabel("Train Step")
    # plt.show()
    plt.savefig('output/temp_learning_rate')


def visualize_transformer_training(epoch, accuracies, losses, source_language, target_language, model_name):
    """
    Draw plot of the training history for a deep learning model
    :param history: history object of the training
    :param model_name: name of the deep learning model
    :return: none
    """

    plt.figure()
    # visualize the training history
    plt.plot(epoch, accuracies)
    plt.title(source_language + " to " + target_language + " " + model_name + " Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.savefig('output/' + model_name + '_accuracy_hist.png')
    # plt.show()

    plt.figure()
    plt.plot(epoch, losses)
    plt.title(source_language + " to " + target_language + " " + model_name + " Model Loss")
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.savefig('output/' + '_loss_hist.png')
    # plt.show()
