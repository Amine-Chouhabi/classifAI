# class for NoteBook
import nbformat as nbf
from Cell import Cell
from CellType import CellType

class NoteBook:
    """Class for NoteBook"""
    def __init__(self, name):
        self.name = name
        self.cells = []
        self.cell_number = 0

    def __str__(self):
        return "NoteBook: " + self.name + " " + str(self.cells)

    def __repr__(self):
        return self.__str__()

    def add_cell(self, cell_type, source):
        self.cell_number += 1
        cell = Cell(self.cell_number, cell_type, source)
        self.cells.append(cell)

    def get_cells(self):
        return self.cells

    def get_cell(self, cell_number):
        for cell in self.cells:
            if cell.get_number() == cell_number:
                return cell
        return None

    def get_cell_type(self, cell_number):
        cell = self.get_cell(cell_number)
        if cell is not None:
            return cell.get_cell_type()
        return None

    def get_cell_source(self, cell_number):
        cell = self.get_cell(cell_number)
        if cell is not None:
            return cell.get_source()
        return None

    def get_cell_number(self):
        return self.cell_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cell_numbers(self):
        cell_numbers = []
        for cell in self.cells:
            cell_numbers.append(cell.get_number())
        return cell_numbers

    def get_cell_types(self):
        cell_types = []
        for cell in self.cells:
            cell_types.append(cell.get_cell_type())
        return cell_types

    def get_cell_sources(self):
        cell_sources = []
        for cell in self.cells:
            cell_sources.append(cell.get_source())
        return cell_sources

    def get_notebook(self):
        notebook = []
        #notebook['name'] = self.name
        #notebook['cell_number'] = self.cell_number
        for cell in self.cells:
            if (cell.get_cell_type() == CellType.MARKDOWN):
                notebook.append(nbf.v4.new_markdown_cell(cell.source))
            elif (cell.get_cell_type() == CellType.CODE):
                notebook.append(nbf.v4.new_code_cell(cell.source))
            elif (cell.get_cell_type() == CellType.RAW):
                notebook.append(nbf.v4.new_raw_cell(cell.source))
            elif (cell.get_cell_type() == CellType.HEADING):
                notebook.append(nbf.v4.new_heading_cell(cell.source))
        return notebook
    
    def add_notebook(self, notebook):
        self.name = notebook    ['name']
        self.cell_number = notebook['cell_number']
        self.cells = notebook['cells']

    def get_notebook_json(self):
        import json
        return json.dumps(self.get_notebook())

    def generate_notebook_file(self, file_name):
        nb = nbf.v4.new_notebook()
        text = """\
        #Notebook : """ + self.name + """
        This is an auto-generated notebook."""
        nb['cells'] = [nbf.v4.new_markdown_cell(text)]
        nb['cells'] += self.get_notebook()

    
        fname = 'test.ipynb'

        with open(fname, 'w') as f:
            nbf.write(nb, f)


