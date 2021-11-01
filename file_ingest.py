import pdfplumber

class crif_report_extractor:

    def __init__(self, crif_report_extract_config):
        self.crif_report_extract_config = crif_report_extract_config
        self.pdf_file_path = self.crif_report_extract_config['report']['pdf_file_path']
        self.pdf_file_pwd = self.crif_report_extract_config['report']['pdf_file_pwd']

    def extract_obj_first_page(self, pages):
        with pdfplumber.open(self.pdf_file_path,password=self.pdf_file_pwd) as pdf:
            # Extract first page from the PDF document
            for page_number in range(pages):
                print("Page Number: ", page_number+1)
                first_page = pdf.pages[page_number]
                # Collates all of the page's character objects into a single string.
                # Adds spaces where the difference between the x1 of one character and the x0 of the next is greater than x_tolerance.
                # Adds newline characters where the difference between the doctop of one character and the doctop of the next is greater than y_tolerance.
                #https://github.com/jsvine/pdfplumber#extracting-tables
                #brew install freetype imagemagick
                #brew install gs
                first_page_tables = first_page.find_tables(table_settings=self.crif_report_extract_config['report']['first_page']['table_settings'])
                #im.reset().draw_rects(first_page.chars)
                #first_page_text = first_page.extract_text(x_tolerance = crif_report_extract_config['report']['first_page']['text_settings']['x_tolerance'],
                #                                          y_tolerance = crif_report_extract_config['report']['first_page']['text_settings']['y_tolerance'])
                #print(first_page_text)
                #first_page_tables = first_page.extract_table(table_settings=self.crif_report_extract_config['report']['first_page']['table_settings'])
                count_tables = 1
                for table in first_page_tables:
                    #table_lines = table[0].split(r'\n')
                    print("Table: ", count_tables)
                    print(table.extract())
                    #for line in table_lines:
                    #    print(line)
                    count_tables += 1


###################################################
## JSON config file for extraction from sample table document
###################################################
crif_report_extract_config = {
    "report":
        {
            "pdf_file_path": "/Users/as/IdeaProjects/crif_pdf_parser/test-side-by-side-tables.pdf",
            "pdf_file_pwd": None,
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
            }
        }
}

###################################################
## Start Process
###################################################
sample_tabular = crif_report_extractor(crif_report_extract_config)

###################################################
## Start Process
###################################################
sample_tabular.extract_obj_first_page(1)

print("############### End of Output for Document ############")
print("")
###################################################
## JSON config file for extraction from CRIF report
###################################################
crif_report_extract_config = {
    "report":
        {
            "pdf_file_path": "/Users/as/IdeaProjects/crif_pdf_parser/typical-tables.pdf",
            "pdf_file_pwd": None,
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
            }
        }
}

###################################################
## Start Process
###################################################
sample_tabular = crif_report_extractor(crif_report_extract_config)

###################################################
## Start Process
###################################################
sample_tabular.extract_obj_first_page(1)

print("############### End of Output for Document ############")
print("")
###################################################
## JSON config file for extraction from CRIF report
###################################################
crif_report_extract_config = {
        "report":
            {
                "pdf_file_path": "/Users/as/IdeaProjects/crif_pdf_parser/CCR210901CR303006928.pdf",
                "pdf_file_pwd": "anan1889",
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
anand_crif.extract_obj_first_page(2)

print("############### End of Output for Document ############")
print("")
