package com.boto.autenticacaoprofessor.model.repository;


import com.boto.autenticacaoprofessor.model.enntity.Professor;
import lombok.Data;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.orm.jpa.AutoConfigureTestEntityManager;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit.jupiter.SpringExtension;

@ExtendWith(SpringExtension.class)
@ActiveProfiles("test")
@DataJpaTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
public class ProfessorRepositoryTest {
    @Autowired
    ProfessorRepository professorRepository;
    @Autowired
    TestEntityManager entityManager;

    @Test
    public void deveVerificarExistenciaDeEmail(){
        Professor professor = Professor.builder().nome("teste").email("teste@gmail.com").senha("1234").matricula("211041295").build();
        professorRepository.save(professor);

        boolean resultado = professorRepository.existsByEmail("teste@gmail.com");

        Assertions.assertThat(resultado).isTrue();

    }

    @Test
    public void deveRetornarFalsoQuandoNaoHouverEmailCadastrado(){
        professorRepository.deleteAll();

        boolean resultado = professorRepository.existsByEmail("teste@gmail.com");

        Assertions.assertThat(resultado).isFalse();
    }

}

