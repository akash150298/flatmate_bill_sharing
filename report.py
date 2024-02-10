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

    
