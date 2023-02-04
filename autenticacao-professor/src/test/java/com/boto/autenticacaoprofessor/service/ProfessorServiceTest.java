package com.boto.autenticacaoprofessor.service;

import java.util.Optional;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mockito;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.boot.test.mock.mockito.SpyBean;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import com.boto.autenticacaoprofessor.exception.ErroAutenticacao;
import com.boto.autenticacaoprofessor.exception.RegraDeNegocioException;
import com.boto.autenticacaoprofessor.model.entity.Professor;
import com.boto.autenticacaoprofessor.model.repository.ProfessorRepository;
import com.boto.autenticacaoprofessor.service.impl.ProfessorServiceImpl;

@ExtendWith(SpringExtension.class)
@ActiveProfiles("test")
public class ProfessorServiceTest{
    @SpyBean
    ProfessorServiceImpl service;

    @MockBean
    ProfessorRepository repository;

    @Test
    public void deveSalvarUmProfessor() {
        //cenário
        Mockito.doNothing().when(service).validarEmail(Mockito.anyString());
        Professor professor = Professor.builder()
                .id(1l)
                .nome("nome")
                .email("email@email.com")
                .senha("senha")
                .matricula("111111111").build();

        Mockito.when(repository.save(Mockito.any(Professor.class))).thenReturn(professor);

        //acao
        Professor professorSalvo = service.salvarProfessor(new Professor());

        //verificao
        Assertions.assertThat(professorSalvo).isNotNull();
        Assertions.assertThat(professorSalvo.getId()).isEqualTo(1l);
        Assertions.assertThat(professorSalvo.getNome()).isEqualTo("nome");
        Assertions.assertThat(professorSalvo.getEmail()).isEqualTo("email@email.com");
        Assertions.assertThat(professorSalvo.getSenha()).isEqualTo("senha");
        Assertions.assertThat(professorSalvo.getMatricula()).isEqualTo("111111111");
    }

}