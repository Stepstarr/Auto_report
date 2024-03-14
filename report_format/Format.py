from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import *

class _Font():
    def __init__(self):
        self.english='宋体'
        self.chinese='宋体'
        self.bold=None
        self.italic=None
        self.size=Pt(10.5)
        self.color=RGBColor(0, 0, 0)
        self.highlight=None
        self.underline=None

class _Para():
    def __init__(self):
        self.alignment=WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        self.left_indent=None
        self.right_indent=None
        self.first_line_indent=None
        self.space_before=None
        self.space_after=None
        self.line_spacing=1

class Format():
    def __init__(self):
        self.font=_Font()
        self.para=_Para()

    def set_format(self,para):
        if len(para.runs)>1:
            run=para.runs[1]
        else:
            run=para.runs[0]

        run.font.name=self.font.english
        run.font.bold=self.font.bold
        run.font.italic=self.font.italic
        run.font.size=self.font.size
        run.font.color.rgb=self.font.color
        run.font.highlight_color=self.font.highlight

        para.alignment=self.para.alignment
        para.paragraph_format.left_indent=self.para.left_indent
        para.paragraph_format.right_indent=self.para.right_indent
        para.paragraph_format.first_line_indent=self.para.first_line_indent
        para.paragraph_format.space_before=self.para.space_before
        para.paragraph_format.space_after=self.para.space_after
        para.paragraph_format.line_spacing=self.para.line_spacing

        return para