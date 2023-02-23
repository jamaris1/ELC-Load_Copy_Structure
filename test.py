
import csv
import os
import time
import gzip
import shutil



from metadata.merch_iri_pos_transfers_1 import sql as sql_iri_pos_transfers
from metadata.merch_trans_activity_1 import sql as sql_trans_activity
from metadata.merch_iro_pos_trfrouts_1 import sql as sql_iro_pos_trfrouts
from metadata.merch_iro_pos_requests_1 import sql as sql_iro_pos_requests
from metadata.merch_transfers_1 import sql as sql_transfers

from metadata.merch_trans_activity_2 import merge as merge_trans_activity
from metadata.merch_iro_pos_trfrouts_2 import merge as merge_iro_pos_trfrouts
from metadata.merch_iro_pos_requests_2 import merge as merge_iro_pos_requests
from metadata.merch_transfers_2 import merge as merge_transfers
from metadata.merch_iri_pos_transfers_2 import merge as merge_iri_pos_transfers


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

if __name__ == '__main__':
    filess = {}
    files = my_dictionary()
    merge_sql = {}

    savePath = 'C:\\Users\\jamaris\\PycharmProjects\\simple_tests\\data_files'

    if not os.path.exists(savePath):
        os.makedirs(savePath)

    thisdate = time.strftime("%d-%m-%Y")
    thistime = time.strftime("%H-%M-%S")
    exporttime = time.strftime("%H:%M:%S")

    tables = {
        "merch_iri_pos_transfers": sql_iri_pos_transfers,
        "merch_trans_activity": sql_trans_activity,
        "merch_iro_pos_trfrouts": sql_iro_pos_trfrouts,
        "merch_iro_pos_requests": sql_iro_pos_requests,
        "merch_transfers": sql_transfers
    }

    for table_name, table_sql in tables.items():
        #print(table_name,table_sql)

        sql = table_sql

        # output each table content to a separate CSV file
        fileName = table_name + "_" + thisdate + "_" + thistime + ".csv"

        # Create the complete filename including the absolute path
        csv_file_dest = os.path.join(savePath, fileName)

        outputFile = open(csv_file_dest, 'w', newline='',
                          errors='ignore')  # 'wb'  ,errors='ignore'  , encoding="utf8"
        output = csv.writer(outputFile, dialect='excel')
        output.writerow("cols")

        outputFile.close()


        # archive the file
        with open(csv_file_dest, 'rb') as f_in:
            with gzip.open(os.path.join(savePath, fileName + '.gz'), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(table_name)
        print(fileName)
        # add file name to files dictionary
        files.key = input(table_name)
        files.value = input(fileName)

        files.add(files.key, files.value)


        print('Step 2')

        for table_name, file_name in files.items():
            print("""Put file://{v_path}{v_sf_stage}""".format(v_path=file_name,
                                                                  v_sf_stage=" @" + sf_stage_name))
        '''
        # delete the csv file
        #os.remove(csv_file_dest)
        '''