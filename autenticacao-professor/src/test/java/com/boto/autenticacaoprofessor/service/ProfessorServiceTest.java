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

    @Test
    public void naoDeveSalvarUmProfessorComEmailJaCadastrado() {
        //cenario
        String email = "email@email.com";
        Professor professor = Professor.builder().email(email).build();
        Mockito.doThrow(RegraDeNegocioException.class).when(service).validarEmail(email);

        //acao
        org.junit.jupiter.api.Assertions
                .assertThrows(RegraDeNegocioException.class, () -> service.salvarProfessor(professor) ) ;

        //verificacao
        Mockito.verify( repository, Mockito.never() ).save(professor);
    }

    @Test
    public void deveAutenticarUmProfessorComSucesso() {
        //cenário
        String email = "email@email.com";
        String senha = "senha";

        Professor professor = Professor.builder().email(email).senha(senha).id(1l).build();
        Mockito.when( repository.findByEmail(email) ).thenReturn(Optional.of(professor));

        //acao
        Professor result = service.autenticar(email, senha);

        //verificacao
        Assertions.assertThat(result).isNotNull();

    }

    @Test
    public void deveLancarErroQUandoNaoEncontrarProfessorCadastradoComOEmailInformado() {

        //cenário
        Mockito.when(repository.findByEmail(Mockito.anyString())).thenReturn(Optional.empty());

        //acao
        Throwable exception = Assertions.catchThrowable( () -> service.autenticar("email@email.com", "senha") );

        //verificacao
        Assertions.assertThat(exception)
                .isInstanceOf(ErroAutenticacao.class)
                .hasMessage("Usuário não encontrado para o email informado");
    }

    @Test

    public void deveLancarErroQuandoSenhaNaoBater() {
        //cenario
        String senha = "senha";
        Professor professor = Professor.builder().email("email@email.com").senha(senha).build();
        Mockito.when(repository.findByEmail(Mockito.anyString())).thenReturn(Optional.of(professor));

        //acao
        Throwable exception = Assertions.catchThrowable( () ->  service.autenticar("email@email.com", "123") );
        Assertions.assertThat(exception).isInstanceOf(ErroAutenticacao.class).hasMessage("Senha inválida");

    }

    @Test
    public void deveValidarEmail() {
        // cenario
        Mockito.when(repository.existsByEmail(Mockito.anyString())).thenReturn(false);

        //acao
        service.validarEmail("email@email.com");
    }

    @Test
    public void deveLancarErroAoValidarEmailQuandoExistirEmailCadastrado() {
        //cenario
        Mockito.when(repository.existsByEmail(Mockito.anyString())).thenReturn(true);

        //acao
        org.junit.jupiter.api.Assertions
                .assertThrows(RegraDeNegocioException.class, () -> service.validarEmail("email@email.com"));
    }
}