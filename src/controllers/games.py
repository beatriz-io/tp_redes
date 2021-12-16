from flask import Flask, request
from flask_restx import Api, Resource
#from werkzeug.wrappers import request
from src.server.instance import server 

app = server.app 
api = server.api 

games_db = [
    {'id': 0, 'statistics': 'a'},
    {'id': 1, 'statistics': 'a'},
    {'id': 2, 'statistics': 'a'},
    {'id': 3, 'statistics': 'a'},
    {'id': 4, 'statistics': 'a'},
    {'id': 5, 'statistics': 'a'},
    {'id': 6, 'statistics': 'a'},
    {'id': 7, 'statistics': 'a'},
    {'id': 8, 'statistics': 'a'},
    {'id': 9, 'statistics': 'a'}
]

@api.route('/api/games/<int:id>')
class Games(Resource):
    def get(self, id):
        return games_db[id]


@api.route('/api/rank/sunk')
@api.doc(params={'start': {'description': 'posição no ranking do primeiro', 'in': 'query', 'type': 'int'},
                 'end': {'description': 'posição no ranking do último', 'in': 'query', 'type': 'int'}})
class MaiorNumeroNaviosAfundados(Resource):
    def get(self):
        argumentos = request.args.to_dict()
        start = argumentos['start']
        end = argumentos['end']
        return {'start': start, 'end': end}


@api.route('/api/rank/escaped')
@api.doc(params={'start': {'description': 'posição no ranking do primeiro', 'in': 'query', 'type': 'int'},
                 'end': {'description': 'posição no ranking do último', 'in': 'query', 'type': 'int'}})
class MaiorNumeroNaviosEscapados(Resource):
    def get(self):
        argumentos = request.args.to_dict()
        start = argumentos['start']
        end = argumentos['end']
        return {'start': start, 'end': end}

