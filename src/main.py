import Jobsearch as apply
from openpyxl import load_workbook
import sys, os
# 
def applyFive():
   keyword = " Cybersecurity AND RecentGrad"
   roles = apply.GetCareerSites(keyword)
   apply.OpenSites(list(roles.values()))
   apply.OpenSites(["https://app.tealhq.com/home"],1)

if __name__ == "__main__":
   #applyFive()
   data_file =  "..\\..\\Job Search Spring 2023.xlsx"
   wb = load_workbook(data_file)
   Company_ws = wb['Companies']
   company_rows = list(Company_ws.rows)
   print(cells[0].value for cells in company_rows[1:10])