from flask import Flask, render_template,request,redirect
import psycopg2


app = Flask(__name__)

# try:
conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='P@$$w0rd'")
# except:
#     print ("I am unable to connect to the database")

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/save-inventory',methods=['post'])
def save_inventory():
    n=request.form["name"]
    bp=request.form["buying_price"]
    sp=request.form["selling_price"]
    sq=request.form["stock_quantity"]
    cur = conn.cursor()
    postgres_insert_query = """INSERT into products(name, buying_price, selling_price, stock_quantity) VALUES (%s,%s,%s,%s)"""
    record_to_insert = (n,bp,sp,sq)
    cur.execute(postgres_insert_query, record_to_insert)
    print("Record inserted successfully into mobile table")
    conn.commit() # <- We MUST commit to reflect the inserted data
    conn.close()



    print(n,bp,sp,sq)


    return redirect("inventory")

@app.route('/sales')
def sales():
    return render_template("sales.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/inventory')
def inventories():
    cur = conn.cursor()
    cur.execute("""SELECT * from products""")
    rows = cur.fetchall()
    # List of tuples. Only print out the product names
    for i in rows:
        print(i)


    # print(rows)

   

    return render_template("inventory.html", rows=rows)




    if __name__ == '__main__':
        app.run(debug=True)

