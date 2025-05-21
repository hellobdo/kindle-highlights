import os
import re
from datetime import datetime

def parse_clippings(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content into individual clippings
    clippings = content.split('==========')
    
    # Dictionary to store highlights by book
    books = {}
    
    for clipping in clippings:
        if not clipping.strip():
            continue
            
        lines = clipping.strip().split('\n')
        if len(lines) < 3:
            continue
            
        # Extract book title and author
        title_author = lines[0].strip()
        # Extract highlight/note content
        content = lines[3].strip() if len(lines) > 3 else ""
        
        # Skip if no content
        if not content:
            continue
            
        # Add to books dictionary
        if title_author not in books:
            books[title_author] = []
        books[title_author].append(content)
    
    return books

def create_markdown_files(books, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    for title_author, highlights in books.items():
        # Create a safe filename from the title
        safe_filename = re.sub(r'[^\w\s-]', '', title_author)
        safe_filename = re.sub(r'[-\s]+', '-', safe_filename).strip('-_')
        file_path = os.path.join(output_dir, f"{safe_filename}.md")
        
        with open(file_path, 'w', encoding='utf-8') as file:
            # Write header
            file.write(f"# {title_author}\n\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Write highlights in the desired format
            for highlight in highlights:
                # Escape any double quotes in the highlight text
                escaped_highlight = highlight.replace('"', '\\"')
                file.write(f'"{escaped_highlight}"\n\n')

def main():
    input_file = "My Clippings.txt"
    output_dir = "exports/items"
    
    print("Reading clippings file...")
    books = parse_clippings(input_file)
    
    print(f"Found {len(books)} books with highlights")
    print("Creating markdown files...")
    create_markdown_files(books, output_dir)
    print("Done!")

if __name__ == "__main__":
    main() 