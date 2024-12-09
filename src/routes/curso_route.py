from src.controllers.curso_controller import CursoController
from flask_restx import Namespace
from src.common.utils import api

def CursoRoute(api):
    
    ns_curso = Namespace("curso", description="Curso operations")
    
    
    ns_curso.add_resource(CursoController, '')
    
    api.add_namespace(ns_curso)