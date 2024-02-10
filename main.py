from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

amount = float(input("Enter the bill amount: ")
period = input("Enter the period for which bill needs to be paid : eg Dec, 2023")

name1 = input("What is your name ? ")
days_in_house1 = int(input(f"How many days {name1} staye in house during bill period? "))
name2 = input("What is your name ? ")
days_in_house2 = int(input(f"How many days {name2} staye in house during bill period? "))

the_bill = Bill(amount, period)

flatmate1 = Flatmates(name1, days_in_house1)
flatmate2 = Flatmates(name2, days_in_house2)

printf(f"{flatmate1.name} pays: ", flatemate1.pays(the_bill, flatmate2))
printf(f"{flatmate2.name} pays: ", flatemate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename = f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileSharer(filepath = pdf_report.filename)
print(file_sharer.share())
