from pathlib import Path
import sys

def make_readme(project_name):
    """Create a basic README.md file in the current working directory."""
    with open("readme.md", mode="w") as file:
        file.write(f"# {project_name}\n\n")
        file.write("TODO\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python make_readme.py <project_name>")
        sys.exit(1)
    make_readme(sys.argv[1])