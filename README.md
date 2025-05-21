# Kindle Highlights Formatter

A collection of Python scripts to format and organize Kindle clippings exported from `My Clippings.txt` into more readable and organized formats.

## Requirements

*   Python 3

## Scripts

### 1. Format Clippings (`format_clippings.py`)

Formats Kindle clippings into a single, readable markdown file.

#### Usage

1.  **Place your clippings file:** Ensure your Kindle clippings are in a file named `clippings.md` in the root directory of this project.
    The expected format includes lines like:
    ```
    Yellow highlight | Page: X

    Highlight text...

    Note: Optional note text...
    ```
2.  **Run the script:**
    ```bash
    python format_clippings.py
    ```
3.  **Find the output:** The formatted clippings will be saved in the `exports/` directory as `formatted_clippings.md`.

#### Output Format

The script generates entries in the following format:

*   Without notes:
    ```markdown
    "Highlight text..." (page: X)
    ```
*   With notes:
    ```markdown
    "Highlight text..." (Note: Optional note text..., page: X)
    ```

Each entry will be separated by a blank line.

### 2. Organize Clippings (`organize_clippings.py`)

Organizes Kindle clippings into separate markdown files, one per book, in the `exports/items/` directory.

#### Usage

1.  **Place your clippings file:** Ensure your Kindle clippings are in a file named `My Clippings.txt` in the root directory of this project.
2.  **Run the script:**
    ```bash
    python organize_clippings.py
    ```
3.  **Find the output:** Each book's highlights will be saved as a separate markdown file in the `exports/items/` directory.

#### Output Format

Each book's markdown file will contain:
```markdown
# Book Title (Author)

Generated on: YYYY-MM-DD HH:MM:SS

"Highlight text..."

"Another highlight text..."
```

## Note

The `exports/` directory and `My Clippings.txt` are gitignored to keep the repository clean. Make sure to keep your own copies of these files.
