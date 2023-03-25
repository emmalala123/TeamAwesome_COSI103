from transaction import Transaction

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:         
            0. quit
            1. show transactions
            2. add transaction
            3. delete transaction
            4. summarize transactions by date
            5. summarize transactions by month
            6. summarize transactions by year
            7. summarize transactions by category
            8. print this menu
            '''
            )
    
def tracker(): 
    db = Transaction()
    (db.add({'amount': 100, 'category': 'food', 'date': '2019-01-01', 'description': 'groceries'}))
    print(db.show_all())

def process_args(arglist):
    db = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="0":
        quit()
    elif arglist[0]=="1":
       print(db.show_all())
    elif arglist[0]=="2":
         if len(arglist)!=5:
             print_usage()
         else:   
            transaction = {'amount':arglist[1],'category':arglist[2],'date':arglist[3],'description': arglist[4]}
            db.add(transaction)
    elif arglist[0]=="3":
        db.delete(arglist[1])

if __name__ == "__main__":

    # allows user to interface with the main menu
    print_usage()

    # this while-loop breaks as soon as the quit() function is called by user-input of "0"
    while True:
        # prompts user to input a choice from the menu and creates a list from white-space in arglist
        arglist = input("\n please input choice:").split()
        process_args(arglist)