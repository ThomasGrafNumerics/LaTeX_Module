import os

def create_custom_eps(filename, text, x, y, size):
    # Define paths relative to this script
    # '..' moves up to the parent directory (MA), then into 'Figures'
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'Figures')
    filepath = os.path.join(output_dir, filename)

    header = f"""%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: 0 0 300 150
/Helvetica findfont {size} scalefont setfont
"""
    drawing = f"{x} {y} moveto ({text}) show\n"
    footer = "showpage\n%%EOF"
    
    with open(filepath, "w") as f:
        f.write(header + drawing + footer)
    print(f"File saved to: {filepath}")

if __name__ == "__main__":
    create_custom_eps("output.eps", "Hello LaTeX!", 50, 70, 55)