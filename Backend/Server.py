from flask import Flask,request,render_template
from dboperation import DataBase
app = Flask(__name__)
app.config['url_from']=''
app.config['Upper_page']=''
app.config['db']=DataBase(passwd="")
#========Home========#
@app.route("/")
@app.route("/home")
def home():
    file=open("templates\\enterpage.html",encoding="utf-8")
    return file.read()
#========Home========#
#========Employee/Company========#
@app.route('/employee')
def employee():
    app.config['url_from'] ="employee"
    file=open("templates\\EmployeeEnterPage.html",encoding="utf-8")
    return file.read()
@app.route('/company')
def company():
    app.config['url_from'] ="company"
    s,t,m,c,i=app.config["db"].get_overview()
    template=render_template("CompanyEnterPage.html",
                             sell=s,
                             trans=t,
                             manu=m,
                             cus=c,
                             inv=i)
    return template
#========Employee/Company========#
#========Employee Details========#
def date_post_handler(temp,table,attr):
    sDate=request.form.get("startDate")
    eDate=request.form.get("endDate")
    data=app.config["db"].select_by_date(table,attr,sDate,eDate)
    print(data)
    template=render_template(temp,
                            url_from=app.config['url_from'],
                            data=data)
    return template
@app.route('/SellingEmployee',methods=["POST","GET"])
def SellingEmployee():
    app.config['Upper_page']='SellingEmployee'
    template=render_template("SellingEmployee.html",url_from=app.config['url_from'])
    if request.method=="POST":
        template=date_post_handler("SellingEmployee.html","selling_order","date")
    return template
@app.route('/TransportEmployee',methods=["POST","GET"])
def TransportEmployee():
    app.config['Upper_page']='TransportEmployee'
    template=render_template("TransportEmployee.html",url_from=app.config['url_from'])
    if request.method=="POST":
        template=date_post_handler("TransportEmployee.html","transport_order","transport_date")
    return template
@app.route('/ManufacturedEmployee',methods=["POST","GET"])
def ManufacturedEmployee():
    app.config['Upper_page']='ManufacturedEmployee'
    template=render_template("ManufacturedEmployee.html",url_from=app.config['url_from'])
    if request.method=="POST":
        template=date_post_handler("ManufacturedEmployee.html","manu_order","date")
    return template
#========Employee Details========#
#========Order and Tire Details========#
@app.route('/tire_info',methods=["POST","GET"])
def tire_info():
    template = render_template("tire_info.html",url_from=app.config['Upper_page'])
    if request.method=="POST":
        tire = request.form.get('TireSize')
        print(tire)
        data=app.config['db'].get_tire(tire)
        template = render_template("tire_info.html",
                                   url_from=app.config['Upper_page'],
                                   data=data)
    return template
@app.route('/member_info',methods=["POST","GET"])
def member_info():
    team = request.args.get("from")
    data = app.config['db'].get_team(team)
    print(team)
    template = render_template("member_info.html",url_from=app.config['Upper_page'],data=data)
    return template
@app.route('/order_detail')
def order_detail():
    order_id = request.args.get("id")
    ofrom = request.args.get("from")
    print(ofrom)
    title,data=app.config["db"].get_order(ofrom,order_id)
    template=render_template("order_detail.html",title=title,data=data)
    return template
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')