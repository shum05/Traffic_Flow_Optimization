import os

# Define the main project directory
project_dir = "Traffic_Flow_Optimization"

# Define subdirectories and files
folders = [
    "data/raw",
    "data/processed",
    "data/external",
    "notebooks",
    "src",
    "config",
    "logs",
    "reports/figures"
]

files = {
    "notebooks/EDA.ipynb": "",
    "notebooks/experiments.ipynb": "",
    "src/__init__.py": "",
    "src/data_processing.py": "",
    "src/model_training.py": "",
    "src/optimization.py": "",
    "src/evaluation.py": "",
    "config/config.yaml": "# Configuration parameters",
    "logs/traffic_flow.log": "",
    "reports/final_report.md": "# Final Project Report",
    "requirements.txt": "pandas\nnumpy\nscikit-learn\nmatplotlib\npyyaml",
    "README.md": "# Traffic Flow Optimization Project\n\nProject description and instructions."
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(project_dir, folder), exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(os.path.join(project_dir, file_path), 'w') as f:
        f.write(content)

print(f"Project structure for '{project_dir}' has been created successfully!")
