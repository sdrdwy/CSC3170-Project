import pymysql
class DataBase:
    def __init__(self,host='localhost',user='root',passwd='',port=3306) -> None:
        self.db=pymysql.connect(host=host,
                           user=user,
                           passwd=passwd,
                           port=port)
        self.cursor=self.db.cursor()
        self.cursor.execute("use tire_company")
    def list_table(self,table)->tuple:
        #return all the elements from table
        ins="SELECT * FROM "+table
        self.cursor.execute(ins)
        return self.cursor.fetchall()
    def select_by_date(self,table,attr,start,end)->tuple:
        ins=f"SELECT * FROM {table}  ORDER BY {attr} DESC"
        if start !="" and end !="":
            ins=f"SELECT * FROM {table} WHERE {attr} BETWEEN '{start}' AND '{end}' ORDER BY {attr} DESC"
        self.cursor.execute(ins)
        return self.cursor.fetchall()
    def select_equal(self,table,attr,constrain)->tuple:
        ins=f"SELECT * FROM {table} WHERE {attr} = {constrain}"
    def get_order(self,oname,oid):
        ins_title=f"DESC {oname}"
        self.cursor.execute(ins_title)
        title=self.cursor.fetchall()
        ins_data=f"SELECT * FROM {oname} WHERE {title[1][0]} = {oid}"
        if "selling" in oname:
            ins_data=f"SELECT * FROM {oname} WHERE {title[0][0]} = {oid}"
        self.cursor.execute(ins_data)
        data=self.cursor.fetchall()
        return title,data
    def get_overview(self):
        #TODO: return 5 tuple (a,b),representing:
        #sell,trans,manu: total money of 3 orders
        #cus: customer count,customer order count
        #inv: inventory count, inventory order count
        cus=[0,0]
        self.cursor.execute("SELECT COUNT(*),SUM(money_amount) FROM selling_order")
        sell=self.cursor.fetchone()
        self.cursor.execute("SELECT COUNT(*),SUM(transport_cost) FROM transport_order")
        trans=self.cursor.fetchone()
        self.cursor.execute("SELECT COUNT(*),SUM(total_cost) FROM manu_order")
        manu=self.cursor.fetchone()
        self.cursor.execute("SELECT COUNT(DISTINCT(customer_id)) FROM selling_order")
        cus[0],cus[1]=self.cursor.fetchone()[0],sell[1]
        self.cursor.execute("SELECT COUNT(DISTINCT(Tire_id)),SUM(tire_storage_number) FROM inventory")
        inv=self.cursor.fetchone()
        return sell,trans,manu,cus,inv
    def get_tire(self,size):
        ins=f"SELECT * FROM tire_information WHERE tire_Inch = '{size}'"
        if size=="":
            ins="SELECT * FROM tire_information"
        self.cursor.execute(ins)
        return self.cursor.fetchall()
    def get_team(self,team)->tuple:
        #team has 3 input: sell, transport, manu
        #TODO: return tuples(teamid,Team Leader,employeeid,team information)
        #refer to program above
        if team=='selling':
            table = 'Selling_Order'
        elif team=='transport':
            table = 'Transport_order'
        else:
            table = 'Manu_order'
        ins=f"""
SELECT DISTINCT so.team_ID, t.leader AS team_leader, e.employee_ID, t.team_name, t.members_info
FROM {table} so
JOIN Team t ON so.team_ID = t.team_ID
JOIN employee e ON t.leader = e.employee_name;
"""
        self.cursor.execute(ins)
        return self.cursor.fetchall()
if __name__ == "__main__":
    db=DataBase(passwd="")
    db.cursor.execute("desc transport_order_detail")
    t,d=db.get_order("selling_order_detail",112452)
    print(t)
    print(d)