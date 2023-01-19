package com.boto.autenticacaoprofessor.conntroller.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class ProfessorDto {
    private String nome;
    private String email;
    private String senha;
    private String matricula;
}
