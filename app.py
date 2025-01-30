from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from scrap import Scrap

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.Memo_Pad

@app.route('/')
def home():
   return render_template('note-pad.html')

@app.route('/api/save', methods=['POST'])
def save():
    url_receive = request.form['url_give']
    scrap = Scrap(url_receive)
    comment_receive = request.form['comment_give']

    doc = {
        'url': url_receive,
        'comment': comment_receive,
        'url_image': scrap.url_image(),
        'url_title': scrap.url_title(),
        'url_description': scrap.url_description()
    }    
    db.memo.insert_one(doc)

    return jsonify({'result':'success', 'msg': '저장 완료!'})

@app.route('/api/memo', methods=['GET'])
def memo():
    memo_list = list(db.memo.find({}))
    
    for memo in memo_list:
        memo['_id'] = str(memo['_id'])  # ObjectId를 문자열로 변환
        
    return jsonify({'result': 'success', 'memo_list': memo_list})

@app.route('/api/delete', methods=['POST'])
def delete():
    id_receive = request.form['id_give']
    db.memo.delete_one({'_id': ObjectId(id_receive)})
    return jsonify({'result': 'success', 'msg': '삭제 완료!'})

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)