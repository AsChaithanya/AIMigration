package com.migrationplatform.rules;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.migrationplatform.rules.javatocsharp.JavaToCSharpRuleRepository;
import com.migrationplatform.rules.javaupgrade.JavaUpgradeRuleRepository;

@Service
public class RuleEngine {
	@Autowired
	private JavaUpgradeRuleRepository upgradeRepository;
	@Autowired
	private JavaToCSharpRuleRepository csharpRepository;

	public MigrationRule findRule(String migrationType, String javaType) {
		if ("JAVA_UPGRADE".equalsIgnoreCase(migrationType)) {
			return upgradeRepository.getRule(javaType);
		}
		if ("JAVA_TO_CSHARP".equalsIgnoreCase(migrationType)) {
			return csharpRepository.getRule(javaType);
		}
		return null;
	}
}