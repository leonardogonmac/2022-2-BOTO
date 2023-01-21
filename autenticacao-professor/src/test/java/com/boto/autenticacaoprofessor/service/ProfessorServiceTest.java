package com.boto.autenticacaoprofessor.service;

import com.boto.autenticacaoprofessor.exception.RegraDeNegocioException;
import com.boto.autenticacaoprofessor.model.enntity.Professor;
import com.boto.autenticacaoprofessor.model.repository.ProfessorRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit.jupiter.SpringExtension;

@SpringBootTest
@ExtendWith(SpringExtension.class)
@ActiveProfiles("test")
public class ProfessorServiceTest {
    @Autowired
    ProfessorService professorService;

    @Autowired
    ProfessorRepository professorRepository;
    @Test
    public void deveValidarEmail(){
        professorRepository.deleteAll();
        professorService.validarEmail("tales@gmail.com");
    }
    @Test
    public void deveLancarErroQuandoEmailJaExiste(){
        Professor professor = Professor.builder().nome("Tales").email("talesrodrigues@gmail.com").senha("123").matricula("211041295").build();
        professorRepository.save(professor);

        professorService.validarEmail("talesrodrigues@gmail.com");

    }
}
