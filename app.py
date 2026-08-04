import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os



app = Flask(__name__)


app.secret_key = os.environ.get('SECRET_KEY', 'your secrete key')


app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD', '9802')
app.config['MYSQL_DB'] = os.environ.get('MYSQLDATABASE', 'cafe_management_system')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQLPORT', 3306))

mysql = MySQL(app)

#------------------------------------- MENU (now loaded from database) -----------------------------------

def get_menu():
    """Fetches all menu items from the database and returns them as a dict,
    e.g. {'item2': {'name': 'AMERICANO', 'price': 120, 'category': 'Coffee'}, ...}
    This replaces the old hardcoded MENU dictionary so admin edits persist."""
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT ITEM_ID, ITEM_NAME, PRICE, CATEGORY FROM MENU_ITEMS')
    rows = cursor.fetchall()
    menu = {}
    for row in rows:
        menu[row['ITEM_ID']] = {
            'name': row['ITEM_NAME'],
            'price': row['PRICE'],
            'category': row['CATEGORY']
        }
    return menu


def admin_required(f):
    """Decorator: blocks access to a route unless the admin is logged in."""
    from functools import wraps
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('Please login as admin first!')
            return redirect(url_for('Admin_login'))
        return f(*args, **kwargs)
    return wrapper

#------------------------------------- CART COUNT (available on every page) -----------------------------------

@app.context_processor
def inject_cart_count():
    cart = session.get('cart', {})
    count = sum(cart.values())
    return dict(cart_count=count)

#------------------------------------- CART ROUTES -----------------------------------

@app.route("/add_to_cart/<item_key>")
def add_to_cart(item_key):
    menu = get_menu()
    if item_key not in menu:
        flash("Item not found!")
        return redirect(request.referrer or url_for('menu'))

    cart = session.get('cart', {})
    cart[item_key] = cart.get(item_key, 0) + 1
    session['cart'] = cart
    session.modified = True

    flash(f"{menu[item_key]['name']} added to cart!")
    return redirect(request.referrer or url_for('menu'))


@app.route("/cart")
def cart():
    menu = get_menu()
    cart = session.get('cart', {})
    bill = []
    grand_total = 0

    for item_key, qty in cart.items():
        if item_key not in menu:
            continue   # item may have been deleted by admin since being added to cart
        price = menu[item_key]['price']
        total = price * qty
        bill.append({
            'key': item_key,
            'name': menu[item_key]['name'],
            'qty': qty,
            'price': price,
            'total': total
        })
        grand_total += total

    return render_template('cart.html', bill=bill, grand_total=grand_total)


@app.route("/remove_from_cart/<item_key>")
def remove_from_cart(item_key):
    cart = session.get('cart', {})
    if item_key in cart:
        del cart[item_key]
        session['cart'] = cart
        session.modified = True
    return redirect(url_for('cart'))


@app.route("/checkout")
def checkout():
    menu = get_menu()
    cart = session.get('cart', {})
    bill = []
    grand_total = 0

    for item_key, qty in cart.items():
        if item_key not in menu:
            continue
        price = menu[item_key]['price']
        total = price * qty
        bill.append({
            'name': menu[item_key]['name'],
            'qty': qty,
            'price': price,
            'total': total
        })
        grand_total += total

    session['bill'] = bill
    session['grand_total'] = grand_total
    session.pop('cart', None)   # clear cart after checkout
    session.modified = True

    return redirect(url_for('receipt'))

#------------------------------------ Admin Login Page ------------------------------------

@app.route("/Admin_login", methods=['GET','POST'])
def Admin_login() :
        print('hi')
        error = None
        # print(f'value of request method #{request.method} #{request.form}')
        # a='username' in request.form
        # b='password' in request.form
        # print(f'value of request method #{a} #{b}')
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:   
            # print("Hello this my first project")
            if request.form['email'] != 'daniel123@gmail.com' or \
                request.form['password'] != 'dan123': 
                # print('inside 2 if')
                error = 'Invalid credentials'
                flash('Invalid Credentials')
            else:
                # print('inside 2 else')
                session['admin_logged_in'] = True
                flash('You have logged in successfully!!')
                return redirect(url_for('admin_dashboard'))

        return render_template("Admin_login.html",error=error) 

@app.route('/Admin_logout')
def AdminLogout() :
    session.pop('admin_logged_in', None)
    log1 = ''
    log1 = 'You have logged out successfully!!'
    return render_template('AdminLogin.html', log1=log1)   


#-------------------------------- Admin Menu Management (CRUD) ----------------------------------

@app.route("/admin/menu")
@admin_required
def admin_menu():
    menu = get_menu()
    # convert to list of dicts (with id included) so the template can loop easily
    items = [{'id': k, 'name': v['name'], 'price': v['price'], 'category': v['category']} for k, v in menu.items()]
    items.sort(key=lambda x: (x['category'], x['name']))
    return render_template('admin_menu.html', items=items)


@app.route("/admin/menu/add", methods=['GET', 'POST'])
@admin_required
def admin_menu_add():
    error = None
    if request.method == 'POST':
        item_id = request.form.get('item_id', '').strip()
        name = request.form.get('name', '').strip()
        price = request.form.get('price', '').strip()
        category = request.form.get('category', '').strip()
        description = request.form.get('description', '').strip()
        image_url = request.form.get('image_url', '').strip()

        if not item_id or not name or not price or not category:
            error = 'Please fill out all required fields!'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM MENU_ITEMS WHERE ITEM_ID = %s', (item_id,))
            existing = cursor.fetchone()
            if existing:
                error = f'Item ID "{item_id}" already exists! Choose a different ID.'
            else:
                cursor.execute(
                    'INSERT INTO MENU_ITEMS (ITEM_ID, ITEM_NAME, PRICE, CATEGORY, DESCRIPTION, IMAGE_URL) VALUES (%s, %s, %s, %s, %s, %s)',
                    (item_id, name, price, category, description, image_url)
                )
                mysql.connection.commit()
                flash(f'{name} added to the menu!')
                return redirect(url_for('admin_menu'))

    return render_template('admin_menu_form.html', mode='add', error=error, item=None)


@app.route("/admin/menu/edit/<item_id>", methods=['GET', 'POST'])
@admin_required
def admin_menu_edit(item_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    error = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        price = request.form.get('price', '').strip()
        category = request.form.get('category', '').strip()
        description = request.form.get('description', '').strip()
        image_url = request.form.get('image_url', '').strip()

        if not name or not price or not category:
            error = 'Please fill out all required fields!'
        else:
            cursor.execute(
                'UPDATE MENU_ITEMS SET ITEM_NAME = %s, PRICE = %s, CATEGORY = %s, DESCRIPTION = %s, IMAGE_URL = %s WHERE ITEM_ID = %s',
                (name, price, category, description, image_url, item_id)
            )
            mysql.connection.commit()
            flash(f'{name} updated!')
            return redirect(url_for('admin_menu'))

    cursor.execute('SELECT * FROM MENU_ITEMS WHERE ITEM_ID = %s', (item_id,))
    item = cursor.fetchone()
    if not item:
        flash('Item not found!')
        return redirect(url_for('admin_menu'))

    return render_template('admin_menu_form.html', mode='edit', error=error, item=item)


@app.route("/admin/menu/delete/<item_id>")
@admin_required
def admin_menu_delete(item_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('DELETE FROM MENU_ITEMS WHERE ITEM_ID = %s', (item_id,))
    mysql.connection.commit()
    flash('Item deleted from menu!')
    return redirect(url_for('admin_menu'))

#-------------------------------- Customer Login ----------------------------------------

@app.route("/Register", methods=['GET','POST'])
def Register():
    error = None
    if request.method == 'POST' and 'Name' in request.form and 'phNo' in request.form and 'Address' in request.form and 'pswd' in request.form:
        Phonenumber = request.form['phNo']
        Name = request.form['Name']
        Address = request.form['Address']
        pswd = request.form['pswd']
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #executing query to insert new data into MySQL
        cursor.execute('INSERT INTO CUSTOMER VALUES(% s, % s , % s, % s)',(Name,Phonenumber,Address,pswd))
        mysql.connection.commit()
        #displaying message
        flash('You have successfully Regsitered!')
        return redirect(url_for('cust_login')) #add a page here
    else :
        error = 'Please fill out the form!!'
        return render_template("register.html", error=error)


@app.route('/cust_login', methods = ['GET','POST'])
def cust_login():
    error = None
    if request.method == 'POST' and 'Name' in request.form and 'pswd' in request.form and 'mobile_no' in request.form:
        cust_name=request.form['Name']
        pswd = request.form['pswd']
        mobile_no = request.form['mobile_no']
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #executing query to insert new data into MySQL
        cursor.execute('SELECT * FROM CUSTOMER WHERE CUST_NAME=%s AND MOBILE_NO = % s AND PSWD=%s',(cust_name,mobile_no,pswd))
        account = cursor.fetchone()
        if account :
            flash('You have logged in successfully!!')
            return redirect(url_for('menu'))
        else:
            error='invalid credentials'
            return render_template('cust_login.html', error=error)
            
    elif request.method =='POST' :
        error = 'Please fill out the details!!'

    return render_template('cust_login.html', error=error)

        #displaying message
        # flash('You have successfully logged in !')
        # return redirect(url_for('menu'))
#    else :
#        error = 'Invalid Crendentials!!'
#     return render_template("cust_login.html", error=error)

@app.route('/Logout')
def Logout() :
    log2 = ''
    log2= 'You have logged out successfully!!'
    return render_template('cust_login.html', log2=log2)

#-------------------------------- Admin Dashboard ---------------------------------------

@app.route("/AdminDashboard")
def admin_dashboard():
    employees = 0
    orders = 0
    customers = 0
    # creating a variable connection
    #---------------*****displays on cards******------------
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT COUNT(DISTINCT EMP_ID) AS Employees FROM EMPLOYEE')        # gives the count of employee
    mysql.connection.commit()
    result1=cursor.fetchone()
    employees = result1['Employees']
    #---------------*****displays on cards******------------
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT COUNT(ORDER_NO) AS Orders FROM ORDERS')                     # gives the count of orders
    mysql.connection.commit()
    result2=cursor.fetchone()
    orders = result2['Orders']
    #---------------*****displays on cards******------------
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT COUNT(MOBILE_NO) AS Customers FROM CUSTOMER')               # gives the count of customer
    mysql.connection.commit()
    result3 = cursor.fetchone()
    customers = result3['Customers']
    #----------------*****displays on cards******------------
    return render_template("admin_dashboard.html",employees=employees,orders=orders,customers=customers)  

#-----------------******** side bars ********------------------
@app.route("/customers")
def customers():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT CUST_NAME,MOBILE_NO,ADDRESS FROM CUSTOMER')                    # fetches the attributes
    mysql.connection.commit()
    customers = cursor.fetchall()
    return render_template("index.html",customers=customers)

@app.route("/orders")
def orders():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT ORDER_NO,ITEM_NAME,ITEM_NO,MOB_NO,QUANTITY FROM ORDERS')       # fetches the attributes
    mysql.connection.commit()
    orders = cursor.fetchall()

    return render_template("orders.html",orders=orders)

@app.route("/employee",methods = ['GET','POST'])
def employees():
    error = ''
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if request.method == 'POST' and 'emp_id' in request.form:
        emp_id= request.form['emp_id']
        cursor.execute('SELECT * FROM EMPLOYEE WHERE EMP_ID = % s',(emp_id,))
        result = cursor.fetchone()
        if  result :
            cursor.execute('DELETE FROM EMPLOYEE WHERE EMP_ID = % s',(emp_id,))
            mysql.connection.commit()
        else :
            error = 'Employee doesn\'t exists!!'
    cursor.execute('SELECT EMP_NAME,EMP_ID,DESIGNATION,GENDER,MOB_NO FROM EMPLOYEE')       # fetches the attributes
    mysql.connection.commit()
    employees = cursor.fetchall()
    return render_template("employee.html",employees=employees, error=error)


@app.route("/employee/add", methods=['GET', 'POST'])
def employee_add():
    error = None
    if request.method == 'POST':
        emp_id = request.form.get('emp_id', '').strip()
        emp_name = request.form.get('emp_name', '').strip()
        designation = request.form.get('designation', '').strip()
        gender = request.form.get('gender', '').strip()
        mob_no = request.form.get('mob_no', '').strip()

        if not emp_id or not emp_name or not designation or not gender or not mob_no:
            error = 'Please fill out all fields!'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM EMPLOYEE WHERE EMP_ID = %s', (emp_id,))
            existing = cursor.fetchone()
            if existing:
                error = f'Employee ID "{emp_id}" already exists! Choose a different ID.'
            else:
                cursor.execute(
                    'INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME, DESIGNATION, GENDER, MOB_NO) VALUES (%s, %s, %s, %s, %s)',
                    (emp_id, emp_name, designation, gender, mob_no)
                )
                mysql.connection.commit()
                flash(f'{emp_name} added successfully!')
                return redirect(url_for('employees'))

    return render_template("employee_add.html", error=error)

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")
#----------------------------*********************************------------------------------

#----------------------------*************Menu****************------------------------------
@app.route("/")
def home():
    #return render_template("welcome.html",username=session['username'])     I changed this
    return render_template("welcome.html")

@app.route("/menu")
def menu():
    return render_template('menu.html')     

@app.route("/coffeemenu")
def coffeemenu():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM MENU_ITEMS WHERE CATEGORY = %s ORDER BY ITEM_NAME', ('Coffee',))
    items = cursor.fetchall()
    return render_template("category.html", items=items, css_file='coffemenu.css')

@app.route("/pizzamenu")
def pizzamenu():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM MENU_ITEMS WHERE CATEGORY = %s ORDER BY ITEM_NAME', ('Pizza',))
    items = cursor.fetchall()
    return render_template("category.html", items=items, css_file='pizzamenu.css')

@app.route("/burgers")
def burgers():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM MENU_ITEMS WHERE CATEGORY = %s ORDER BY ITEM_NAME', ('Burgers',))
    items = cursor.fetchall()
    return render_template("category.html", items=items, css_file='Burgers.css')

@app.route("/Sandwiches")
def Sandwiches():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM MENU_ITEMS WHERE CATEGORY = %s ORDER BY ITEM_NAME', ('Sandwiches',))
    items = cursor.fetchall()
    return render_template("category.html", items=items, css_file='Sandwiches.css')

@app.route("/shorteates")
def shorteates():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM MENU_ITEMS WHERE CATEGORY = %s ORDER BY ITEM_NAME', ('ShortEats',))
    items = cursor.fetchall()
    return render_template("category.html", items=items, css_file='shorteates.css')

@app.route("/Beverages")
def Beverages():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM MENU_ITEMS WHERE CATEGORY = %s ORDER BY ITEM_NAME', ('Beverages',))
    items = cursor.fetchall()
    return render_template("category.html", items=items, css_file='Beverages.css')

@app.route("/reviews")
def reviews():
    return render_template("reviews.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/item", methods=["GET", "POST"])
def item():

    if request.method == "POST":

        menu = get_menu()
        selected_items = request.form.getlist("items")

        bill = []
        grand_total = 0

        for item in selected_items:

            qty = int(request.form.get(item, 0))

            if qty > 0 and item in menu:

                price = menu[item]["price"]
                total = price * qty

                bill.append({
                    "name": menu[item]["name"],
                    "qty": qty,
                    "price": price,
                    "total": total
                })

                grand_total += total

        session["bill"] = bill
        session["grand_total"] = grand_total

        return redirect(url_for("receipt"))

    return render_template("item.html")


@app.route("/receipt")
def receipt():

    bill = session.get("bill", [])
    grand_total = session.get("grand_total", 0)

    return render_template(
        "receipt.html",
        bill=bill,
        grand_total=grand_total
    )

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)