from flask import Flask
from flask import Flask, render_template
import requests
import pandas as pd
import random
import csv
# app = Flask(__name__)
app=Flask(__name__,template_folder='templates')




@app.route('/')
def hello_world():
    with open("person.csv", mode='r') as infile:

        reader = csv.reader(infile, skipinitialspace=True)
        keys = next(reader)
        ret_list = []
        for row in reader:
            ret_list.append({})
            for key, value in zip(keys, row):
                ret_list[-1][key] = value
        print(ret_list)
    # return "heyyyyyy"
    return render_template("index.html", data=ret_list)

        
    # # with open("person.csv") as file:
    # #     print("fileeeeeeeeeeeeeee",file)
    # #     return render_template("index.html", csv=file)
    
    # # file_name=requests.args.get("age","sample_data")

    # # cols = ['Name', 'Email','Phone']
    # #  = pd.read_csv("Person", names = cols)

    # sample_data=pd.read_csv("person" +".csv")
    # # print("sample data name is",sample_data['Name'][0].str)
    # print("sample_dataaaaaaaaaa",sample_data)
    # json_data=sample_data.to_dict()
    # print("json dataaaaaaaaaaaaaaaa",json_data)
    # return json_data
    # # print(sample_data)
    # # return render_template("index.html", len=len(sample_data),columns=list(sample_data), content=json_data)
    # # return sample_data




    

if __name__ == "__main__":
    port = 5000 + random.randint(0, 999)
    app.run(debug=True, port=port)
    # app.run()


