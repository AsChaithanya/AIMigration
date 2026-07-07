package com.migrationplatform.generator;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Component;

@Component
public class TypeMapper {
	private final Map<String, String> map = new HashMap<>();

	public TypeMapper() {
		map.put("String", "string");
		map.put("int", "int");
		map.put("boolean", "bool");
		map.put("double", "double");
		map.put("float", "float");
		map.put("long", "long");
		map.put("ArrayList", "List");
		map.put("HashMap", "Dictionary");
	}

	public String map(String javaType) {
		return map.getOrDefault(javaType, javaType);
	}
}
