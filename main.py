import sys
from PyPDF2 import PdfReader, PdfWriter

def main(pdf_path: str):
  u_password = input("Choose user password for pdf file > ")
  o_password = input("Choose owner password for pdf file > ")
  path, filename = pdf_path.rsplit("\\", 1)
  filename = filename.removesuffix(".pdf")

  pdf_read = PdfReader(pdf_path)
  pdf_write = PdfWriter()

  for page in pdf_read.pages:
      pdf_write.add_page(page)

  pdf_write.encrypt(user_password=u_password,owner_password=o_password)
  pdf_write.write(f"{path}\\encrypted_{filename}.pdf")

if __name__ == '__main__':
  main(sys.argv[1])