package com.migrationplatform.model;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonProperty;

public class MigrationRequest {
	private Metadata metadata;
	private FileInfo file;
	private List<String> imports;
	private List<ClassMetadata> classes;
	private List<Relationship> relationships;

	@JsonProperty("business_entities")
	private List<String> businessEntities;

	@JsonProperty("business_flow")
	private List<String> businessFlow;
	private MigrationInfo migration;
	private Rag rag;

	public Metadata getMetadata() {
		return metadata;
	}

	public void setMetadata(Metadata metadata) {
		this.metadata = metadata;
	}

	public FileInfo getFile() {
		return file;
	}

	public void setFile(FileInfo file) {
		this.file = file;
	}

	public List<String> getImports() {
		return imports;
	}

	public void setImports(List<String> imports) {
		this.imports = imports;
	}

	public List<ClassMetadata> getClasses() {
		return classes;
	}

	public void setClasses(List<ClassMetadata> classes) {
		this.classes = classes;
	}

	public List<Relationship> getRelationships() {
		return relationships;
	}

	public void setRelationships(List<Relationship> relationships) {
		this.relationships = relationships;
	}

	public List<String> getBusinessEntities() {
		return businessEntities;
	}

	public void setBusiness_entities(List<String> businessEntities) {
		this.businessEntities = businessEntities;
	}

	public List<String> getBusinessFlow() {
		return businessFlow;
	}

	public void setBusinessFlow(List<String> businessFlow) {
		this.businessFlow = businessFlow;
	}

	public MigrationInfo getMigration() {
		return migration;
	}

	public void setMigration(MigrationInfo migration) {
		this.migration = migration;
	}

	public Rag getRag() {
		return rag;
	}

	public void setRag(Rag rag) {
		this.rag = rag;
	}

}