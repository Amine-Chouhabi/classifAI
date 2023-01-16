# This project for internal DSL language for data mining

# import the necessary packages
from NoteBook import NoteBook
from CellType import CellType



def main():
    # generate a notebook
    notebook = NoteBook("Test Notebook")
    notebook.add_cell(CellType.MARKDOWN, "This is a markdown cell")
    notebook.add_cell(CellType.CODE, "print('This is a code cell')")

    # print the notebook
    print(notebook)

    # generate the file
    notebook.generate_notebook_file("test.ipynb")

    

if __name__ == "__main__":
    main()


