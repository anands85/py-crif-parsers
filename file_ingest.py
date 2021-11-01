import pdfplumber
import json

class crif_report_extractor:

    def __init__(self, crif_report_extract_config):
        self.crif_report_extract_config = crif_report_extract_config
        self.pdf_file_path = self.crif_report_extract_config['report']['pdf_file_path']
        self.pdf_file_pwd = self.crif_report_extract_config['report']['pdf_file_pwd']

    def extract_obj_first_page(self):
        with pdfplumber.open(self.pdf_file_path,password='anan1889') as pdf:
            # Extract first page from the PDF document
            first_page = pdf.pages[0]
            # Collates all of the page's character objects into a single string.
            # Adds spaces where the difference between the x1 of one character and the x0 of the next is greater than x_tolerance.
            # Adds newline characters where the difference between the doctop of one character and the doctop of the next is greater than y_tolerance.
            first_page_text = first_page.extract_text(x_tolerance = crif_report_extract_config['report']['first_page']['text_settings']['x_tolerance'],
                                                      y_tolerance = crif_report_extract_config['report']['first_page']['text_settings']['y_tolerance'])
            print(first_page_text)
            #https://github.com/jsvine/pdfplumber#extracting-tables
            first_page_tables = first_page.extract_table(table_settings=self.crif_report_extract_config['report']['first_page']['table_settings'])
            count_tables = 1
            for table in first_page_tables:
                table_lines = table[0].split(r'\n')
                print("Table: ", count_tables)
                for line in table_lines:
                    print(line)
                count_tables += 1

###################################################
## JSON config file for extraction from CRIF report
###################################################
crif_report_extract_config = {
        "report":
            {
                "pdf_file_path": "/Users/as/IdeaProjects/crif_pdf_parser/Anand Srinivasan_CCR210901CR303006928.pdf",
                "pdf_file_pwd": "<first 4 letters of name +  last 4 digits mobile>",
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
                        'x_tolerance': 2,
                        'y_tolerance' : 2
                    },
                    "table_settings" : {
                        "vertical_strategy": "lines",
                        "horizontal_strategy": "lines",
                        "explicit_vertical_lines": [],
                        "explicit_horizontal_lines": [],
                        "snap_tolerance": 2,
                        "join_tolerance": 2,
                        "edge_min_length": 2,
                        "keep_blank_chars": True,
                        "intersection_tolerance": 2,
                        "intersection_x_tolerance": None,
                        "intersection_y_tolerance": None,
                    }
                }
            }
        }

###################################################
## Start Process
###################################################
anand_crif = crif_report_extractor(crif_report_extract_config)

###################################################
## Start Process
###################################################
anand_crif.extract_obj_first_page()


