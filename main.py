from flask import Flask , request , jsonify 

app = Flask(__name__)

@app.route("/get-user")
def get_user():
    user_data = [
        {
        "user_id" : 471912,
        "name" : "Mulumba Moses",
        "email" : "mulumbamoses@cranecloud.io"
        },
        {
        "user_id" : 213453,
        "name" : "Kibuuka Amaal",
        "email" : "kibuukaamaal@gmail.com"
        },
        {
        "user_id" : 782633,
        "name" : "Muwanguzi Able",
        "email" : "able456@gmail.com"
        },
        {
        "user_id" : 902344,
        "name" : "Ssekadde Peter",
        "email" : "ssekapater100@gmail.com"
        },
        {
        "user_id" : 762343,
        "name" : "Macho John",
        "email" : "machojo94@gmail.com"
        },
        {
        "user_id" : 123428,
        "name" : "Kirabo Amos",
        "email" : "amoskirabo100@gmail.com"
        },
        {
        "user_id" : 112429,
        "name" : "Not Hacked",
        "email" : "nothacked@gmail.com"
        },
        {
        "user_id" : 135210,
        "name" : "Ntege Kanun",
        "email" : "ntegekkitegna@gufum.com"
        },
        {
        "user_id" : 342131,
        "name" : "Raheem Stlon",
        "email" : "raheem@students.cavendish.ac.ug"
        },
        {
        "user_id" : 423132,
        "name" : "Sod Mohamad",
        "email" : "mohdmasodo817@gmail.com"
        },
        {
        "user_id" : 511333,
        "name" : "Desire Nakalembe",
        "email" : "desirecrevandish140@gmail.com"
        },
        {
        "user_id" : 912334,
        "name" : "Daniel Mudhasi",
        "email" : "mundasidaniel@gmail.com"
        },
        {
        "user_id" : 751342,
        "name" : "Atuhire Lyn",
        "email" : "lynnettelunakish@gmail.com"
        },
        {
        "user_id" : 672436,
        "name" : "Nakalyango Angel",
        "email" : "angelnak1234@gmail.com"
        },
        {
        "user_id" : 431137,
        "name" : "Nakazibwe Buganda",
        "email" : "nakabuganda09@yahoo.com"
        },
        {
        "user_id" : 762313,
        "name" : "Lunkuse Aminah",
        "email" : "lunkuseminah500@yahoo.com"
        },
        {
        "user_id" : 873142,
        "name" : "Happy Betty",
        "email" : "bettyhapi2134@gmail.com"
        },
        {
        "user_id" : 401341,
        "name" : "Elon Moses",
        "email" : "elonmoses94@gmail.com"
        },


    ]
    
    
    ##we shall pass a query parameter as extra

    extra = request.args.get("extra")
    if extra : 
        user_data["extra"] = extra
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__" :
    app.run(debug=True)