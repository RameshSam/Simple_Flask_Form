from flask import Flask , render_template , request , make_response , jsonify
import sqlite3

con = sqlite3.connect("flaskdb.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS Datas")
print(" Table IF created Deleted ")
cmd = """ CREATE TABLE Datas(
            Reg_No Integer PRIMARYKEY , 
            Name VARCAHR(20) NOT NULL ,
            Email VARCHAR(20) ,
            Password VARCHAR(20));"""
cur.execute(cmd)
print(" Table Created ! ")
con.commit()
con.close()

app =Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
       
@app.route("/login")
def login():
    return render_template("update.html")

@app.route("/getdata",methods = ['GET','POST'])   
def getdata():
    if request.method == "POST" :
        try:
            reg = request.form["Reg"]
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["pass"]

            with sqlite3.connect("flaskdb.db") as conn:
                curs = conn.cursor()
                check = curs.execute(" INSERT INTO Datas(Reg_No,Name ,Email ,Password) VALUES(? , ? ,? ,? ) ;",(reg,name ,email ,password))
                msg = " Account Created Successfully..."
                # if check:
                #     print(" Inserted Successfully")
                # else:
                #     print(" Inserted Unsuccessfully")
                scmd = """ SELECT * FROM Datas ;"""
                curs.execute(scmd)
                result = curs.fetchmany()
                for i in result:
                    global Employee
                    Employee = {
                        i[0]:
                        {
                        "Regno" : i[0] , 
                        "Name" : i[1] , 
                        "Email" : i[2] ,
                        "Password" : i[3]
                       }
                }
                print(Employee)
                print(" Table Showed ")
                conn.commit()

        except:
            conn.rollback()
            msg = "Error in Insertion of Database"

        finally:
            conn.close()
            return render_template("result.html", msg= msg)
        
    return render_template("result.html", msg= " PUT method Can't Initalized ")

@app.route("/updated/<int:id>",methods = ["PUT"])
def updated():
    try:
        # reg = request.form['Reg']
        print(id)
        if request.method == "PUT" :
                with sqlite3.connect("flaskdb.db") as conn:
                    curs = conn.cursor()
                    for i in Employee["Regno"]:
                        print(i["Regno"])
                        print(i["Name"])
                        # print(i["Email"])
                        if id == i['Regno']:
                            check = curs.execute(" UPDATE Datas SET Password =(? ) WHERE Reg_No = (?) ;",('6565',id))
                        if check :
                            print(" Working Properly")
                    msg  = "Account Password Updated "
        return render_template("result.html",msg = msg)
    
    except:
        msg = "This didn't Work "

    finally :
        return render_template("result.html", msg= msg) , 404

@app.route("/created")
def created():

    res = make_response(jsonify(Employee) , 200)
    return res

@app.route("/deleted/<int:id>" , methods= "DELETE")
def deleted_employee():
    global Employee
    i=0
    deleted  =False
    for employee in Employee:
        if employee['Reg_No'] == id:
            employee.pop(i)
            deleted = True
        i+= 1
    if deleted:
        msg = " Account Deleted "
        return render_template("result.html",msg = msg)
    else:
        msg = " Account Not Created  "
        return render_template("result.html",msg = msg)

if __name__ == "__main__" :
    app.run(debug=True,port=5000)
