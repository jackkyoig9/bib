"""
--------------------------------------------------------------------------------
FILE NAME:  extract_sql_bib.py
DATE:       190314(Thu)
SYNOPSIS:   python3 extract_sql_bib.py [original_file_name]
DESCRIPTION:
성경 파일을 불러들여 DB에 저장할 수 있는 sql생성
HISTORY:
190405: 파일 이름 바꿈 scr_div_data_from_bib.py => extract_sql_bib.py
190405: str_savefile_name 추가
--------------------------------------------------------------------------------
"""

import sys

str_please = "파일을 입력해주세요.\n"
str_use = "USE:\\extract_sql_data_bib.py [file_name]\n"
# str_savefile_name = "bib_kHRV"  # 190405
str_savefile_name = "bib_eNIV2011"  # 190405

# 공식문서
# The Python Tutotial
# 7. Input and Output
# For reading lines from a file, you can loop over the file object.
# This is memory efficient, fast, and leads to simple code:


def readfile(fname):
    with open(fname) as f:
        for line in f:
            print(line, end='')
    f.closed


def readmyfile(fname):
    line_num = 0
    insert_bib = ""
    with open(fname) as f:
        for line in f:
            line_num += 1
            # bib00_eNIV2011.sql
            # bib00_kNKRV.sql
            # bib01_eNIV2011.sql
            # if len(line) > 5 and line_num < 1535:
            # bib02_eNIV2011.sql
            # if len(line) > 5 and (line_num >= 1535 and line_num < 2749):
            # 간단히 테스트
            # if len(line) > 5 and line_num < 10:
            if len(line) > 5:
                # print(line[:-1].split(" ", 2))
                # 마지막은 줄바꿈 \n이 들어있음
                bib_line = line[:-1].split(" ", 2)

                # bib index
                str_id = bib_line[0][0:2]
                str_index = bib_line[0][2:]
                # bib chapter 01, 02
                bib_ch = bib_line[1].split(":")
                str_ch01 = bib_ch[0]
                str_ch02 = bib_ch[1]
                # bib content
                bib_content = bib_line[2]

                # str_ch01 과 str_ch02로 붙여놓으면 구분이 어려움
                str_bib_id = str_id + str_index + bib_line[1]

                # insert_bib += "insert into bib_niv2011 (bib_id, id, idx, ch01, ch02, content) "\
                insert_bib += "insert into {0:s} (bib_id, id, idx, ch01, ch02, content) "\
                    "values ('{1:s}', '{2:s}', '{3:s}', {4:s}, {5:s}, '{6:s}');\n".format(
                        str_savefile_name,
                        str_bib_id, str_id, str_index, str_ch01, str_ch02, bib_content)

        # print(line_num)
        # print(insert_bib)
    f.closed
    return insert_bib


def getparam():
    arg1 = ""
    try:
        arg1 = sys.argv[1]
    except IndexError:
        pass
    return arg1


def writemyfile(fname, val):
    f = open(fname, "w")
    f.write(val)
    f.close()


# main
str_file = ""
try:
    str_file = readmyfile(getparam())
except FileNotFoundError as e:
    print(str_please + str_use)

# 파일 만들기
# 작은 파일은 한번에 가능하겠지만 큰 파일은 문제가 될 수 있음(문제 없었음)
# writemyfile("bib_line_num.txt", str_file)
# writemyfile("bib00_eNIV2011.sql", str_file)
# writemyfile("bib_kNKRV.sql", str_file)
writemyfile("{0:s}.sql".format(str_savefile_name), str_file)  # 190405


'''
# test file
/Users/iki/Downloads/dev/python/doc/sqlite_for_python_190131.txt
./../doc/sqlite_for_python_190131.txt
'''

'''
# bib
/Users/iki/Downloads/vm_downloads/01_edu/99_bib
/Users/iki/Downloads/vm_downloads/01_edu/99_bib/eNIV1984.btx
/Users/iki/Downloads/vm_downloads/01_edu/99_bib/eNIV2011.btx
/Users/iki/Downloads/vm_downloads/01_edu/99_bib/kNKRV.btx
'''

'''
# splie(string, number)
str_title = "Python Programming Tutorial Example"
print(str_title.split())
print(str_title.split(' ', 2))
'''
