package com.migrationplatform.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.migrationplatform.agent.LanguageMigrationAgent;
import com.migrationplatform.generator.GeneratedFile;
import com.migrationplatform.model.MigrationRequest;
import com.migrationplatform.planner.DependencyResolver;

@Service
public class MigrationPlannerService {

	@Autowired
	private DependencyResolver resolver;

	@Autowired
	private LanguageMigrationAgent languageMigrationAgent;

    public void process(MigrationRequest request) {

    	List<String> order =
    		       resolver.resolve(request.getClasses(),
    		                        request.getRelationships());
    		System.out.println("Migration Order");
    		order.forEach(System.out::println);

    		List<GeneratedFile> generatedFiles = languageMigrationAgent.migrate(request);

    }

}
