"""
--------------------------------------------------------------------------------
FILE NAME:  scr_json_data_bib.py
DATE:       190318(Mon)
HISTORY:    20200108(Wed) eKJV(킹제임스) 생성, 주석 수정
SYNOPSIS:   scr_json_data_bib.py [original_bible_file_name]
DESCRIPTION: 성경 파일을 읽고 분석해서 ./json/만든 폴더에 모든 json형식의 파일을 생성

# 진행순서 190909(Mon)
1. 현재폴더 확인
/Users/iki/Downloads/dev/python/lib_py/script_bib

2. original_bib_file 에 원본파일 확인(from /Users/iki/Downloads/vm_downloads/01_edu/99_bib)
eKJV.btx # 20200108(Wed) KJS(킹제임스)
kNKRV.btx

3. bib_name 를 정함
bib_name = "eKJV"  # 20200108(Wed) KJS(킹제임스)
bib_name = "kNKRV"  # 개역개정판

4. .json 아래에 폴더 생성하기
/Users/iki/Downloads/dev/python/lib_py/script_bib/json
mkdir kNKRV_bib

5. run & save the log
# 20200108(Wed) 실행 & 로그 저장
iki script_bib $ python3 scr_json_data_bib.py ./original_bib_file/eKJV.btx > ./log/log_json_eKJV.txt
#
iki script_bib $ python3 scr_json_data_bib.py ./original_bib_file/kNKRV.btx > ./log/log_json_kNKRV.txt
--------------------------------------------------------------------------------
"""

import sys

str_please = "파일을 입력해주세요.\n"
str_use = "USE:\tscr_json_data_bib.py [original_bible_file_name]\n"

'''
def readfile(fname):  # 파일 읽기 기본 구조
    with open(fname) as f:
        for line in f:
            print(line, end='')
    f.closed
'''


def readmyfile(fname, book):
    line_num = 0  # Check the line number
    made_line_num = 0  # Check the made line number
    insert_bib = "[\n"  # Save file
    with open(fname) as f:
        for line in f:
            line_num += 1
            # 간단히 테스트
            # if len(line) < 5: # Print book number of start
            # Print only 5 line(test)
            # if (len(line) > 5 and line_num < 7) and line[0:2] == "01": # Genesis
            # New Testament
            # Matthew
            # if (len(line) > 5 and made_line_num < 5) and line[0:2] == "41":
            # if (len(line) > 5 and made_line_num < 5) and line[0:2] == "41": # Mark
            # len(line) => Avoid header of book, line[0:2] => Check the number of book
            # if len(line) > 5 and line[0:2] == "01":  # Genesis
            # if len(line) > 5 and line[0:2] == "40":  # Matthew
            # if len(line) > 5 and line[0:2] == "41":  # Mark
            if len(line) > 5 and line[0:2] == book:  # Luke
                made_line_num += 1  # Count the made line number
                # print(line)  # Print line from the original file(test)
                # Split before the content(many space in content)
                bib_list = line[:-1].split(" ", 2)
                # Save file
                insert_bib += "{" + '"bib_name":"{0:s}", "bib_chapter":"{1:s}", '\
                    '"bib_content":"{2:s}"'.format(
                        bib_list[0], bib_list[1], bib_list[2]) + "},\n"
        # Delete last two character in save file ",\n"
        result_bib = insert_bib[:-2] + "\n]"
        # print(result_bib)  # Print result(test)
        print("made line num:", made_line_num)  # Print total line
    f.closed
    return result_bib


def getparam():  # 파일이 있는지 확인
    arg1 = ""
    try:
        arg1 = sys.argv[1]
    except IndexError:
        pass
    return arg1


def writemyfile(fname, val):  # 파일에 저장
    f = open(fname, "w")
    f.write(val)
    f.close()


# 190324(Sun) 파일 내의 book(66)을 확인하고 book별로 파일을 만들어 저장함.
# main
str_file = ""
bib_name = "eKJV"  # KJV # 20200108(Wed) 추가
# bib_name = "kNKRV"  # 개역개정판 190909(Mon)
# bib_name = "eNIV2011"  # NIV 190324(Sun)
# bib_name = "kHRV"  # 개역한글판 190324(Sun)

# 성경은 총66개로 구성되어있음, 01~66 (Old:39, New:27)
# book = "41"
for i in range(66):
    book = "%02d" % (i+1)
    # print(book, end=" ")
    try:
        str_file = readmyfile(getparam(), book)
    except FileNotFoundError as e:
        print(str_please + str_use)

    # print("만들 파일 이름: ./json/{0:s}_bib{1:s}.json".format(bib_name, book))
    # writemyfile("./json/kHRV_bib{s}.json".format(chapter), str_file)  # 190324(Sun)
    print("만들 파일 이름: ./json/%s_bib/%s_bib%s.json" % (bib_name, bib_name, book))
    writemyfile("./json/%s_bib/%s_bib%s.json" %
                (bib_name, bib_name, book), str_file)


'''
# main
str_file = ""
# bib_name = "eNIV2011" # NIV
bib_name = "kHRV"  # 개역한글판
# 01~66 (Old:39, New:27)
book = "41"

try:
    str_file = readmyfile(getparam(), book)
except FileNotFoundError as e:
    print(str_please + str_use)

# print("만들 파일 이름: ./json/{0:s}_bib{1:s}.json".format(bib_name, book))
print("만들 파일 이름: ./json/%s_bib%s.json" % (bib_name, book))
# writemyfile("./json/kHRV_bib{s}.json".format(chapter), str_file)  # 190324(Sun)
'''

# 파일 이름을 정하고 만들기 | Make the file
# 작은 파일은 한번에 가능하겠지만 큰 파일은 문제가 될 수 있음(문제 없었음)
# writemyfile("bib_line_num.txt", str_file)
# sql
# writemyfile("bib00_eNIV2011.sql", str_file)
# writemyfile("bib00_kNKRV.sql", str_file)
# json
# writemyfile("./json/eNIV2011_bib01.json", str_file) # 190319(Tue)
# writemyfile("./json/kNKRV_bib01.json", str_file) # 190321(Thu)
# writemyfile("./json/eNIV2011_bib40.json", str_file)  # 190322(Fri)
# writemyfile("./json/kNKRV_bib40.json", str_file)  # 190322(Fri)
# writemyfile("./json/eNIV2011_bib41.json", str_file)  # 190323(Sat)
# writemyfile("./json/kNKRV_bib41.json", str_file)  # 190323(Sat)
# writemyfile("./json/eNIV2011_bib42.json", str_file)  # 190324(Sun)
# writemyfile("./json/kNKRV_bib42.json", str_file)  # 190324(Sun)

# writemyfile("./json/kHRV_bib01.json", str_file)  # 190324(Sun)
# writemyfile("./json/kHRV_bib40.json", str_file)  # 190324(Sun)
# writemyfile("./json/kHRV_bib41.json", str_file)  # 190324(Sun)
# writemyfile("./json/kHRV_bib42.json", str_file)  # 190324(Sun)


'''
# test file
/Users/iki/Downloads/dev/python/doc/sqlite_for_python_190131.txt
./../doc/sqlite_for_python_190131.txt
'''

'''
# bib: 파일을 읽을때 사용할 경로
/Users/iki/Downloads/vm_downloads/01_edu/99_bib
/Users/iki/Downloads/vm_downloads/01_edu/99_bib/eNIV1984.btx
/Users/iki/Downloads/vm_downloads/01_edu/99_bib/eNIV2011.btx
/Users/iki/Downloads/vm_downloads/01_edu/99_bib/kNKRV.btx # 개역개정판 
/Users/iki/Downloads/dev/python/lib_py/scr_bib/original_bib_file/kHRV.btx # 개역한글판
/Users/iki/Downloads/dev/python/lib_py/scr_bib/original_bib_file/eNIV2011.btx # NIV
'''

'''
# for문
for i in range(10):
    print(i, end='')
# Result: 0123456789
'''
