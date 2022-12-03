def carregar_dados(collection:str):
    if collection == "servidor":
        dados = "{'id_servidor':'001','nome':'PEGASUS'}
        "{'id_servidor':'002','nome':'THOR'}"
        "{'id_servidor':'003','nome':'FENIX'}"
    elif collection == "conta":
        dados = "{'id_conta':'08595','id_servidor':'001','nome':'os_melhores','email':'lucas@gmail.com'}"
        "{'id_conta':'25478','id_servidor':'001','nome':'tudorapido','email':'joao@gmail.com'}"
        "{'id_conta':'54007','id_servidor':'001','nome':'magadoteclado','email':'marcela@outlook.com'}"
        "{'id_conta':'45472','id_servidor':'002','nome':'tornadoVermelho','email':'thais@gmail.com'}"
        "{'id_conta':'24879','id_servidor':'002','nome':'magicoDEoz','email':'marco@gmail.com'}"
        "{'id_conta':'65478','id_servidor':'003','nome':'familiar','email':'ana@gmail.com'}"
        "{'id_conta':'15327','id_servidor':'003','nome':'voandobaixo','email':'vicente@outlook.com'}"
        "{'id_conta':'28954','id_servidor':'003','nome':'lanche.da.tarde','email':'antonio@gmail.com'}"
        "{'id_conta':'75498','id_servidor':'003','nome':'giro_duplo','email':'teobaldo@outlook.com'}"
        
    elif collection == "personagem":
        dados = "{'id_personagem':'DFGT','id_conta':'25478','nome':'GorilaAbacate','nivel':'18', 'classe':'mago'}"
        "{'id_personagem':'KLSD','id_conta':'25478','nome':'FormigaPera','nivel':'20', 'classe':'paladino'}"
        "{'id_personagem':'PERR','id_conta':'25478','nome':'LeãoAbobora','nivel':'25', 'classe':'arqueiro'}"
        "{'id_personagem':'SDIU','id_conta':'08595','nome':'TigreFeliz','nivel':'18', 'classe':'mago'}"
        "{'id_personagem':'MKLF','id_conta':'08595','nome':'OncaUva','nivel':'49', 'classe':'mago'}"
        "{'id_personagem':'SYDE','id_conta':'15327','nome':'TomateAvestruz','nivel':'102', 'classe':'arqueiro'}"
        "{'id_personagem':'XCKJ','id_conta':'15327','nome':'TucanoRoxo','nivel':'78', 'classe':'tank'}"
        "{'id_personagem':'LKCV','id_conta':'15327','nome':'GirafaVerde','nivel':'43', 'classe':'tank'}"
        "{'id_personagem':'SOPD','id_conta':'75498','nome':'PagaioLaranja','nivel':'57', 'classe':'paladino'}"
        "{'id_personagem':'HUDF','id_conta':'24879','nome':'PelicanoTorresmo','nivel':'82', 'classe':'elfo'}"

    return dados