from flask import Flask ,render_template,request,redirect,url_for
app=Flask(__name__)


@app.route("/")
def welcome():
    return "<h1>Welcome to the flask program</h1>"

@app.route("/about",methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form["name"]
        return f"Hello {name}"
    return render_template("form.html")

@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else: 
        res="FAIL"
    return render_template("success.html",results=res)


@app.route("/success_res/<int:score>")
def success_res(score):
    res=""
    if score>=50:
        res="PASS"
    else: 
        res="FAIL"
    exp={"score":score,"res":res}
    return render_template("success1.html",results=exp)

@app.route("/success_if/<int:score>")
def success_if(score):
    return render_template("success2.html",results=score)

@app.route("/get_results",methods=["POST","GET"])
def get_results():
    total_score=0
    for i in request.form.values():
        total_score=total_score+int(i)
        print(total_score)
    total_score/=4
    return  redirect(url_for("success_if",score=total_score))

@app.route("/form1")
def form1():
    return render_template("form1.html")



if __name__=="__main__":
    app.run(debug=True)