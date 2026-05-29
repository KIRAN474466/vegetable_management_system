#python plus my sql project
import mysql.connector as db
conn=db.connect(user='root',password='your_password',\
           host='localhost',database='project')
cur=conn.cursor()
print('Start')
while True:
    role=input('Select Role(Owner/User/LogOut): ')
    if role == 'Owner' or role=='owner':      
        User=input('ENter User Id: ')
        Password=input('ENter Your Password: ')
        if User=='123' and Password=='1234':
            cur.execute("SELECT COUNT(*) AS column_count FROM INFORMATION_SCHEMA.COLUMNS\
                        WHERE table_schema = 'project' AND table_name ='Owner'")
            m=cur.fetchone()[0]
            cur.execute('select count(*) from Owner')
            n=cur.fetchone()[0]
            print('*'*10,'Inventory','*'*10)
            sp=' '
            columns=['Vegetables','Quantity','CostPrice','SellPrice','SoldQty']
            for i in columns:
                print(i,sp*(13-len(i)),end='')
            print()
            sp=' '
            for i in range(0,n):
                for j in range(0,m):
                    cur.execute('Select *from Owner')
                    data=cur.fetchall()[i][j]
                    if len(str(data))>0:
                        print(data,sp*(12-len(str(data))),end='|')
                print()
            print('-'*10,'Menu','-'*10)
            x=['Add','Delete','Update','View_Inventory'\
               ,'Item_Wiseprofit','Report','Exit']
            j=1
            for i in x:
                print(j,')',i,sep='')
                j=j+1
            while True:
                Option=input('Enter Any Option From Menu: ')
                if Option == '1' or Option == 'Add' or Option == 'add':
                    Item=input('Enter the item you want add: ')
                    Quantity=int(input('Enter the Quantity of the Item: '))
                    Cost_price=int(input('Enter The Cost price Of the Item: '))
                    Sell_price=int(input('Enter the Sell Price Of The Item: '))
                    cur.execute('insert into Owner(Vegetables,Quantity,Cost_price,Sell_price) values(%s,%s,%s,%s)',[Item,Quantity,Cost_price,Sell_price])
                    conn.commit()
                elif Option == '2' or Option == 'Remove' or Option == 'remove':
                    Item=input('Enter The Item To be Removed: ')
                    cur.execute('Select count(*) from Owner Where Vegetables=%s',[Item])
                    Cnt=cur.fetchone()[0]
                    if Cnt>0:
                        cur.execute('delete from Owner where Vegetables=%s',[Item])
                        conn.commit()
                    else:
                        print('Item is Not available')
                        continue
                elif Option == '3' or Option == 'Update' or Option == 'update':
                    choice=input('enter what do you want to update(quantity/price/soldqty):')
                    if choice == 'quantity':
                        Item=input('Enter The Item To be Updated: ')
                        cur.execute('select count(*) from Owner where Vegetables=%s ',[Item])
                        cnt=cur.fetchone()[0]
                        if cnt>0:
                            quantity=input('Enter the quantity To be updated:')
                            cur.execute('Update Owner set Quantity =%s where Vegetables=%s',[quantity,Item])
                            conn.commit()
                        else:
                            print('Item is not available')
                            continue
                    elif choice == 'price':
                        Item=input('Enter The Item To be Updated: ')
                        cur.execute('select count(*) from Owner where Vegetables=%s ',[Item])
                        cnt=cur.fetchone()[0]
                        if cnt>0:
                            Cost_price=input('Enter the Costprice To be updated:')
                            Sell_price=input('Enter the Sellprice To be updated:')
                            cur.execute('Update Owner set Cost_price = %s,Sell_price=%s where Vegetables=%s',[Cost_price,Sell_price,Item])
                            conn.commit()
                        else:
                            print('Item is not available')
                            continue
                    elif choice == 'soldqty':
                        cur.execute('Update owner set Sold_qty=0')
                        conn.commit()
                    else:
                        print('Invalid Choice')
                        continue
                elif Option == '4' or Option == 'Inventory' or Option == 'inventory':
                    cur.execute("SELECT COUNT(*) AS column_count FROM INFORMATION_SCHEMA.COLUMNS\
                        WHERE table_schema = 'project' AND table_name ='Owner'")
                    m=cur.fetchone()[0]
                    cur.execute('select count(*) from Owner')
                    n=cur.fetchone()[0]
                    print('*'*10,'Inventory','*'*10)
                    sp=' '
                    columns=['Vegetables','Quantity','CostPrice','SellPrice','SoldQty']
                    for i in columns:
                        print(i,sp*(13-len(i)),end='')
                    print()
                    for i in range(0,n):
                        for j in range(0,m):
                            cur.execute('Select *from Owner')
                            data=cur.fetchall()[i][j]
                            if len(str(data))>0:
                                print(data,sp*(12-len(str(data))),end='|')
                        print()
                elif Option == '5' or Option == 'Itemwise_Profit' or Option == 'itemwise_profit':
                    print('-'*5,'Item Wise Profit','-'*5)
                    columns=['Vegetables','Soldqty','Itemprofit']
                    sp=' '
                    for i in columns:
                        print(i,sp*(13-len(i)),end='')
                    print()
                    cur.execute('Select count(*)from Owner')
                    c=cur.fetchone()[0]      
                    for i in range(0,c):
                        for j in range(0,3):
                            cur.execute('select Vegetables,Sold_qty,(Sell_price-Cost_price)*Sold_qty from Owner')
                            data=cur.fetchall()[i][j]
                            if len(str(data))>0:
                                print(data,sp*(12-len(str(data))),end='|')
                        print()
                    cur.execute('Select sum((Sell_price-Cost_price)*Sold_qty) from owner')
                    r=cur.fetchone()[0]
                    print('Total Sales Profit',r)
                elif Option == '6' or Option == 'Report' or Option == 'report':
                    print('-'*5,'Total Sales Report','-'*5)
                    columns=['Vegetables','Soldqty','Itemsales']
                    sp=' '
                    for i in columns:
                        print(i,sp*(13-len(i)),end='')
                    print()
                    cur.execute('Select count(*)from Owner')
                    c=cur.fetchone()[0]      
                    for i in range(0,c):
                        for j in range(0,3):
                            cur.execute('select Vegetables,Sold_qty,Sell_price*Sold_qty from Owner')
                            data=cur.fetchall()[i][j]
                            if len(str(data))>0:
                                print(data,sp*(12-len(str(data))),end='|')
                        print()
                    cur.execute('Select sum(Sell_price*Sold_qty) from owner')
                    s=cur.fetchone()[0]
                    print('Total Sales',s)
                elif Option == '7' or Option == 'Exit' or Option == 'exit':
                    Choice=input('Do You Want to log out From Owner(yes/no): ')
                    if Choice == 'yes':
                        print('Logout Successful')
                        break
                    else:
                        print('Ok')
                        continue
                else:
                    print('Invalid Option')
                    continue
        else:
            if User != '123' or Password != '1234':
                print('Access denied - Invalid Userid or Password')
                print('Please Check And Re-enter Your Details')
                break
    elif role == 'User' or role == 'user':
        print('*'*10,'Inventory','*'*10)
        sp=' '
        columns=['Vegetables','Quantity']
        for i in columns:
            print(i,sp*(12-len(i)),end=' ')
        print()
        cur.execute('select count(*) from Owner')
        n=cur.fetchone()[0]
        for i in range(0,n):
            for j in range(0,2):
                cur.execute('select Vegetables,Quantity from Owner group by Vegetables,Quantity')
                o=cur.fetchall()[i][j]
                if len(str(o))>0:
                    print(o,sp*(12-len(str(o))),end='|')
            print()
        print('-'*10,'Menu','-'*10)
        x=['Add','Remove','Modify','View cart','Billing','Exit']
        j=1
        for i in x:
            print(j,')',i,sep='')
            j=j+1
        while True:
            Option=input('Enter Any Option from Menu:')
            if Option == 'Add' or Option == '1' or Option == 'add':
                Item=input('Enter the Item To be Added to Cart:')
                cur.execute('Select count(*) from Owner where Vegetables=%s',[Item])
                cnt=cur.fetchone()[0]
                if cnt>0:
                    Qty=int(input('ENter How Much Quantity Do You Want:'))
                    cur.execute('Select Quantity from Owner Where Vegetables=%s',[Item])
                    result=cur.fetchone()[0]
                    if Qty<=result:
                        cur.execute('Select Sell_price from Owner Where Vegetables=%s',[Item])
                        price=cur.fetchone()[0]
                        cur.execute('Insert into user Values(%s,%s,%s)',[Item,Qty,price])
                        conn.commit()
                    else:
                        print('Entered Quantity is not available')
                else:
                    print('Item Not available')
            elif Option =='Remove' or Option == 'remove' or Option == '2':
                Item=input('Enter The Item Need To Be removed: ')
                cur.execute('Select count(*) from User where Item_name=%s',[Item])
                cnt=cur.fetchone()[0]
                if cnt>0:
                    cur.execute('Delete From User where Item_name=%s',[Item])
                    conn.commit()
                else:
                    print('Item is Not available in cart')
            elif Option == 'Modify' or Option =='modify' or Option =='3':
                Item=input('Enter The Item Need to be Updated:')
                cur.execute('Select count(*) from user where Item_name=%s',[Item])
                cnt=cur.fetchone()[0]
                if cnt>0:
                    Qty=int(input("How much Quantity do you want to modify:"))
                    cur.execute('Select Quantity from Owner where Vegetables=%s',[Item])
                    result=cur.fetchone()[0]
                    bkp=Item
                    if Qty<=result:
                        cur.execute('Update User set Item_quantity=%s where Item_name=%s',[Qty,bkp])
                        conn.commit()
                    else:
                        print('Entered Quantity is not available')
                else:
                    print('Item is not available')
            elif Option == 'Cart' or Option == 'cart' or Option == '4':
                cur.execute('select count(*) from user')
                m=cur.fetchone()[0]
                sp=' '
                columns=['Vegetables','Quantity','Price(kg)']
                for i in columns:
                    print(i,sp*(12-len(i)),end=' ')
                print()
                for i in range(0,m):
                    for j in range(0,3):
                        cur.execute('Select * From User')
                        n=cur.fetchall()[i][j]
                        if len(str(n))>0:
                            print(n,sp*(12-len(str(n))),end='|')
                    print()
            elif Option =='Bill' or Option == 'bill' or Option == '5':
                while True: 
                        cur.execute('select count(*) from user')
                        m=cur.fetchone()[0]
                        if m>0:
                            Mobile=input('Enter Mobile Number: ')
                            Name=input('Enter your Name:')
                            n=m
                            if Mobile.isdigit() and len(Mobile)==10:
                                print('SKMl Super Market')
                                print('Mobile: ',Mobile)
                                print('Name:',Name)
                                s=' '
                                columns=['S.no','Item','Quantity','Price','Totalprice']
                                for i in columns:
                                    print(i,sp*(12-len(i)),end='')
                                print()
                                for i in range(0,n):
                                    print(i+1,')',sp*(11-len(str(i))),end='')
                                    for j in range(0,4):
                                        cur.execute('select Item_name,Item_Quantity,Item_Price,\
                                                    Item_Quantity*Item_Price as Total_price from user')
                                        data=cur.fetchall()[i][j]
                                        if len(str(data))>0:
                                            print(data,sp*(11-len(str(data))),end=' ')
                                    print()
                                cur.execute('with tmp as(select Item_name,Item_Quantity,Item_Price,Item_Quantity*Item_Price as Total_Price from user)\
                                              select sum(Total_Price) from tmp;')
                                t=cur.fetchone()[0]
                                print('Total Amount To Be Paid:',t)
                                cur.execute('select count(*) from user')
                                m=cur.fetchone()[0]
                                for i in range(0,m):
                                    cur.execute('select Item_name,Item_quantity from user')
                                    item=cur.fetchall()[i][0]
                                    cur.execute('select Item_name,Item_quantity from user')
                                    qty=cur.fetchall()[i][1]
                                    cur.execute('update owner set Sold_qty=%s Where Vegetables=%s',[qty,item])
                                conn.commit()
                                cur.execute('delete from user')
                                conn.commit()
                                cur.execute('update owner set Quantity=Quantity-Sold_qty')
                                conn.commit()
                                break
                            else:
                                print('Invalid Please re-enter Your Details')
                        else:
                            print('No Items in cart To generate bill')
                            break
            elif Option =='Exit' or Option=='exit' or Option =='6':
                Choice=input('Do you want to log out From user(yes/no):')
                if Choice == 'yes':
                    print('Log out Successful')
                    break
                else:0
                    print('Ok')
                    continue
            else:
                print('Invalid Option')
                continue
    elif role == 'Logout' or role =='logout':
        Status=input('Do you want to close the shop(yes/no): ')
        if Status == 'yes':
            print('Hope You Had a great Day')
            break
        else:
            print('Ok')
            continue
    else:
        print('Invalid Role')
        continue                    
conn.close()
cur.close()
