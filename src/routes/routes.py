from .curso_route import CursoRoute
from .carrera_curso_route import CarreraCursoRoute

def  Routes(api):

    CarreraCursoRoute(api)
    CursoRoute(api)