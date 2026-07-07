package com.migrationplatform.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.migrationplatform.agent.LanguageMigrationAgent;
import com.migrationplatform.generator.GeneratedFile;
import com.migrationplatform.model.MigrationRequest;
import com.migrationplatform.service.MigrationPlannerService;

@RestController

@RequestMapping("/api/migration")

public class MigrationController {

	@Autowired
	private MigrationPlannerService plannerService;

	@Autowired
	private LanguageMigrationAgent languageMigrationAgent;

	@PostMapping("/execute")
	public ResponseEntity<List<GeneratedFile>> executeMigration(
	       @RequestBody MigrationRequest request) {
	   return ResponseEntity.ok(
	           languageMigrationAgent.migrate(request));
	}
}
