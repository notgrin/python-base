# регулярные варвжения
import re

string = "asadasd 'a' \"C\" sad \\ addsa"

values = ['abd', 'a3-4', '333', '1324d', '111d']
for value in values:

    # result = re.search(r'\d', value)
    result = re.search(r'[02468d-]', value) # - набор букв, любой набор []
    if result:
        print(value, result)
    else:
        print(value, '- nothing found')



1,40

































# декораторы в Python