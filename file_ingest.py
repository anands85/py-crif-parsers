import pdfplumber
import pandas as pd
import numpy as np

class crif_report_extractor:

    def __init__(self, crif_report_extract_config):
        self.crif_report_extract_config = crif_report_extract_config
        self.pdf_file_path = self.crif_report_extract_config['report']['pdf_file_path']
        self.pdf_file_pwd = self.crif_report_extract_config['report']['pdf_file_pwd']
        self.excel_file_path = self.crif_report_extract_config['report']['excel_file_path']
        self.process_success = True
        self.writer = pd.ExcelWriter(self.excel_file_path, engine='openpyxl')

    def table_array_to_df(self,table_array):
        self.process_success = True
        try:
            table_df = pd.DataFrame(table_array[1:],columns=table_array[0])
        except Exception as err:
            print(err)
            self.process_success = False
            table_df = pd.DataFrame()
        return self.process_success,table_df

    def table_df_to_sheet(self,table_df,excel_file,page_number,table_number):
        self.process_success = True
        try:
            table_df.to_excel(self.writer,sheet_name='Sht_'+str(page_number)+"_"+str(table_number))
            print("Page Number: ", page_number+1, "Table: ", table_number,'written to excel...')
        except Exception as err:
            print(err)
            self.process_success = False
        return self.process_success

    def extract_obj_first_page(self, pages):
        self.process_success = True
        try:
            with pdfplumber.open(self.pdf_file_path,password=self.pdf_file_pwd) as pdf:
                # Extract first page from the PDF document
                if pages == -1:
                    pages = len(pdf.pages)
                print("Number of pages processing...", pages)
                for page_number in range(pages):
                    first_page = pdf.pages[page_number]
                    first_page_tables = first_page.find_tables(table_settings=self.crif_report_extract_config['report']['first_page']['table_settings'])
                    count_tables = 1
                    for table in first_page_tables:
                        print("Page Number: ", page_number+1, "Table: ", count_tables)
                        self.process_success,table_df = self.table_array_to_df(table.extract())
                        if self.process_success:
                            self.process_success = self.table_df_to_sheet(table_df=table_df,
                                                                          excel_file=self.excel_file_path,
                                                                          page_number=page_number,
                                                                          table_number=count_tables)
                            if self.process_success:
                                count_tables += 1
                            else:
                                raise Exception("Table not saved in Excel")
                        else:
                            raise Exception("Tables not saved and Excel not created")
                self.writer.save()
                self.writer.close()
        except Exception as err:
            print(err)
            self.process_success = False
        return self.process_success


###################################################
## JSON config file for extraction from CRIF report
###################################################
crif_report_extract_config = {
        "report":
            {
                "pdf_file_path": "/Users/as/IdeaProjects/crif_pdf_parser/CCR210901CR303006928.pdf",
                "pdf_file_pwd": "XXXX1234",
                "first_page": {
                    'extract_inquiry_input_info': True,
                    'extract_crif_highmark_score': True,
                    'extract_crif_score_name': True,
                    'extract_crif_risk_desc': True,
                    'extract_name_variations_dates': True,
                    'extract_address_variations_dates': True,
                    'extract_name_variations_dates': True,
                    'extract_address_variations_dates': True,
                    'extract_email_variations_dates': True,
                    'extract_dob_variations_dates': True,
                    'extract_phone_variations_dates': True,
                    'extract_id_variations_dates': True,
                    'text_settings': {
                        'x_tolerance': 3,
                        'y_tolerance': 3
                    },
                    "table_settings": {
                        "text_x_tolerance": 3,
                        "text_y_tolerance": 3,
                        "intersection_x_tolerance": 3,
                        "intersection_y_tolerance": 3
                    }
                },
                "excel_file_path": "/Users/as/IdeaProjects/crif_pdf_parser/CCR210901CR303006928.xlsx"
            }
        }

###################################################
## Start Process
###################################################
doc_crif = crif_report_extractor(crif_report_extract_config)

###################################################
## Start Process
###################################################
doc_crif.extract_obj_first_page(-1)

print("############### End of Output for Document ############")
print("")
