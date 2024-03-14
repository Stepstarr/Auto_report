from docx.shared import *

from report_format.Format import Format
from report_format.output import output

content={'heading1':'hsiugfsuhfuh','heading2':'wqoiryewiuyriqu'}
f=Format()
f.font.size=Pt(18)
f.para.left_indent=Cm(1.5)
name='test1'
output(content,f,name)