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

class LeaderList(Resource):
	def get(self):
		return ["Associació Leader de Ponent",
"Associació pel Desenvolupament Rural de la Catalunya Central",
"Associació per al Desenvolupament Rural Integral de la zona Nord‐Oriental de Catalunya",
"Associació per la Gestió del Programa Leader Ripollès Ges Bisaura",
"Consorci GAL Alt Urgell – Cerdanya",
"Consorci Grup d’Acció Local Noguera ‐ Segrià Nord",
"Consorci Intercomarcal d’Iniciatives Socioeconòmiques",
"Consorci Leader de Desenvolupament Rural del Camp",
"Consorci Leader Pirineu Occidental",
"Consorci pel al Desenvolupament del Baix Ebre i Montsià",
"Consorci per al Desenvolupament de la Catalunya Central"]

class ComarcaList(Resource):
	def get(self):
		return ["Alt Camp",
"Alt Empordà",
"Alt Penedès",
"Alt Urgell",
"Alta Ribagorça",
"Anoia",
"Bages",
"Baix Camp",
"Baix Ebre",
"Baix Empordà",
"Baix Llobregat",
"Baix Penedès",
"Barcelonès",
"Berguedà",
"Cerdanya",
"Conca de Barberà",
"Garraf",
"Les Garrigues",
"Garrotxa",
"Gironès",
"Maresme",
"Moianès",
"Montsià",
"Noguera",
"Osona",
"Pallars Jussà",
"Pallars Sobirà",
"Pla de l'Estany",
"Pla d'Urgell",
"Priorat",
"Ribera d'Ebre",
"Ripollès",
"Segarra",
"Segrià",
"Selva",
"Solsonès",
"Tarragonès",
"Terra Alta",
"Urgell",
"Val d'Aran (Vall d'Aran)",
"Vallès Occidental",
"Vallès Oriental"]

class PropostasList(Resource):
	def get(self):
		return {"Recursos": {
				"cat": ["Implementar una estratègia de sostenibilitat que permeti optimitzar l'ús de recursos reduint la quantitat de materials necessaris per la fabricació i prioritzant matèries primeres sostenibles i de qualitat.",
					"Analitzar l'impacte ambiental de les matèries primeres per identificar punts febles i estudiar alternatives més sostenibles, eficients i econòmiques."
				],
				"es": ["Implementar una estrategia de sostenibilidad que permita optimizar el uso de recursos reduciendo la cantidad de materiales necesarios para la fabricación y priorizando materias primas sostenibles y de calidad.",
					"Analizar el impacto ambiental de las materias primas para identificar puntos débiles y estudiar alternativas más sostenibles, eficientes y económicas."
				]
			},
			"Fabricació i distribució": {
				"cat": ["Analitzar els processos de fabricació i distribució per trobar millores potencials que permetin reduir l'ús de matèries primeres, energia, residus i emissions, estalviant costos i minimitzant l'impacte ambiental.",
					"Analitzar l'impacte ambiental dels productes per identificar punts febles i aplicar estratègies d'ecodisseny que permetin complir normatives, estalviar costos i reduir el seu impacte."
				],
				"es": ["Analizar los procesos de fabricación y distribución para encontrar mejoras potenciales que permitan reducir el uso de materias primas, energía, residuos y emisiones, ahorrando costes y minimizando el impacto ambiental.",
					"Analizar el impacto ambiental de los productos para identificar puntos débiles y aplicar estrategias de ecodiseño que permitan cumplir normativas, ahorrar costes y reducir su impacto."
				]
			},
			"Ús": {
				"cat": ["Ecodissenyar una o més categories de producte per allargar la seva vida útil, minimitzant l'impacte ambiental, fidelitzant els clients i millorant la competitivitat i la percepció social de l'empresa.",
					"Estudiar noves línies de negoci basades en la servitització, minimitzant l'impacte ambiental de l'empresa i estalviant costos derivats de la compra de matèries primeres noves alhora que s'amplien els models de negoci i s'augmenta la interacció positiva amb els clients."
				],
				"es": ["Ecodiseñar una o más categorías de producto para alargar su vida útil, minimizando el impacto ambiental, fidelizando los clientes y mejorando la competitividad y la percepción social de la empresa.",
					"Estudiar nuevas líneas de negocio basadas en la servitización, minimizando el impacto ambiental de la empresa, ahorrando costes derivados de la compra de materias primas nuevas a la vez que se amplían los modelos de negocio y se aumenta la interacción positiva con los clientes."
				]
			},

			"Reparació": {
				"cat": ["Estudiar com millorar el potencial de reparació dels productes del catàleg, analitzant els avantatges socials, econòmics i ambientals.",
					"Analitzar i redefinir el catàleg de productes de l'empresa per determinar i prioritzar aquells productes que destaquin per la seva durabilitat i potencial de reparació."
				],
				"es": ["Estudiar cómo mejorar el potencial de reparación de los productos del catálogo, analizando las ventajas sociales, económicas y ambientales.",
					"Analizar y redefinir el catálogo de productos de la empresa para determinar y priorizar aquellos productos que destaquen por su durabilidad y potencial de reparación."
				]
			},

			"Reús": {
				"cat": ["Analitzar la millora ambiental i econòmica que suposa la substitució de línies de negoci associades a productes no pensats per la reutilització en comparació amb nous models pensats per minimitzar la necessitat de matèries primeres i energia a través d'aquesta estratègia.",
					"Realitzar un estudi de les estratègies de reús utilitzades per les empreses del sector i com integrar-les per millorar la competitivitat de l'empresa."
				],
				"es": ["Analizar la mejora ambiental y económica que supone la sustitución de líneas de negocio asociadas a productos no pensados para la reutilización en comparación con nuevos modelos pensados para minimizar la necesidad de materias primas y energía a través de esta estrategia.",
					"Reun estudio de las estrategias de reutilización utilizadas por las empresas del sector y cómo integrarlas para mejorar la competitividad de la empresa."
				]
			},

			"Remanufactura": {
				"cat": ["Analitzar la millora ambiental i econòmica que suposa la substitució de línies de negoci associades a productes no pensats per la remanufactura en comparació amb nous models dissenyats per a minimitzar la necessitat de matèries primeres i energia a través d'aquesta estratègia.",
					"Realitzar un estudi de les estratègies de remanufactura utilitzades per les empreses del sector i com integrar-les per millorar la competitivitat de l'empresa."
				],
				"es": ["Analizar la mejora ambiental y económica que supone la sustitución de líneas de negocio asociadas a productos no pensados para la remanufactura en comparación con nuevos modelos pensados para minimizar la necesidad de materias primas y energía a través de esta estrategia.",
					"Realizar un estudio de las estrategias de remanufactura utilizadas por las empresas del sector y cómo integrarlas para mejorar la competitividad de la empresa."
				]
			},

			"Reciclatge": {
				"cat": ["Ecodissenyar una o més categories de producte per determinar materials que poden ser substituïts per altres materials reciclables, minimitzant l'impacte ambiental, fidelitzant els clients i millorant la competitivitat i la percepció social de l'empresa.",
					"Realitzar un estudi dels materials reciclables utilitzats per les empreses del sector i com integrar-los per millorar la competitivitat de l'empresa."
				],
				"es": ["Ecodiseñar una o más categorías de producto para determinar materiales que pueden ser sustituidos por otros materiales reciclables, minimizando el impacto ambiental, fidelizando los clientes y mejorando la competitividad y la percepción social de la empresa.",
					"Realizar un estudio de los materiales reciclables utilizados por las empresas del sector y cómo integrarlos para mejorar la competitividad de la empresa."
				]
			}
		}
