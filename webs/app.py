from flask import Flask, render_template
import random

app = Flask(__name__)
ls = ['胡桃', '达达利亚', '钟离', '雷电将军', '巴巴托斯', '枫原万叶', '班尼特', '尤拉', '迪卢克', '纳西妲']

@app.route("/index")
def index():
    return render_template('index.html', ls = ls)

@app.route("/choujiang")
def choujiang():
    nums = random.randint(0, len[ls] - 1)
    num = (ls[nums])
    return render_template('index.html', ls = ls, num = num)

app.run(debug=True)
