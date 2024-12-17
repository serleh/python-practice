import pandas as pd
import random
import os

def plot_loss_curves(history):
  """
    Returns seperate loss curve for training and validation metrics
  """
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  accuracy = history.history['accuracy']
  val_accuracy = history.history['val_accuracy']

  epochs = range(len(history.history['loss']))

  # plot the loss
  plt.plot(epochs,loss,label='Training loss')
  plt.plot(epochs,val_loss,label='Validation loss')
  plt.title('loss')
  plt.xlabel('epochs')
  plt.legend()

  plt.figure()
  # Plot accuracy
  plt.plot(epochs,accuracy,label='Training accuracy')
  plt.plot(epochs,val_accuracy, label='Validation accuracy')
  plt.title('accuracy')
  plt.xlabel('epochs')
  plt.legend()




def view_random_images(target_dir, target_class, num_images=6):
    """"
    This function accept target_dir, target_class, and number_images
    To plot random images
    """
    # Setup target image directory from a specific class
    target_folder = os.path.join(target_dir,target_class)

    # Get random image path
    random_images = random.sample(os.listdir(target_folder), num_images)


    # Plot 

    plt.figure(figsize=(10,10))
    plt.suptitle(f"Random Images from class {target_class}", fontsize=16)

    for i, image_name in enumerate(random_images):
        img = mpimg.imread(os.path.join(target_folder, image_name))

        ax = plt.subplot(3,3, i+1)
        ax.imshow(img)
        ax.axis("off")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to fit the title nicely
    plt.show()



 #Create a tensorflow callback

import datetime
def create_tensorboard_callback(dir_name, experiment_name):
  log_dir = dir_name + "/" + experiment_name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
  tensorboard_callback = keras.callbacks.TensorBoard(
      log_dir=log_dir
  )
  print(f"Saving TensorBoard log files to: {log_dir}")
  return tensorboard_callback