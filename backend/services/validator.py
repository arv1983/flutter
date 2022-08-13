

class Validator:
    def base(requered: dict, data: dict):
        requered = [req for req in requered if req not in data]
        
        if requered:
            response = {
                "erro": "Faltam campos obrigatórios",
                "recebido": [inf for inf in data],
                "faltantes": {
                    "Campos": requered,
                },
            },
            
            return response      
  
    def register_validator(data: dict):
        REGISTER = ["nome", "email", "senha"]
        return Validator.base(REGISTER, data)



