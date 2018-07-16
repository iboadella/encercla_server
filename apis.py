from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel,CompanyModel,SurveyCompanyModel

from flask import Flask, jsonify, request
from datetime import datetime
class SectorList(Resource):
    def get(self):
        return [{ "sector" : "Agroalimentari","subsector":"Agricultura i ramaderia"},
		{ "sector" : "Agroalimentari","subsector":"Pesca i caça"},
		{ "sector" : "Agroalimentari","subsector":"Productes càrnics"},
		{ "sector" : "Agroalimentari","subsector":"Fruites i hortalisses"},
		{ "sector" : "Agroalimentari","subsector":"Oli"},
		{ "sector" : "Agroalimentari","subsector":"Productes lactis"},
		{ "sector" : "Agroalimentari","subsector":"Productes de fleca"},
		{ "sector" : "Agroalimentari","subsector":"Begudes"},
		{ "sector" : "Agroalimentari","subsector":"Altres"},
		{ "sector" : "Industrial","subsector":"Fusta"},
		{ "sector" : "Industrial","subsector":"Maquinària"},
		{ "sector" : "Industrial","subsector":"Química"},
		{ "sector" : "Industrial","subsector":"Metal·lúrgia"},
		{ "sector" : "Industrial","subsector":"Tèxtil"},
		{ "sector" : "Industrial","subsector":"Construcció"},
		{ "sector" : "Industrial","subsector":"Altres"},
		{ "sector" : "Comercial","subsector":"Productes d'alimentació"},
		{ "sector" : "Comercial","subsector":"Altres productes"},
		{ "sector" : "Serveis","subsector":"Transport"},
		{ "sector" : "Serveis","subsector":"Restauració"},
		{ "sector" : "Serveis","subsector":"Allotjaments"},
		{ "sector" : "Serveis","subsector":"Reparació de vehicles"},
		{ "sector" : "Serveis","subsector":"Activitats professionals"},
		{ "sector" : "Serveis","subsector":"Activitats sanitàries"},
		{ "sector" : "Serveis","subsector":"Educació"},
		{ "sector" : "Serveis","subsector":"Entreteniment"},
		{ "sector" : "Serveis","subsector":"Altres serveis"},
		{ "sector" : "Públic","subsector":"Administració pública"},
		{ "sector" : "Altres","subsector":"altres"}]


