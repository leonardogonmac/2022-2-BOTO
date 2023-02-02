package com.boto.autenticacaoprofessor.conntroller.dto;

import lombok.*;

@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ProfessorDto {
    private String nome;
    private String email;
    private String matricula;
    private String senha;
}
