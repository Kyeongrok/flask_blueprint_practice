import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import sqlalchemy
from libs.FileManager import FileManager

class DbInit():
    fm = FileManager()

    def __init__(self, db_uri, csv_file_dir):
        self.engine = create_engine(db_uri)
        self.csv_file_dir = csv_file_dir


    def insert_person(self):
        df = pd.read_csv('{}/person.csv'.format(self.csv_file_dir))
        df.to_sql(con=self.engine, name='person', index=False, dtype={
            'person_id':sqlalchemy.types.BIGINT(),
            'gender_concept_id':sqlalchemy.types.INTEGER(),
            'year_of_birth':sqlalchemy.types.INTEGER(),
            'month_of_birth':sqlalchemy.types.INTEGER(),
            'day_of_birth':sqlalchemy.types.INTEGER(),
            'birth_datetime':sqlalchemy.DateTime(),
            'race_concept_id':sqlalchemy.types.INTEGER(),
            'ethnicity_concept_id':sqlalchemy.types.INTEGER(),
            'location_id':sqlalchemy.types.INTEGER(),
            'provider_id':sqlalchemy.types.INTEGER(),
            'care_site_id':sqlalchemy.types.INTEGER(),
            'person_source_value':sqlalchemy.types.VARCHAR(length=255),
            'gender_source_value':sqlalchemy.types.VARCHAR(length=255),
            'gender_source_concept_id':sqlalchemy.types.INTEGER(),
            'race_source_value':sqlalchemy.types.VARCHAR(length=50),
            'race_source_concept_id':sqlalchemy.types.INTEGER(),
            'ethnicity_source_value':sqlalchemy.types.VARCHAR(length=50),
            'ethnicity_source_concept_id':sqlalchemy.types.INTEGER()})

        with self.engine.connect() as con:
            con.execute('ALTER TABLE person ADD PRIMARY KEY (person_id);')

    def insert_visit_occurrence(self):
        df = pd.read_csv('{}/visit_occurrence.csv'.format(self.csv_file_dir))
        df.to_sql(con=self.engine, name='visit_occurrence', index=False, dtype={
            'visit_occurrence_id':sqlalchemy.types.BIGINT(),
            'person_id':sqlalchemy.types.INTEGER(),
            'visit_concept_id':sqlalchemy.types.INTEGER(),
            'visit_start_date':sqlalchemy.types.DATE(),
            'visit_start_datetime':sqlalchemy.types.DateTime(),
            'visit_end_date':sqlalchemy.types.DATE(),
            'visit_end_datetime':sqlalchemy.types.DateTime(),
            'visit_type_concept_id':sqlalchemy.types.INTEGER(),
            'provider_id':sqlalchemy.types.INTEGER(),
            'care_site_id':sqlalchemy.types.INTEGER(),
            'visit_source_value':sqlalchemy.types.VARCHAR(length=50),
            'visit_source_concept_id':sqlalchemy.types.INTEGER(),
            'admitting_source_concept_id':sqlalchemy.types.INTEGER(),
            'admitting_source_value':sqlalchemy.types.INTEGER(),
            'discharge_to_concept_id':sqlalchemy.types.INTEGER(),
            'discharge_to_source_value':sqlalchemy.types.INTEGER(),
            'preceding_visit_occurrence_id':sqlalchemy.types.INTEGER(),})
        with self.engine.connect() as con:
            con.execute('ALTER TABLE visit_occurrence ADD PRIMARY KEY (visit_occurrence_id);')
        print(df.columns)


    def condition_occurrence(self):
        df = pd.read_csv('{}/condition_occurrence.csv'.format(self.csv_file_dir))
        df.to_sql(con=self.engine, name='condition_occurrence', index=False, dtype={
            'condition_occurrence_id':sqlalchemy.types.INTEGER(),
            'person_id':sqlalchemy.types.INTEGER(),
            'condition_concept_id':sqlalchemy.types.INTEGER(),
            'condition_start_date':sqlalchemy.types.INTEGER(),
            'condition_start_datetime':sqlalchemy.types.INTEGER(),
            'condition_end_date':sqlalchemy.types.INTEGER(),
            'condition_end_datetime':sqlalchemy.types.INTEGER(),
            'condition_type_concept_id':sqlalchemy.types.INTEGER(),
            'stop_reason':sqlalchemy.types.INTEGER(),
            'provider_id':sqlalchemy.types.INTEGER(),
            'visit_occurrence_id':sqlalchemy.types.INTEGER(),
            'visit_detail_id':sqlalchemy.types.INTEGER(),
            'condition_source_value':sqlalchemy.types.INTEGER(),
            'condition_source_concept_id':sqlalchemy.types.INTEGER(),
            'condition_status_source_value':sqlalchemy.types.INTEGER(),
            'condition_status_concept_id':sqlalchemy.types.INTEGER(),
        })
        with self.engine.connect() as con:
            con.execute('ALTER TABLE condition_occurrence ADD PRIMARY KEY (condition_occurrence_id);')
        print(df.columns)

    def drug_exposure(self):
        df = pd.read_csv('{}/drug_exposure.csv'.format(self.csv_file_dir))
        df.to_sql(con=self.engine, name='drug_exposure', index=False, dtype={
            'drug_exposure_id':sqlalchemy.types.INTEGER(),
            'person_id':sqlalchemy.types.INTEGER(),
            'drug_concept_id':sqlalchemy.types.INTEGER(),
            'drug_exposure_start_date':sqlalchemy.types.INTEGER(),
            'drug_exposure_start_datetime':sqlalchemy.types.INTEGER(),
            'drug_exposure_end_date':sqlalchemy.types.INTEGER(),
            'drug_exposure_end_datetime':sqlalchemy.types.INTEGER(),
            'verbatim_end_date':sqlalchemy.types.INTEGER(),
            'drug_type_concept_id':sqlalchemy.types.INTEGER(),
            'stop_reason':sqlalchemy.types.INTEGER(),
            'refills':sqlalchemy.types.INTEGER(),
            'quantity':sqlalchemy.types.INTEGER(),
            'days_supply':sqlalchemy.types.INTEGER(),
            'sig':sqlalchemy.types.INTEGER(),
            'route_concept_id':sqlalchemy.types.INTEGER(),
            'lot_number':sqlalchemy.types.INTEGER(),
            'provider_id':sqlalchemy.types.INTEGER(),
            'visit_occurrence_id':sqlalchemy.types.INTEGER(),
            'visit_detail_id':sqlalchemy.types.INTEGER(),
            'drug_source_value':sqlalchemy.types.INTEGER(),
            'drug_source_concept_id':sqlalchemy.types.INTEGER(),
            'route_source_value':sqlalchemy.types.INTEGER(),
            'dose_unit_source_value':sqlalchemy.types.INTEGER(),
        })
        with self.engine.connect() as con:
            con.execute('ALTER TABLE drug_exposure ADD PRIMARY KEY (drug_exposure_id);')
        print(df.columns)
    def concept(self):
        # 먼저 큰 파일을 n개로 나눈다.

        file_list = self.fm.get_file_list('./separated/*.csv')
        if len(file_list) == 0:
            self.fm.csv_separate_files('{}/concept.csv'.format(self.csv_file_dir), file_cnt=50)
            file_list = self.fm.get_file_list('./separated/*.csv')
        for filename in file_list:
            df = pd.read_csv(filename)
            df.to_sql(con=self.engine, name='concept', index=False, if_exists='append', dtype={
                'concept_id':sqlalchemy.types.INTEGER(),
                'concept_name':sqlalchemy.types.VARCHAR(length=255),
                'domain_id':sqlalchemy.types.VARCHAR(length=50),
                'vocabulary_id':sqlalchemy.types.VARCHAR(length=50),
                'concept_class_id':sqlalchemy.types.VARCHAR(length=50),
                'standard_concept':sqlalchemy.types.VARCHAR(length=20),
                'concept_code':sqlalchemy.types.INTEGER(),
                'valid_start_date':sqlalchemy.types.Date(),
                'valid_end_date':sqlalchemy.types.Date(),
                'invalid_reason':sqlalchemy.types.VARCHAR(length=20)
            })
            print('{}/{} finished'.format(filename, len(file_list)))
        with self.engine.connect() as con:
            con.execute('ALTER TABLE concept ADD PRIMARY KEY (concept_id);')
            # print(df.columns)

    def death(self):
        df = pd.read_csv('{}/death.csv'.format(self.csv_file_dir))
        df.to_sql(con=self.engine, name='death', index=False, dtype={
            'person_id':sqlalchemy.types.INTEGER(),
            'death_date':sqlalchemy.types.Date(),
            'death_datetime':sqlalchemy.types.DateTime(),
            'death_type_concept_id':sqlalchemy.types.INTEGER(),
            'cause_concept_id':sqlalchemy.types.INTEGER(),
            'cause_source_value':sqlalchemy.types.INTEGER(),
            'cause_source_concept_id':sqlalchemy.types.INTEGER()
        })
        with self.engine.connect() as con:
            con.execute('ALTER TABLE death ADD PRIMARY KEY (person_id);')

        print(df.columns)
'''

'''
user_id = 'root'
password = '12345678'
synthea_cdm_csv_location = 'C:/Users/ocean/Desktop/synthea_cdm_csv/'
dbi = DbInit('postgresql://{}:{}@127.0.0.1:5432/postgres'.format(user_id,password), synthea_cdm_csv_location)
dbi.insert_visit_occurrence()
# dbi.concept()
# dbi.death()

