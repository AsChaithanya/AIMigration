package com.migrationplatform.model;

import com.fasterxml.jackson.annotation.JsonProperty;

public class FileInfo {
	private String name;
	private String path;

	@JsonProperty("package")
	private String packageName;
	private String language;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getPath() {
		return path;
	}

	public void setPath(String path) {
		this.path = path;
	}

	// Maps JSON field "package"
	public String getPackageName() {
		return packageName;
	}

	public void setPackageName(String packageName) {
		this.packageName = packageName;
	}

	public String getLanguage() {
		return language;
	}

	public void setLanguage(String language) {
		this.language = language;
	}
}