package com.boto.autenticacaoprofessor.service;

import com.boto.autenticacaoprofessor.model.enntity.Professor;

public interface ProfessorService {
    Professor autenticar(String email,String senha);

    Professor salvarProfessor(Professor professor);

    void validarEmail(String email);
}
