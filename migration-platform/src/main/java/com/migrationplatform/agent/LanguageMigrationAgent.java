package com.migrationplatform.agent;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.migrationplatform.generator.CSharpClassGenerator;
import com.migrationplatform.generator.GeneratedFile;
import com.migrationplatform.model.ClassMetadata;
import com.migrationplatform.model.MigrationRequest;

@Service
public class LanguageMigrationAgent {

	@Autowired
	private CSharpClassGenerator csharpGenerator;

	public List<GeneratedFile> migrate(MigrationRequest request) {
	   List<GeneratedFile> files = new ArrayList<>();
	   for (ClassMetadata cls : request.getClasses()) {
	       GeneratedFile file = csharpGenerator.generate(cls);
	       files.add(file);

	       System.out.println("----------------------------------------");
	       System.out.println("Generated : " + file.getFileName());
	       System.out.println(file.getContent());
	   }
	   return files;
	}
}