import os
import json
from PIL import Image
from pypdf import PdfWriter
import glob

def create_pdfs(templates_folder, reports_folder):

#    out_filename = "misure.pdf"
    
    #read latex templates
    template_path_V = os.path.join(templates_folder, "template_ambientale_447_V.tex")
    with open (template_path_V, "r") as f:
        template_ambientale_V = f.read()

    template_path_H = os.path.join(templates_folder, "template_ambientale_447_H.tex")
    with open (template_path_H, "r") as f:
        template_ambientale_H = f.read()
    
    #---------------
    plots_folder = os.path.join(reports_folder, "plots")
    data_folder = os.path.join(reports_folder, "data")
    latex_folder = os.path.join(reports_folder, "latex")
    os.makedirs(latex_folder, exist_ok=True) 
    pdfs_folder = os.path.join(reports_folder, "pdfs")
    os.makedirs(pdfs_folder, exist_ok=True) 
    
    with open(os.path.join(data_folder, "latex_data.json"), 'r') as f:
        data = json.load(f)

    for item in data[:]:
        print("creating latex for:", item['filename'])

#        print(item)
        
        img = Image.open(item['fields']['-foto-'] + ".jpg")
#        img = Image.open("/".join(item['fields']['-foto-'].split("/")[2:]) + ".jpg")

        if img.size[0] > img.size[1]:
    #        print("H")
            report = template_ambientale_H
            item['fields']['-foto-H'] = item['fields'].pop("-foto-")
        else:
            report = template_ambientale_V
            item['fields']['-foto-V'] = item['fields'].pop("-foto-")

        for field_k, field_v in item['fields'].items():
    #        print(field_k, field_v)
            report = report.replace(field_k, str(field_v))#.replace("_", "\_")

        latex_file = os.path.join(latex_folder, item['filename'].replace(".xlsx", ".tex"))
        
        with open (latex_file, "w") as f:
            f.write(report)

#        print(pdfs_folder)
        
        command = r"pdflatex -output-directory=" + pdfs_folder + " '" + latex_file + "'" 
#        print(command)       
#        print(latex_file)
        
#        os.system(command)
        os.system(command  + "> /dev/null 2>&1")

    #remove .log and .aux files
    for remove_path in glob.iglob(os.path.join(pdfs_folder, '*.log')):
        os.remove(remove_path)
    for remove_path in glob.iglob(os.path.join(pdfs_folder, '*.aux')):
        os.remove(remove_path)
    
    print("- all latex files created")

def merge_pdfs(reports_folder, out_filename = "misure.pdf"):
    
    pdfs_folder = os.path.join(reports_folder, "pdfs")

#    pdf_filenames = sorted([x for x in os.listdir(pdfs_folder) if x.endswith(".pdf")])

    pdf_filenames = [os.path.join(pdfs_folder, x) for x in os.listdir(pdfs_folder) if x.endswith(".pdf")]
    pdf_filenames.sort(key=lambda x: os.path.getmtime(x))
    pdf_filenames = [x.split("/")[-1] for x in pdf_filenames]

    merger = PdfWriter()

    for pdf_filename in pdf_filenames:
        print("merging", pdf_filename)
        pdf_path = os.path.join(pdfs_folder, pdf_filename)
        merger.append(pdf_path)

    merger.write(os.path.join(reports_folder, out_filename))
    merger.close()
    
    print("- all pdf merged")
    
#    return