import data_analyser

answer = int(input('Press 1 for file data or 2 for database data'))

if answer == 1:
    data_analyser.file_data_analyser.analyse_data()
elif answer == 2:
    data_analyser.database_data_analyser.analyse_data()
else:
    print('Incorrect option')
