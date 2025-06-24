from groq import Groq
from dotenv import load_dotenv
import os
from flask import Flask,request,jsonify,render_template,redirect,session,url_for

load_dotenv()

app=Flask(__name__)

client=Groq(api_key=os.environ.get("key"))
app.secret_key=os.getenv("SECRET_KEY","fallback-secret")

@app.route("/")
def login():
    
    return render_template("login.html")

@app.route("/chatbot",methods=["GET","POST"])
def chatbot():
    if request.method == "POST":
        session["email"]=request.form.get("email")
        
        session["chatbot"]=request.form.get("chatbot")
        if(request.form.get("chatbot-cust")):
            session["chatbot"]=request.form.get("chatbot-cust")
            X=session.get("chatbot")
            print("Bot is "+X)
        
        session["info"]=request.form.get("info")
        return redirect(url_for("chatbot"))
    email=session.get("email")
    chatbot=session.get("chatbot")
    info=session.get("info")
    
    return render_template("index.html",email=email,chatbot=chatbot,info=info)
@app.route("/chat",methods=["POST"])
def chat():
    if request.method == "POST":
        data=request.get_json()
        message=data.get("message")
        print("message is ",message)
        # message=request.form["message"]
        email=session.get("email")
        chatbot=session.get("chatbot")
        print("i am chatbot name "+chatbot)
        info=session.get("info")
        responce=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role":"system","content":"You are "+chatbot+"on whatsapp"},
                {"role":"user","content":f"I am ${info} with message ${message} on whatsapp"}
            ]
        )
        print(responce.choices[0].message.content)
        return jsonify({"responce":responce.choices[0].message.content})


    

if __name__=="__main__":
    app.run(debug=True)
