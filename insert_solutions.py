
import os
import re
import shutil

# Configuration
TARGET_FILE = "/Users/kapsitis/workspace-public/nms-courses/avg-pulcins-2026/class16-reading-geometry/content.md"
PROBLEM_BASE = "/Users/kapsitis/workspace-public/math/problembase"
TARGET_DIR = os.path.dirname(TARGET_FILE)

def get_source_path(problem_id):
    # LV.VOL.2023.9.4 -> LV.VOL/lv-vol-2023/content_lv.md
    parts = problem_id.split('.')
    if len(parts) < 3:
        # Check if format is LV.AMO.2017.8.3
        # It should be.
        return None
        
    country = parts[0]
    olympiad = parts[1]
    year = parts[2]
    
    # Construct directory name
    dir_name = f"{country.lower()}-{olympiad.lower()}-{year}"
    base_dir = f"{country}.{olympiad}"
    
    path = os.path.join(PROBLEM_BASE, base_dir, dir_name, "content_lv.md")
    return path

def extract_solution(source_path, problem_id):
    if not os.path.exists(source_path):
        print(f"Source not found: {source_path}")
        return None, []

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the problem block
    # Pattern: # <lo-sample/> LV.VOL.2023.9.4
    problem_pattern = re.compile(rf"# <lo-sample/> {re.escape(problem_id)}\s+", re.MULTILINE)
    match = problem_pattern.search(content)
    if not match:
        print(f"Problem {problem_id} not found in {source_path}")
        return None, []
    
    start_index = match.end()
    
    # Extract until next problem or end of file
    next_problem_pattern = re.compile(r"^# <lo-sample/>", re.MULTILINE)
    next_match = next_problem_pattern.search(content, start_index)
    end_index = next_match.start() if next_match else len(content)
    
    problem_block = content[start_index:end_index]
    
    # Find "## Atrisinājums"
    solution_pattern = re.compile(r"## Atrisinājums\s+", re.MULTILINE)
    sol_match = solution_pattern.search(problem_block)
    
    if not sol_match:
        print(f"Solution header not found for {problem_id}")
        return None, []
    
    solution_text = problem_block[sol_match.end():].strip()
    
    # Find images
    # ![](filename.png)
    # This regex captures the URL/filename inside the parentheses.
    # We should grab the filename only, but usually it is just a filename.
    image_pattern = re.compile(r"!\[.*?\]\((.*?)\)")
    images = image_pattern.findall(solution_text)
    
    return solution_text, images

def process_problem(problem_id):
    source_path = get_source_path(problem_id)
    if not source_path:
        print(f"Cannot determine source path for {problem_id}")
        return None, []
        
    sol_text, images = extract_solution(source_path, problem_id)
    if not sol_text:
        return None, []
        
    # Copy images
    source_dir = os.path.dirname(source_path)
    for img_ref in images:
        # img_ref might be "filename.png" or "filename.png){ width=... }" 
        # Actually my regex `!\[.*?\]\((.*?)\)` stops at the first `)`, so it should be just "filename.png".
        # However, if there are spaces or other characters, it might be tricky.
        # Assuming standard markdown format where url/filename is first.
        # Just in case, split by space and take first part if it looks like a URL/filename?
        # Usually local images don't have spaces.
        
        # Check if the file exists as is.
        img_name = img_ref.split(' ')[0] # naive, but usually works for simple filenames
        img_source = os.path.join(source_dir, img_name)
        
        if os.path.exists(img_source):
            try:
                shutil.copy(img_source, TARGET_DIR)
                print(f"Copied {img_name} to {TARGET_DIR}")
            except Exception as e:
                print(f"Error copying {img_name}: {e}")
        else:
            print(f"Image not found at source: {img_source}")
            
    return sol_text, images

def main():
    print("Starting solution insertion...")
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    # Regex to identify problem headers in target file
    # ## 1.uzdevums (LV.VOL.2023.9.4) {-}
    # But wait, problem base might have inconsistent spacing.
    # The target file has: `## 1.uzdevums (LV.VOL.2023.9.4) {-}`
    header_pattern = re.compile(r"## \d+\.uzdevums \((.*?)\) \{-")
    
    current_problem_id = None
    buffer = []
    
    for line in lines:
        header_match = header_pattern.search(line)
        if header_match:
            # We found a NEW problem header.
            # If we were processing a previous problem, finish it.
            if current_problem_id:
                # Add the accumulated buffer (the text of the previous problem)
                new_lines.extend(buffer)
                buffer = []
                
                # Fetch and add solution for the previous problem
                print(f"Processing ID: {current_problem_id}")
                sol_text, images = process_problem(current_problem_id)
                if sol_text:
                    new_lines.append("\n\n::: solution\n**Atrisinājums:**\n\n")
                    new_lines.append(sol_text + "\n")
                    new_lines.append("::: \n\n")
            
            # Start tracking new problem
            current_problem_id = header_match.group(1)
            new_lines.append(line) # Add the header line itself
        
        else:
            # Not a header line.
            if current_problem_id:
                buffer.append(line)
            else:
                # Preamble before first problem
                new_lines.append(line)
    
    # Handle the very last problem
    if current_problem_id:
        new_lines.extend(buffer)
        print(f"Processing ID: {current_problem_id}")
        sol_text, images = process_problem(current_problem_id)
        if sol_text:
            new_lines.append("\n\n::: solution\n**Atrisinājums:**\n\n")
            new_lines.append(sol_text + "\n")
            new_lines.append("::: \n\n")

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Done.")

if __name__ == "__main__":
    main()
