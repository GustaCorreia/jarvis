from app.core.identity import identity
from app.core.mission import MISSION
from app.core.principles import PRINCIPLES


class JarvisCore:
    """
    Núcleo da identidade do Jarvis.

    Centraliza todas as informações fundamentais sobre o sistema.
    """

    def who_am_i(self):
        return identity

    def mission(self):
        return MISSION

    def principles(self):
        return PRINCIPLES
