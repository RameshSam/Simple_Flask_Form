from flask import Flask , render_template , request
import sqlite3

con = sqlite3.connect("sample.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS Datas")
print(" Table IF created Deleted ")
cmd = """ CREATE TABLE Datas(
            Reg_No Integer PRIMARYKEY , 
            Name VARCAHR(20) NOT NULL ,
            Email VARCHAR(20) ,
            Password VARCHAR(20) ,
            Confrim VARCHAR(20) );"""
cur.execute(cmd)
print(" Table Created ! ")
con.commit()
con.close()

app =Flask(__name__ , template_folder="template")

@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/getdata",methods = ['GET','POST'])   
def getdata():
    if request.method == "POST" :
        try:
            reg = request.form["Reg"]
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["pass"]
            conpass = request.form["conpass"]

            with sqlite3.connect("sample.db") as conn:
                curs = conn.cursor()
                check = curs.execute(" INSERT INTO Datas(Reg_No,Name ,Email ,Password ,Confrim ) VALUES(? , ? ,? ,? ,? ) ;",(reg,name ,email ,password ,conpass))
                msg = " Account Created Successfully..."
                # if check:
                #     print(" Inserted Successfully")
                # else:
                #     print(" Inserted Unsuccessfully")
                scmd = """ SELECT * FROM Datas ;"""
                curs.execute(scmd)
                result = curs.fetchmany()
                for i in result:
                    print(i)
                print(" Table Showed ")
                conn.commit()

        except:
            conn.rollback()
            msg = "Error in Insertion of Database"

        finally:
            conn.close()
            return render_template("result.html", msg= msg)
        
@app.route("/login")
def login():
    return render_template("signin.html")

@app.route("/fetchdata",methods =['GET',"POST"])
def fetchdata():
   if request.method == "POST" :
        try:
            name = request.form["name"]
            # email = request.form["email"]
            password = request.form["pass"]

            with sqlite3.connect("sample.db") as conn:
                curs = conn.cursor()
                scmd = """ SELECT * FROM Datas ;"""
                curs.execute(scmd)
                result = curs.fetchmany()
                for i in result:
                    if ( name == i[1] and password == i[3] ):
                        msg = " Login Successfully.."
                    else :
                        msg = " Login Unsuccessfully.."
                    print(i)
                print(" Table Data Allocated... ")
                conn.commit()
        except:
            conn.rollback()
            msg = "Error in Logining"

        finally:
            conn.close()
            return render_template("result.html", msg= msg)
@app.route("/change")
def change():
    return render_template("changepass.html")

@app.route("/changedata",methods =['GET',"POST"])
def changedata():
   if request.method == "POST" :
        try:
            email = request.form['email']
            curpass = request.form["curpass"]
            password = request.form["pass"]
            confirmpass = request.form["conpass"]

            with sqlite3.connect("sample.db") as conn:
                curs = conn.cursor()
                scmd = """ SELECT * FROM Datas ; """
                curs.execute(scmd)
                result = curs.fetchmany()
                for i in result:
                    if (curpass == i[3]):
                        conn.execute(" UPDATE Datas SET Password=(?) WHERE Email=(?)",(password , email))
                        msg = " Password Changed Successfully.."
                    else :
                        msg = " Password Changed Unsuccessfully.."
                    conn.execute(" UPDATE Datas SET Confrim=(?) WHERE Email=(?)",(confirmpass , email))
                curs.execute(" SELECT * FROM Datas ; ")
                result1 = curs.fetchmany()
                for j in result1:
                    print(j)
                print(" Table Data Updated... ")
                conn.commit()
        except:
            conn.rollback()
            msg = "Error in Logining"
            

        finally:
            conn.close()
            return render_template("result.html", msg= msg)

if __name__ == "__main__" :
    app.run(debug=True)