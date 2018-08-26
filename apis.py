from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel,CompanyModel,SurveyCompanyModel

from flask import Flask, jsonify, request
from datetime import datetime
class SectorList(Resource):
    def get(self):
        return [{ "sector" : "Agroalimentari","subsector":"Agricultura i ramaderia","info":"Conreus, vivers, producció ramadera, producció agrícola combinada amb la producció ramadera, activitats de suport a l'agricultura, ramaderia i preparació posterior a la collita"},
		{ "sector" : "Agroalimentari","subsector":"Pesca i caça","info":"Pesca, aqüicultura i caça"},
		{ "sector" : "Agroalimentari","subsector":"Productes càrnics","info":"Sacrifici de bestiar i conservació de carn i elaboració de productes càrnics"},
		{ "sector" : "Agroalimentari","subsector":"Fruites i hortalisses","info":"Preparació i conservació de fruites i hortalisses"},
		{ "sector" : "Agroalimentari","subsector":"Oli","info":"Fabricació d'oli d'oliva"},
		{ "sector" : "Agroalimentari","subsector":"Productes lactis","info":"Elaboració de gelats, fabricació de formatges, preparació de llet i altres productes lactis"},
		{ "sector" : "Agroalimentari","subsector":"Productes de fleca","info":"Pa, productes de fleca i pastes alimentàries"},
		{ "sector" : "Agroalimentari","subsector":"Begudes","info":"Cervesa, vins, sidra, begudes analcohòliques, aigües minerals i altres tipus d'aigües embotellades"},
		{ "sector" : "Agroalimentari","subsector":"Altres","info":"Elaboració i conservació de peix, crustacis i mol·luscos\n Fabricació d'olis (excepte d'oliva) i greixos\n Fabricació de productes per l'alimentació animal\n Indústries del tabac\n"},
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


