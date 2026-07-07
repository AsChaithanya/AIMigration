package com.migrationplatform.rules;

public interface MigrationRuleRepository {

	MigrationRule getRule(String javaType);
}