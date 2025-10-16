from contextlib import chdir  # Python 3.11+

from make_readme import make_readme

def test_make_readme(tmp_path):
    """Test creating a README file in current working directory."""
    project_name = "My Awesome Project"

    # Change to temporary directory and run function
    with chdir(tmp_path):
        make_readme(project_name)

    # Verify file was created in the temporary directory
    readme_file = tmp_path / "readme.md"
    assert readme_file.exists()

    content = readme_file.read_text()
    assert content == "# My Awesome Project\n\nTODO\n"
