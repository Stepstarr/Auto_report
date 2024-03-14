from docx import Document

from report_format.format_get import sep_paras

paragraph=Document().add_paragraph("哈对佛胡啥时候哈市发货啦还是为何也很多asdfghjk山东科技服务呵呵奥胡发的死啊里弗斯")
for run in sep_paras(paragraph,'asdfghjk').runs:
    print(run.text)