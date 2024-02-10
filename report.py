import webbrowser
import os

from filestack import Client
from fpdf import FPDF

class PdfReport:
  """
  Creates pdf reports for flatmates
  """
  def __init__(self, filename):
    self.filename = filename

  def generate(self, flatmate1, flatmate2, bill):
    flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
    flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))
    
    pdf = FPDF(orientation = 'P', unit = 'pt', format = 'A4')
    pdf.add_page()

    pdf.image("files/house.jpg", w = '30', h = '30')

    pdf.set_font(family='Times', size=24, style='B')
    pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

    pdf.set_font(family="Times", size=14, style='B')
    pdf.cell(w=100, h=40, txt="Period:", border=0)
    pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

      # Insert name and due amount of the first flatmate
    pdf.set_font(family="Times", size=12)
    pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
    pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

      # Insert name and due amount of the second flatmate
    pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
    pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

    oschdir("files")
    pdf.output(self.filename)
    webbrowser.open(self.filename)

class FileSharer:
  """
  Adding pdf file to cdn
  """
  def __init__(self, filepath, api_key = "Insert your apikey here"):
    self.filepath = filepath
    self.api_key = apikey

  def share(self):
    client = Client(self.api_key)
    new_filelink = client.upload(filepath = self.filepath)
    return new_filelink

    
