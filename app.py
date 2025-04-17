from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def home():
    return "welcome"
@app.route('/register',methods=['POST','GET'])
def register():
    if register.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(f"user will login {username} with {'email'}")
        return f"successfully register"
    return render_template(sucess.html)
if __name__ == '__main__':
    app.run(debug=True)
