from src.controllers.carrera_curso_controller import CarreraCursoController
from flask_restx import Namespace
from src.common.utils import api

def CarreraCursoRoute(api):
    
    ns_carreracurso = Namespace("carrera_curso", description="CarreraCurso operations")
    
    
    ns_carreracurso.add_resource(CarreraCursoController, '')
    
    api.add_namespace(ns_carreracurso)