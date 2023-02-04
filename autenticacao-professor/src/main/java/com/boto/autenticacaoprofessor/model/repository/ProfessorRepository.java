package com.boto.autenticacaoprofessor.model.repository;
import com.boto.autenticacaoprofessor.model.entity.Professor;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ProfessorRepository extends JpaRepository<Professor,Long> {
    boolean existsByEmail(String email);

    Optional<Professor> findByEmail(String email);

    boolean existsByMatricula(String matricula);

}
