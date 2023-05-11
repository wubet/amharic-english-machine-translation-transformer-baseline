import os
import shutil

# Get the current working directory
current_dir = os.getcwd()

# Specify the folder you want to move
datasets_folder_name = "unified-amharic-english-corpus"

# Specify the transformer folder where you want to move
transformer_folder_name = "tf-transformer"

# Specify the commons folder where you want to move
commons_path = "tf-transformer/commons"

# Specify the create tfRecord machine translation file you want to move
create_tfrecord_file = "create_tfrecord_machine_translation.py"

# Specify the transliteration file you want to move
transliteration_file = "transliteration.py"

# Specify the create_transliteration file you want to move
create_transliteration_file = "create_transliteration.py"

# Specify the run_trainer file you want to move
run_trainer_file = "run_trainer.py"

# Specify the visualization file you want to move
visualization_file = "visualization.py"

# Specify the model_runners file you want to move
model_runners_file = "model_runners.py"

# Specify the run_evaluator file you want to move
run_evaluator_file = "run_evaluator.py"

# Specify the datasets source directory
source = os.path.join(current_dir, datasets_folder_name);

# Specify the destination directory
destination = os.path.join(current_dir, transformer_folder_name)

# Specify the create_tfRecord_machine_translation source directory
source_create_tfRecord = os.path.join(current_dir, create_tfrecord_file)

# Specify the transliteration source directory
source_transliteration = os.path.join(current_dir, transliteration_file)

# Specify the commons folder destination directory
commons_destination_dir = os.path.join(current_dir, commons_path)

# Specify the create_transliteration source directory
source_create_transliteration = os.path.join(current_dir, create_transliteration_file)

# Specify the run_trainer source directory
source_run_trainer = os.path.join(current_dir, run_trainer_file)

# Specify the visualization source directory
source_visualization = os.path.join(current_dir, visualization_file)

# Specify the model_runners source directory
source_model_runners = os.path.join(current_dir, model_runners_file)

# Specify the run_evaluator source directory
source_run_evaluator = os.path.join(current_dir, run_evaluator_file)


# Move the datasets folder to the destination directory
shutil.move(source, destination)

# Move the create_tfRecord_machine_translation file into the destination
os.replace(source_create_tfRecord, os.path.join(commons_path, create_tfrecord_file))

# Move the transliteration file into the destination
shutil.move(source_transliteration, commons_destination_dir)

# # Move the create_transliteration file into the destination
shutil.move(source_create_transliteration, commons_destination_dir)

# Move the run_trainer file into the destination
os.replace(source_run_trainer, os.path.join(destination, run_trainer_file))

# Move the visualization file into the destination
shutil.move(source_visualization, transformer_folder_name)

# Move the model_runner file into the destination
os.replace(source_model_runners, os.path.join(destination, model_runners_file))

# Move the run_evaluator file into the destination
os.replace(source_run_evaluator, os.path.join(destination, run_trainer_file))