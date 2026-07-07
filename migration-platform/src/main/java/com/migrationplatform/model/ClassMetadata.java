package com.migrationplatform.model;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;

public class ClassMetadata {
	private String name;
	private String type;
	@JsonProperty("extends")
	private String extendsClass;
	@JsonProperty("implements")
	private List<String> implementsList;
	private String purpose;

	@JsonDeserialize(using = FieldMetadataListDeserializer.class)
	private List<FieldMetadata> fields;
	private List<ConstructorMetadata> constructors;
	private List<MethodMetadata> methods;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getExtendsClass() {
		return extendsClass;
	}

	public void setExtendsClass(String extendsClass) {
		this.extendsClass = extendsClass;
	}

	public List<String> getImplementsList() {
		return implementsList;
	}

	public void setImplementsList(List<String> implementsList) {
		this.implementsList = implementsList;
	}

	public String getPurpose() {
		return purpose;
	}

	public void setPurpose(String purpose) {
		this.purpose = purpose;
	}

	public List<FieldMetadata> getFields() {
		return fields;
	}

	public void setFields(List<FieldMetadata> fields) {
		this.fields = fields;
	}

	public List<ConstructorMetadata> getConstructors() {
		return constructors;
	}

	public void setConstructors(List<ConstructorMetadata> constructors) {
		this.constructors = constructors;
	}

	public List<MethodMetadata> getMethods() {
		return methods;
	}

	public void setMethods(List<MethodMetadata> methods) {
		this.methods = methods;
	}
}