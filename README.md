# Kindle Highlights Formatter

A simple Python script to format Kindle clippings exported from `My Clippings.txt` (or a similar file like the provided `clippings.md`) into a more readable Markdown format.

## Requirements

*   Python 3

## Usage

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

## Output Format

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
