from flask import Flask
from flask import make_response
from flask import request
import requests
import json
import os
demo=Flask(__name__)
@demo.route('/webhook',methods=['post'])
def webhook():
    r=request.get_json(silent=True,force=True)
    q=makeresponse(r)
    g=make_response(q)
    g.headers['content-type']='application/json'
    return g
def makeresponse(r):
    result = r.get("queryResult")
    output=result.get("outputContexts")[0]
    parameter = output.get("parameters")
    comp=parameter.get("company_name")
    namm=parameter.get("employee_name")
    print(namm)
    defaultasn="no such company existed"
    r=requests.get('https://soonapi.herokuapp.com/api')
    q=r.json()
    que=q["list"]
    for j in range(0,5):
        loo=que[j]
        company=loo["company"]
        if(company==comp):
            print(company)
            employee=loo["employee details"]
            for i in range(0,5):
                details=employee[i]
                name=details["name"]
                if(namm==name):
                    print(name)
                    state=details["state"]
                    print(state)
                    
    answers="emloyee name is %s and he is from %s  company and he is from %s city"%(namm,comp,state)
    print(answers)
    return{
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        answers
                        ]
                    }
                }
            ]
        }
if __name__=='__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    demo.run(debug=True, port=port, host='0.0.0.0')
