from flask import Flask, render_template, request
import psycopg2

con = psycopg2.connect(database='medicine', user='postgres', password='201901033021', host='127.0.0.1', port=5432)

app = Flask(__name__)

"""*****************************************************************************************************"""


# 登录界面
@app.route('/')
def login():
    text = "Login"
    return render_template("login.html", text=text)  # 模板渲染


# 验证是否登录成功
@app.route('/is_login', methods=['GET', 'POST'])
def is_login():
    datalist = []
    text = "账号密码错误"
    cur = con.cursor()
    sql = "select * from login"
    cur.execute(sql)
    data = cur.fetchall()
    for item in data:
        datalist.append(item)
    cur.close()
    username = request.form["username"]
    password = request.form["password"]
    for item in datalist:
        if username == item[1] and password == item[2]:
            return render_template("index.html")
    return render_template("login.html", text=text)  # 模板渲染


"""*****************************************************************************************************"""


# 首页
@app.route('/index')
def index():  # put application's code here
    return render_template("index.html")  # 模板渲染


"""*****************************************************************************************************"""


# 信息查询(food_drug)
@app.route('/food_drug_find')
def food_drug_find():
    datalist = []
    cur = con.cursor()
    sql = "select * from food_drug order by id"
    cur.execute(sql)
    data = cur.fetchall()
    num = 1
    for item in data:
        item_list = list(item)
        item_list[0] = num
        datalist.append(item_list)
        num = num + 1
    cur.close()
    return render_template("food_drug_find.html", movies=datalist)


# 查询成功（food_drug)
@app.route('/success_find1', methods=["POST"])
def success_find1():
    name = request.form["name"]
    datalist = []
    cur = con.cursor()
    sql = "select * from food_drug where name = '" + name + "'"
    cur.execute(sql)
    data = cur.fetchall()
    num = 1
    for item in data:
        item_list = list(item)
        item_list[0] = num
        print(item_list)  # test
        datalist.append(item_list)
        num = num + 1
    cur.close()
    return render_template("food_drug_find.html", movies=datalist)


# 信息查询(health_food)
@app.route('/health_food_find')
def health_food_find():
    datalist = []
    cur = con.cursor()
    sql = "select * from health_food"
    cur.execute(sql)
    data = cur.fetchall()
    num = 1
    for item in data:
        item_list = list(item)
        item_list[33] = num
        print(item_list)  # test
        datalist.append(item_list)
        num = num + 1
    cur.close()
    return render_template("health_food_find.html", movies=datalist)


# 查询成功（health_food)
@app.route('/success_find2', methods=["POST"])
def success_find2():
    name = request.form["name"]
    datalist = []
    cur = con.cursor()
    sql = "select * from health_food where foodname = '" + name + "'"
    print(sql)
    cur.execute(sql)
    data = cur.fetchall()
    num = 1
    for item in data:
        item_list = list(item)
        item_list[33] = num
        print(item_list)  # test
        datalist.append(item_list)
        num = num + 1
    cur.close()
    return render_template("health_food_find.html", movies=datalist)


# 信息查询(warehouse_content)
@app.route('/content_find')
def content_find():
    datalist = []
    cur = con.cursor()
    sql = "select * from health_food where id <=100"
    cur.execute(sql)
    data = cur.fetchall()
    num = 1
    for item in data:
        item_list = list(item)
        item_list[33] = num
        print(item_list)  # test
        datalist.append(item_list)
        num = num + 1
    cur.close()
    return render_template("content_find.html", movies=datalist)


# 查询成功（warehouse_content)
@app.route('/success_find3', methods=["POST"])
def success_find3():
    name = request.form["name"]
    datalist = []
    cur = con.cursor()
    sql = "select * from health_food where foodname = '" + name + "'"
    print(sql)
    cur.execute(sql)
    data = cur.fetchall()
    num = 1
    for item in data:
        item_list = list(item)
        item_list[33] = num
        print(item_list)  # test
        datalist.append(item_list)
        num = num + 1
    cur.close()
    return render_template("health_food_find.html", movies=datalist)


"""*****************************************************************************************************"""


# 添加基本药品信息
@app.route('/message_add')
def message_add():
    return render_template("message_add.html")


# 保存成功
@app.route("/saverecord", methods=["POST", "GET"])
def saveRecord():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            other_name = request.form["other_name"]
            location = request.form["location"]
            effect = request.form["effect"]
            taboo = request.form["taboo"]
            address = request.form["address"]
            cur = con.cursor()
            sql = "INSERT INTO public.food_drug(name, alias, loc, effect, taboo,  place)	VALUES('" + name + "','" + other_name + "','" + location + "','" + effect + "','" + taboo + "','" + address + "')"
            cur.execute(sql)
            # (中药1,中药别称，肚子，可以治病，有一定毒性，江西)
            con.commit()
            msg = "医药信息添加成功"
        except:
            con.rollback()
            msg = "不能把该信息添加到数据库"
        finally:
            return render_template("success_record.html", msg=msg)


# 添加中成药的信息
@app.route('/health_food_add')
def health_food_add():
    return render_template("health_food_add.html")


# 保存成功
@app.route("/health_food_saverecord", methods=["POST", "GET"])
def health_saveRecord():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            wenhao = request.form["wenhao"]
            effect = request.form["effect"]
            chengfen = request.form["chengfen"]
            people = request.form["people"]
            yongliang = request.form["yongliang"]
            cur = con.cursor()
            sql = "INSERT INTO public.health_food(id,foodname, approval_number, function, main_material, appropriate_crowd,  usage)	VALUES(1,'" + name + "','" + wenhao + "','" + effect + "','" + chengfen + "','" + people + "','" + yongliang + "')"
            print(sql)  # test
            cur.execute(sql)
            con.commit()
            msg = "中成药信息添加成功"
        except:
            con.rollback()
            msg = "不能把该信息添加到数据库"
        finally:
            return render_template("success_record.html", msg=msg)


# 添加药品库存信息
@app.route('/content_add')
def content_add():
    return render_template("content_add.html")


# 保存成功
@app.route("/content_saverecord", methods=["POST", "GET"])
def content_saveRecord():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            yongliang = request.form["yongliang"]
            hanliang = request.form["hanliang"]
            content = request.form["content"]
            isku = request.form["isku"]
            attention = request.form["attention"]
            cur = con.cursor()
            cur.execute(
                "INSERT INTO public.food_drug(name, usage, product_specification, content,   matters_attention)	VALUES(" + name + "," + yongliang + "," + hanliang + "," + content + "," + attention + ")")

            con.commit()
            msg = "医药库存添加成功"
        except:
            con.rollback()
            msg = "不能把该信息添加到数据库"
        finally:
            return render_template("success_record.html", msg=msg)


"""*****************************************************************************************************"""


# 刪除药品信息（中药材）
@app.route('/message_delect')
def message_delect():
    return render_template("message_delect.html")


# 删除成功（中药材）
@app.route('/success_delect', methods=["POST"])
def success_delect():
    name = request.form["name"]
    cur = con.cursor()
    sql1 = "select * from food_drug where name = '" + name + "'"
    sql2 = "delete from food_drug where name = '" + name + "'"
    cur.execute(sql1)
    data = cur.fetchall()
    if not data == []:
        cur.execute(sql2)
        cur.close()
        return render_template("success_delect.html", data1="删除药类（源中药）" + name + "基本信息成功！",
                               data2="Successfully deleted the basic information of the drug!")
    else:
        cur.close()
        return render_template("success_delect.html", data1="医药信息数据库未查询到药类（源中药）" + name + "!",
                               data2="The drug was not found in the medical information database!")


# 刪除药品信息(中成药）
@app.route('/health_food_message_delect')
def health_food_message_delect():
    return render_template("health_food_delect.html")


# 删除成功(中成药）
@app.route('/health_food_success_delect', methods=["POST"])
def health_food_success_delect():
    name = request.form["name"]
    cur = con.cursor()
    sql1 = "select * from health_food where foodname = '" + name + "'"
    sql2 = "delete from health_food where foodname = '" + name + "'"
    cur.execute(sql1)
    data = cur.fetchall()
    if not data == []:
        cur.execute(sql2)
        cur.close()
        return render_template("success_delect.html", data1="删除药类(中成药）" + name + "基本信息成功！",
                               data2="Successfully deleted the basic information of the drug!")
    else:
        cur.close()
        return render_template("success_delect.html", data1="医药信息数据库未查询到药类（中成药）" + name + "!",
                               data2="The drug was not found in the medical information database!")


"""*****************************************************************************************************"""


# wordcloud
@app.route('/word')
def word():
    return render_template("word.html")


# echarts
@app.route('/echarts')
def echart():
    return render_template("echarts.html")


# 医药AHP安全性评价算法
@app.route('/ahp')
def ahp():
    return render_template("ahp.html")


# 医药AHP安全性评价算法(result)
@app.route('/ahp_result')
def ahp_result():
    return render_template("ahp_result.html")


if __name__ == '__main__':
    app.run()
