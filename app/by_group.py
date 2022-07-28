import xlwt
from appearance import create_dict

wb = xlwt.Workbook()
gen = wb.add_sheet('Genesis')
exo = wb.add_sheet('Exodus')
lev = wb.add_sheet('Leviticus')
num = wb.add_sheet('Numbers')
deu = wb.add_sheet('Deuteronamy')
est = wb.add_sheet('Esther')
shi = wb.add_sheet('Shir Hashirim')



def by_group(script, sheet):
    letters = create_dict(script)
    column = 1
    for key in letters:
        row = 1
        for entry in letters[key]:
            sheet.write(row, column, label=entry)
            row += 1
        sheet.write(0, column, label=key)
        column += 1
    

# by_group('..\processed_text\Chumash\Genesis.txt', gen)
# by_group('..\processed_text\Chumash\Exodus.txt', exo)
# by_group('..\processed_text\Chumash\Leviticus.txt', lev)
# by_group(r'..\processed_text\Chumash\Numbers.txt', num)
# by_group('..\processed_text\Chumash\Deuteronomy.txt', deu)
# by_group('..\processed_text\Megillah\Esther.txt', est)
# by_group('..\processed_text\Megillah\Shir_Hashirim.txt', shi)
# wb.save('Letter Location.xls')