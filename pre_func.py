import os
def meta_images(directory):
  """
  Makes a summary of components from a directory
  Args:
    directory (str): filepath
  """
  for dirpath, dirnames, filenames in os.walk(directory):
    print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")


def unzip_data(filename):
  """
  Unzips filename into the current working directory.
  Args:
    filename (str): a filepath to a target zip folder to be unzipped.
  """
  zip_ref = zipfile.ZipFile(filename, "r")
  zip_ref.extractall()
  zip_ref.close()

# Walk through an image classification directory and find out how many files (images)
# are in each subdirectory.