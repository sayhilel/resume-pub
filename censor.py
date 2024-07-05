import re
import subprocess

def censor(input_file, output_file):
    phone_pattern = r'\(\d{3}\)\s*\d{3}-\d{4}'
    with open(input_file, 'r') as file:
        content = file.read()
    content = re.sub(phone_pattern, 'CENSORED', content)
    with open(output_file, 'w') as file:
        file.write(content)


censor("resume.tex", "resume_pub.tex")
subprocess.run(["pdflatex", "resume_pub.tex"])
subprocess.run(["rm", "-f", "resume_pub.aux",  "resume_pub.log",  "resume_pub.out", "resume_pub.tex"])
subprocess.run(["mv", "resume_pub.pdf", "docs/"])
