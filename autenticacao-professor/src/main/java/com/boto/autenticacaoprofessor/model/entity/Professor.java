package com.boto.autenticacaoprofessor.model.entity;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;


@Entity
@Table(name = "professor",schema = "bot")
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Data
public class Professor {

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "email")
    private String email;

    @Column(name = "nome")
    private String nome;

    @Column(name = "senha")
    private String senha;

    @Column(name = "matricula")
    private String matricula;

    @Column(name = "plano_de_ensino")
    private String plano_de_ensino;



}
