package com.migrationplatform.rules;

public class MigrationRule {
	private String javaType;
	private String csharpType;
	private String category;
	private String migrationStrategy;

	public MigrationRule() {
	}

	public MigrationRule(String javaType, String csharpType, String category, String migrationStrategy) {
		this.javaType = javaType;
		this.csharpType = csharpType;
		this.category = category;
		this.migrationStrategy = migrationStrategy;
	}

	public String getJavaType() {
		return javaType;
	}

	public String getCsharpType() {
		return csharpType;
	}

	public String getCategory() {
		return category;
	}

	public String getMigrationStrategy() {
		return migrationStrategy;
	}
}