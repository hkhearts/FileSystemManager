from docxtpl import DocxTemplate

template_path = "tempdoc.docx"
doc = DocxTemplate(template_path)

name = input("Enter your name: ")
dept = input("Enter your department: ")

context = {
    'name': name,
    'dept': dept
}

doc.render(context)

output_path = "output.docx"
doc.save(output_path)

print(f"Document saved as {output_path}")