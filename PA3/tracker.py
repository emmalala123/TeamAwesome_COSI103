'''This program uses the Transaction class to track transactions,
summarize them, and print them out. It tracks the amount, category,
date, and description of each transaction. It can also summarize
transactions by day, month, year, or category. It can also add, show, and delete
transactions.'''

import sys
from datetime import datetime
from transaction import Transaction

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
        0. quit                                 (0)
        1. show transactions                    (1)
        2. add transaction                      (2 amount category description)
        3. delete transaction                   (3 transaction_#)
        4. summarize transactions by date       (4 DD)
        5. summarize transactions by month      (5 MM)
        6. summarize transactions by year       (6 YYYY)
        7. summarize transactions by category   (7 category)
        8. print this menu                      (8)
        '''
            )

def print_transactions(transactions):
    ''' print the todo items '''
    if len(transactions)==0:
        print('no transactions to print')
        return
    print('\n')
    print("#\tamount\tcategory\tdate\t\t\tdescription")
    print('-'*80)
    for item in transactions:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print(f"{values[0]}\t{values[1]}\t{values[2]}\t\t{values[3]}\t{values[4]}")

def process_crud_args(arglist):
    ''' process the command line arguments '''
    database = Transaction()
    database.show_all()
    if arglist==[]:
        print_usage()

    # show transactions
    elif arglist[0]=="1":
        print_transactions(database.show_all())

    # add transaction
    elif arglist[0]=="2":
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  #"2022-11-09 01:34:38"
        transaction = {'amount':arglist[1],'category':arglist[2],
                       'date':date,'description':arglist[3]}
        database.add(transaction)

    # delete transaction
    elif arglist[0]=="3":
        if len(arglist)!= 2:
            print_usage()
        else:
            database.delete(arglist[1])

    else:
        process_summary_args(arglist, database)

def process_summary_args(arglist, database):
    ''' process the summary command line arguments '''
    # summarize by day
    if arglist[0]=="4" and len(arglist)== 2:
        print_transactions(database.summarize_by_day(arglist[1]))

    # summarize by month
    elif arglist[0]=="5" and len(arglist)== 2:
        print_transactions(database.summarize_by_month(arglist[1]))

    # summarize by year
    elif arglist[0]=="6" and len(arglist)== 2:
        print_transactions(database.summarize_by_year(arglist[1]))

    # summarize by category
    elif arglist[0]=="7" and len(arglist)== 2:
        print_transactions(database.summarize_by_category(arglist[1]))

    # print usage
    else:
        print_usage()

def toplevel():
    ''' read the command args and process them'''
    print_usage()
    args = []
    while args!=['']:
        args = input("command> ").split(' ')

        # add
        if args[0]=='0' or args[0]=='quit':
            sys.exit()
        if args[0]=='':
            args[0]='8'
        if args[0]=='2':
            # make sure right amount of args
            if len(args)<4:
                args[0]='8'
            # join everyting after the name as a string
            else:
                args = ['2',args[1],args[2]," ".join(args[3:])]
        process_crud_args(args)
        print('-'*80+'\n'*3)

if __name__ == "__main__":
    toplevel()
