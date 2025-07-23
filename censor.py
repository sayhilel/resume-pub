import re
import subprocess

def censor(input_file, output_file):
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    with open(input_file, 'r') as file:
        content = file.read()
    content = re.sub(phone_pattern, 'xxx-xxx-xxxx', content)
    with open(output_file, 'w') as file:
        file.write(content)


censor("./original/Sahil_Sinha_Resume.tex", "Sahil_Sinha_Resume_Pub.tex")
subprocess.run(["pdflatex", "Sahil_Sinha_Resume_Pub.tex"])
subprocess.run(["rm", "-f", "Sahil_Sinha_Resume_Pub.aux",  "Sahil_Sinha_Resume_Pub.log",  "Sahil_Sinha_Resume_Pub.out", "Sahil_Sinha_Resume_Pub.tex"])
subprocess.run(["mv", "Sahil_Sinha_Resume_Pub.pdf", "pub/"])
