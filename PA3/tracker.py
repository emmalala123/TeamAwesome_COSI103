from transaction import Transaction
import sys
from datetime import datetime


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
    print("%-5s %-10s %-15s %-20s %-30s"%('#','amount','category','date','description'))
    print('-'*80)
    for item in transactions:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-5s %-10s %-15s %-20s %-30s"%values)

def process_args(arglist):
    db = Transaction()
    db.show_all()
    if arglist==[]:
        print_usage()
    
    # show transactions
    elif arglist[0]=="1":
       print_transactions(db.show_all())

    # add transaction
    elif arglist[0]=="2":
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  #"2022-11-09 01:34:38"
        transaction = {'amount':arglist[1],'category':arglist[2],'date':date,'description':arglist[3]}
        db.add(transaction)

    # delete transaction
    elif arglist[0]=="3":
        if len(arglist)!= 2:
            print_usage()
        else:
            db.delete(arglist[1])

    # summarize by day
    elif arglist[0]=="4":
        if len(arglist)!= 2:
            print_usage()
        else:
            print_transactions(db.summarize_by_day(arglist[1]))

    # summarize by month
    elif arglist[0]=="5":
        if len(arglist)!= 2:
            print_usage()
        else:
            print_transactions(db.summarize_by_month(arglist[1]))

    # print usage
    elif arglist[0]=="8":
        print_usage()

    else:
        print(arglist,"is not implemented")
        print_usage()

def toplevel():
    ''' read the command args and process them'''
    print_usage()
    args = []
    while args!=['']:
        args = input("command> ").split(' ')
        
        # add
        if args[0]=='0' or args[0]=='quit':
            break
        if args[0]=='':
            args[0]='8'
        if args[0]=='2':
            # make sure right amount of args
            if len(args)<4:
                args[0]='8'
            # join everyting after the name as a string
            else:
                args = ['2',args[1],args[2]," ".join(args[3:])]
        process_args(args)
        print('-'*80+'\n'*3)

toplevel()