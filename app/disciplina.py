class Disciplina:
    def __init__(self, codigo, nome, chs, situacao, tipo): 
        self.codigo = codigo
        self.nome = nome
        self.chs = chs
        self.situacao = situacao
        self.tipo = tipo

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "chs": self.chs,
            "situacao": self.situacao,
            "tipo": self.tipo
        }

    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getChs(self):
        return self.chs

    def getSituacao(self):
        return self.situacao
    
    def getTipo(self):
        return self.tipo
        
    def setCodigo(self, codigo):
        self.codigo = codigo

    def setNome(self, nome):
        self.nome = nome

    def setChs(self, chs):
        self.chs = chs

    def setSituacao(self, situacao):
        self.situacao = situacao

    def setTipo(self, tipo):
        self.tipo = tipo
        