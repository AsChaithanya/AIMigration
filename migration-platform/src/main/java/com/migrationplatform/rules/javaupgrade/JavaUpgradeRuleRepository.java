package com.migrationplatform.rules.javaupgrade;

import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Component;
import com.migrationplatform.rules.MigrationRule;
import com.migrationplatform.rules.MigrationRuleRepository;

@Component
public class JavaUpgradeRuleRepository implements MigrationRuleRepository {
	private final Map<String, MigrationRule> rules = new HashMap<>();

	public JavaUpgradeRuleRepository() {
		rules.put("Date", new MigrationRule("Date", "LocalDate", "Modernization", "Use java.time API"));
		rules.put("AnonymousClass",
				new MigrationRule("AnonymousClass", "Lambda", "Modernization", "Replace anonymous class with lambda"));
		rules.put("switch",
				new MigrationRule("switch", "Switch Expression", "Modernization", "Use Java 21 switch expression"));
	}

	@Override
	public MigrationRule getRule(String javaType) {
		return rules.get(javaType);
	}
}