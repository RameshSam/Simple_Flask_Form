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

app =Flask(__name__ , template_folder="tempalate1")

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

@app.route("/updated",method = ['POST',"GET"])
def updated():
    try:
        id = request.form['Reg']
        print(id)
        if request.method == "POST" :
            for i in Employee[id]:
                if id == i["Regno"]:
                    print(i["Regno"])
                    print(i["Name"])
                    print(i["Email"])
                    msg  = "Working purpose "
        return render_template("result.html",msg = msg)


    except:
        msg = "This didn't Work "
    finally :
        return render_template("result.html", msg= msg) , 404

@app.route("\created ")
def create():

    res = make_response(jsonify(Employee) , 200)
    return res

if __name__ == "__main__" :
    app.run(debug=True,port=5000)
