# print("Hello World")

# from core.utils.helpers import load_yml

# PREFIX = "params"
# out = load_yml("test.yml", PREFIX)

import subprocess
import os

def execute_notebook(notebook_path):
    """Executes a Jupyter Notebook and saves it with outputs."""
    try:
        cmd = ['jupyter', 'nbconvert', '--execute', notebook_path, '--inplace']
        subprocess.run(cmd, check=True)
        print(f"Notebook executed successfully: {notebook_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing notebook: {e}")

def convert_notebook_to_html(notebook_path, output_dir="."):
   """Converts a Jupyter Notebook to HTML, saving it in the specified directory."""
   try:
       notebook_name = os.path.basename(notebook_path)
       name_without_extension = os.path.splitext(notebook_name)[0]
    
       cmd = ['jupyter', 'nbconvert', '--to', 'html', notebook_path, '--output-dir', output_dir, '--output', name_without_extension]
       subprocess.run(cmd, check=True)
       print(f"Notebook converted to HTML successfully: {notebook_path} -> {output_dir}/{name_without_extension}.html")
   except subprocess.CalledProcessError as e:
       print(f"Error converting notebook to HTML: {e}")

# Example usage:
notebook_filepath = './datascience/notebooks/test.ipynb'
output_directory = 'reports'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

execute_notebook(notebook_filepath)
convert_notebook_to_html(notebook_filepath, output_directory)