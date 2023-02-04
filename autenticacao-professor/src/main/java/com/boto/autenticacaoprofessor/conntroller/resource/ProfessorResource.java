package com.boto.autenticacaoprofessor.conntroller.resource;

import com.boto.autenticacaoprofessor.conntroller.dto.ProfessorDto;
import com.boto.autenticacaoprofessor.exception.ErroAutenticacao;
import com.boto.autenticacaoprofessor.exception.RegraDeNegocioException;
import com.boto.autenticacaoprofessor.model.entity.Professor;
import com.boto.autenticacaoprofessor.service.ProfessorService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/professor")
public class ProfessorResource {

    private ProfessorService professorService;

    public ProfessorResource(ProfessorService professorService) {
        this.professorService = professorService;
    }

    @PostMapping
    public ResponseEntity salvar(@RequestBody ProfessorDto professorDto){
        Professor professor = Professor.builder()
                                        .nome(professorDto.getNome())
                                        .email(professorDto.getEmail())
                                        .matricula(professorDto.getMatricula())
                                        .senha(professorDto.getSenha())
                                        .build();
        try {
           Professor usuarioSalvo = professorService.salvarProfessor(professor);
           return new ResponseEntity(usuarioSalvo, HttpStatus.CREATED);
        }catch (RegraDeNegocioException e){
                return  ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @PostMapping("/login")
    public ResponseEntity autenticar(@RequestBody ProfessorDto professorDto){
        try {
        Professor  professorAutenticado = professorService.autenticar(professorDto.getEmail(), professorDto.getSenha());
        return  ResponseEntity.ok(professorAutenticado);
        }catch (ErroAutenticacao e ){
            return  ResponseEntity.badRequest().body(e.getMessage());
        }

    }

    }

