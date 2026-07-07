package com.migrationplatform.generator;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.migrationplatform.model.ClassMetadata;
import com.migrationplatform.model.ConstructorMetadata;
import com.migrationplatform.model.FieldMetadata;
import com.migrationplatform.model.MethodMetadata;

@Component
public class CSharpClassGenerator implements CodeGenerator {


	@Autowired
	private TypeMapper typeMapper;

	@Override
	public GeneratedFile generate(ClassMetadata cls) {
	   StringBuilder sb = new StringBuilder();
	   sb.append("public class ")
	     .append(cls.getName());
	   // Handle inheritance
	   if (cls.getExtendsClass() != null &&
	           !cls.getExtendsClass().isBlank()) {
	       sb.append(" : ")
	         .append(convertBaseClass(cls.getExtendsClass()));
	   }
	   sb.append("\n{\n\n");
	   // Generate properties
	   if (cls.getFields() != null) {
	       for (FieldMetadata field : cls.getFields()) {
	           sb.append("    public ")
	             .append(typeMapper.map(field.getType()))
	             .append(" ")
	             .append(capitalize(field.getName()))
	             .append(" { get; set; }\n\n");
	       }
	   }

	   // Generate Constructors
	   generateConstructors(cls, sb);

	   // Generate Methods
	   generateMethods(cls, sb);

	   sb.append("}");
	   return new GeneratedFile(
	           cls.getName() + ".cs",
	           sb.toString());
	}

		private String capitalize(String value) {
		   if (value == null || value.isEmpty())
		       return value;
		   return Character.toUpperCase(value.charAt(0))
		           + value.substring(1);
		}

		private String convertBaseClass(String base) {
			switch (base) {
			case "JFrame":
				return "Controller";
			default:
				return base;
			}
		}

		private void generateConstructors(ClassMetadata cls, StringBuilder sb) {
			if (cls.getConstructors() == null)
				return;
			for (ConstructorMetadata constructor : cls.getConstructors()) {
				sb.append("    public ").append(cls.getName()).append("()").append("\n    {\n").append("    }\n\n");
			}
		}

		private void generateMethods(ClassMetadata cls, StringBuilder sb) {
			if (cls.getMethods() == null)
				return;
			for (MethodMetadata method : cls.getMethods()) {
				sb.append("    public ").append(typeMapper.map(method.getReturnType())).append(" ")
						.append(capitalize(method.getName())).append("()").append("\n    {\n");
				sb.append("        // TODO: Convert Java logic\n");
				sb.append("    }\n\n");
			}
		}

		private String generateInterfaces(ClassMetadata cls) {
			if (cls.getImplementsList() == null || cls.getImplementsList().isEmpty())
				return "";
			return " : I" + cls.getImplementsList().get(0);
		}
}