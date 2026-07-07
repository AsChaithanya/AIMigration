package com.migrationplatform.rules.javatocsharp;

import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Component;
import com.migrationplatform.rules.MigrationRule;
import com.migrationplatform.rules.MigrationRuleRepository;

@Component
public class JavaToCSharpRuleRepository implements MigrationRuleRepository {
	private final Map<String, MigrationRule> rules = new HashMap<>();

	public JavaToCSharpRuleRepository() {
		rules.put("JFrame",
				new MigrationRule("JFrame", "Controller + Razor View", "UI", "Convert Swing screen to ASP.NET MVC"));
		rules.put("JButton", new MigrationRule("JButton", "Button", "UI", "Convert to HTML Button"));
		rules.put("JTextField", new MigrationRule("JTextField", "TextBox", "UI", "Convert to HTML Input"));
		rules.put("JComboBox", new MigrationRule("JComboBox", "Select", "UI", "Convert to HTML Select"));
		rules.put("ActionListener",
				new MigrationRule("ActionListener", "Controller Action", "Event", "Generate ASP.NET Action"));
		rules.put("Serializable", new MigrationRule("Serializable", "DTO", "Model", "Generate C# DTO"));
	}

	@Override
	public MigrationRule getRule(String javaType) {
		return rules.get(javaType);
	}
}