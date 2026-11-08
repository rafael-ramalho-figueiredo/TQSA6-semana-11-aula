mydict = self.__dict__;
    mydict['turma'] = [i.__dict__ for i in self.turma]
    mydict['menorNota'] = self.menorNota.__dict__;
    mydict['maiorNota'] = self.maiorNota.__dict__;
    x = conexao[colecao].insert_one(mydict)    
    return x.acknowledged;
