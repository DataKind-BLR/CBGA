'''
CBGA Analytics Center Web App

AUTHOR: Suhas, <github.com/jargnar>
LICENSE: MIT
'''
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

displayNameDocumentMap = {
    "Department of Agricultural Research and Education": "Department of Agricultural Research and Education.sequences.csv",
    "Department of Health and Family Welfare": "Department of Health and Family Welfare.sequences.csv",
    "Department of Rural Development": "Department of Rural Development.sequences.csv",
    "Department of School Education and Literacy": "Department of School Education and Literacy.sequences.csv",
    "Department of Urban Development": "Department of Urban Development.sequences.csv",
    "Ministry of  Drinking Water and Sanitation": "Ministry of  Drinking Water and Sanitation.sequences.csv",
    "Ministry of Women and Child Development": "Ministry of Women and Child Development.sequences.csv"
}


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/outlook')
def outlook():
    doc = request.args.get('doc')
    if doc:
        return render_template('outlook.html', document_name=displayNameDocumentMap[doc],
                               document_options=displayNameDocumentMap.keys())
    return render_template('outlook.html', document_options=displayNameDocumentMap.keys())


@app.route('/trend')
def trend():
    return render_template('trend.html')


@app.route('/data/<path:path>')
def send_data(path):
    return send_from_directory('data', path)


if __name__ == '__main__':
    app.run(debug=True)
