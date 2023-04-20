import os
import shutil

# Clone a Git project
os.system("git clone https://github.com/wubet/unified-amharic-english-corpus.git")

# Move the downloaded file to a specified directory
# shutil.move("<filename>", "/path/to/directory/")

# Get the current working directory
current_dir = os.getcwd();

# Specify the folder you want to move
source_folder_name = "unified-amharic-english-corpus";

# Specify the folder you want to move
destination_folder_name = "tf-transformer";

transliteration_file = "transliteration.py";

create_transliteration_file = "create_transliteration.py";

commons_path = "tf-transformer/commons"


# Specify the datasets source directory
source = os.path.join(current_dir, source_folder_name);

# Specify the destination directory
destination = os.path.join(current_dir, destination_folder_name)

# Specify the transliteration source directory
source_transliteration = os.path.join(current_dir, transliteration_file)

# Specify the commons folder destination directory
commons_destination_dir = os.path.join(current_dir, commons_path)

# Specify the create_transliteration source directory
source_create_transliteration = os.path.join(current_dir, create_transliteration_file)


# Move the datasets folder to the destination directory
shutil.move(source, destination)

# Move the transliteration file into the destination
shutil.move(source_transliteration, commons_destination_dir)

# Move the create_transliteration file into the destination
shutil.move(source_create_transliteration, commons_destination_dir)


