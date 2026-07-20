from app.core.core import JarvisCore


class JarvisService:
    """
    Serviço responsável por fornecer informações
    institucionais sobre o Jarvis.
    """

    def __init__(self):
        self.core = JarvisCore()

    def about(self) -> dict:
        identity = self.core.who_am_i()

        return {
            "name": identity.name,
            "version": identity.version,
            "creator": identity.creator,
            "description": identity.description,
            "mission": self.core.mission(),
            "principles": self.core.principles(),
        }
