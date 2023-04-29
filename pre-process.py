import os
import shutil

# Clone a Git project
os.system("git clone https://github.com/wubet/unified-amharic-english-corpus.git")

# Move the downloaded file to a specified directory
# shutil.move("<filename>", "/path/to/directory/")

# Get the current working directory
current_dir = os.getcwd()

# Specify the folder you want to move
datasets_folder_name = "unified-amharic-english-corpus"

# Specify the transformer folder where you want to move
transformer_folder_name = "tf-transformer"

# Specify the commons folder where you want to move
commons_path = "tf-transformer/commons"

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

# Specify the datasets source directory
source = os.path.join(current_dir, datasets_folder_name);

# Specify the destination directory
destination = os.path.join(current_dir, transformer_folder_name)

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


# Move the datasets folder to the destination directory
shutil.move(source, destination)

# Move the transliteration file into the destination
shutil.move(source_transliteration, commons_destination_dir)

# Move the create_transliteration file into the destination
shutil.move(source_create_transliteration, commons_destination_dir)

# Move the run_trainer file into the destination
shutil.move(source_run_trainer, transformer_folder_name)

# Move the visualization file into the destination
shutil.move(source_visualization, transformer_folder_name)

# Move the model_runner file into the destination
shutil.move(source_model_runners, transformer_folder_name)


