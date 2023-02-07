import argparse
from pathlib import Path

from openpyxl.reader import excel

if __name__ == '__main__':

    # parse command-line arguments using argparse
    parser = argparse.ArgumentParser(
        prog='xlscan',
        description='output info of an xl file'
    )
    parser.add_argument(
        'xl_file',
        metavar='xl_file',
        nargs=1,
        help='A path to your xl file'
    )
    args = parser.parse_args()
    xl_file_path = Path(args.xl_file[0])
    xl_file_name = xl_file_path.name

    # open xl workbook
    xl_workbook = excel.load_workbook(
        filename=xl_file_path,
        read_only=True,
        keep_links=False
    )

    # get names of the workbook
    worksheet_names = xl_workbook.sheetnames

    # output the file name and worksheet names
    for worksheet_name in worksheet_names:
        print(f'{xl_file_name}, {worksheet_name}')
