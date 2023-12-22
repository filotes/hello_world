from flask import Flask, render_template
import random

app = Flask(__name__)

ls = ['胡桃', '达达利亚', '钟离', '雷电将军', '巴巴托斯', '枫原万叶', '班尼特', '尤拉', '迪卢克', '纳西妲']


@app.route("/index")
def index():
    return render_template("index.html", ls=ls)


@app.route("/chuojiang")
def chuojiang():
    nums = random.randint(0, len(ls) - 1)
    return render_template("index.html", ls=ls, num=ls[nums])


app.run(debug=True)
