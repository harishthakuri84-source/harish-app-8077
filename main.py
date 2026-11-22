# project_init.py - AI-Media-Video-Studio Initialization
import os
import subprocess

def init_project():
    project_path = "AI-Media-Video-Studio"
    os.makedirs(f"{project_path}/backend", exist_ok=True)
    os.makedirs(f"{project_path}/frontend", exist_ok=True)
    
    # Create .env template
    with open(f"{project_path}/.env", "w") as f:
        f.write("OPENAI_API_KEY=\nSTABILITY_AI_KEY=\n")
    
    # Git Init for Independent Repo
    subprocess.run(["git", "init"], cwd=project_path)
    
    print(f"Project {project_path} initialized safely.")

# Autonomous build flow initiated for AI-Media-Video-Studio.
