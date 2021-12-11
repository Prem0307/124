from flask import Flask,jsonify,request
app=Flask(__name__)
data=[
    {
        'contact':'99874563',
        'Name':'Raju',
        'done':False,
        'id':1
        
        
    },
    {
        'contact':'99874563',
        'name':'Raju',
        'done':False,
        'id':2
    }
]


@app.route("/add-data",methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)

    datas = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    data.append(datas)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        'data':data,
        
    })
if(__name__=='__main__'):
    app.run(debug=True,port=8000)
