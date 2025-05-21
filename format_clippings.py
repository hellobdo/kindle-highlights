import re
import os

def format_clippings(input_filename='clippings.md', output_filename='exports/formatted_clippings.md'):
    """
    Reads Kindle clippings from input_filename, formats them according to specific rules,
    and writes the results to output_filename.

    Expected input format per clipping:
    Yellow highlight | Page: X
    or
    Yellow highlight | Location: X
    <empty line>
    Highlight text line 1
    Highlight text line 2 (optional)
    ...
    <potentially empty line>
    Note: XXX (optional)
    <empty line>

    Output format per clipping:
    "Consolidated highlight text..." (page: X)
    or
    "Consolidated highlight text..." (location: X)
    or
    "Consolidated highlight text..." (Note: XXX, page: X)
    or
    "Consolidated highlight text..." (Note: XXX, location: X)
    """
    input_filepath = os.path.abspath(input_filename)
    output_filepath = os.path.abspath(output_filename)

    if not os.path.exists(input_filepath):
        print(f"Error: Input file '{input_filepath}' not found.")
        return

    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_filepath)
        os.makedirs(output_dir, exist_ok=True)

        with open(input_filepath, 'r', encoding='utf-8') as infile, \
             open(output_filepath, 'w', encoding='utf-8') as outfile:

            lines = infile.readlines()
            i = 0
            processed_count = 0
            while i < len(lines):
                line = lines[i].strip()
                # Check for the highlight marker line - now matches both Page and Location
                match = re.match(r"Yellow highlight \| (Page|Location): (\d+)", line)
                if match:
                    location_type = match.group(1).lower()  # 'page' or 'location'
                    number = match.group(2)
                    i += 1 # Move past the marker line

                    # Skip the expected empty line immediately after the marker
                    if i < len(lines) and lines[i].strip() == "":
                        i += 1
                    # Optional: Add warning if format deviates, but proceed cautiously
                    # else:
                    #     print(f"Warning: Expected empty line after marker for {location_type} {number}, around input line {i+1}.")

                    highlight_text_lines = []
                    # Read the highlight text lines until an empty line or next marker or EOF
                    while i < len(lines):
                        current_line_stripped = lines[i].strip()
                        # Stop if it's an empty line or the start of the next highlight
                        if current_line_stripped == "" or re.match(r"Yellow highlight \| (?:Page|Location): (\d+)", current_line_stripped):
                             break
                        # Stop also if it's a note line (don't include note in highlight text)
                        if current_line_stripped.startswith("Note:"):
                            break
                        highlight_text_lines.append(current_line_stripped)
                        i += 1

                    # Now check for a Note line immediately following the highlight text
                    note_text = None
                    # Skip potential empty line between highlight and note
                    if i < len(lines) and lines[i].strip() == "":
                         i += 1

                    # Check if the current line is a note
                    if i < len(lines) and lines[i].strip().startswith("Note:"):
                        note_match = re.match(r"Note:\s*(.*)", lines[i].strip())
                        if note_match:
                            note_text = note_match.group(1).strip()
                            i += 1 # Consume the note line

                    if highlight_text_lines:
                        full_highlight_text = " ".join(highlight_text_lines)
                        # Escape existing double quotes within the highlight text
                        full_highlight_text = full_highlight_text.replace('"', '\\"')

                        # Format the output line based on whether a note was found and the location type
                        if note_text:
                            formatted_line = f'"{full_highlight_text}" (Note: {note_text}, {location_type}: {number})\n\n'
                        else:
                            formatted_line = f'"{full_highlight_text}" ({location_type}: {number})\n\n'

                        outfile.write(formatted_line)
                        processed_count += 1

                    # Skip potential empty lines after the note or highlight text before the next marker
                    while i < len(lines) and lines[i].strip() == "":
                        i += 1
                    # If we stopped because of the next marker, the outer loop's i increment
                    # will handle moving to that marker line correctly.
                    # If we stopped at EOF, the loop condition handles it.

                else:
                    # This line is not a highlight marker, skip it
                    i += 1

        print(f"Successfully processed {processed_count} highlights.")
        print(f"Formatted clippings saved to '{output_filepath}'")

    except Exception as e:
        print(f"An error occurred during processing: {e}")
        print(f"Please check the input file format near the error.")

if __name__ == "__main__":
    # Assuming clippings.md is in the same directory as the script
    # or in the current working directory where the script is run.
    format_clippings() 