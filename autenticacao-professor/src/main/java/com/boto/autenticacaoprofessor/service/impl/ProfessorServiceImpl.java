package com.boto.autenticacaoprofessor.service.impl;

import com.boto.autenticacaoprofessor.exception.ErroAutenticacao;
import com.boto.autenticacaoprofessor.exception.RegraDeNegocioException;
import com.boto.autenticacaoprofessor.model.enntity.Professor;
import com.boto.autenticacaoprofessor.model.repository.ProfessorRepository;
import com.boto.autenticacaoprofessor.service.ProfessorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@Service
public class ProfessorServiceImpl implements ProfessorService {

    ProfessorRepository repository;
    @Autowired
    public ProfessorServiceImpl(ProfessorRepository professorRepository) {
        super();
        this.repository = professorRepository;
    }

    @Override
    public Professor autenticar(String email, String senha) {
        Optional<Professor> professor = repository.findByEmail(email);
        if(!professor.isPresent()){
            throw new ErroAutenticacao("Usuario não encontrado para o email informado");
        }

        if (!professor.get().getSenha().equals(senha)){
            throw new ErroAutenticacao("Senha invalida");
        }
        return professor.get();
    }

    @Override
    @Transactional
    public Professor salvarProfessor(Professor professor) {
        validarEmail(professor.getEmail());
        return repository.save(professor);
    }

    @Override
    public void validarEmail(String email) {
        boolean existe = repository.existsByEmail(email);
        if (existe){
            throw new RegraDeNegocioException("Email já cadastrado");
        }
    }
}
