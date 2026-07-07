package com.migrationplatform.model;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Metadata {

    @JsonProperty("project_name")

    private String projectName;

    private String language;

    private String framework;

    @JsonProperty("build_tool")

    private String buildTool;

    @JsonProperty("source_version")

    private String sourceVersion;

    @JsonProperty("target_language")

    private String targetLanguage;

    @JsonProperty("target_framework")

    private String targetFramework;

    private int files;

	public String getProjectName() {
		return projectName;
	}

	public void setProjectName(String projectName) {
		this.projectName = projectName;
	}

	public String getLanguage() {
		return language;
	}

	public void setLanguage(String language) {
		this.language = language;
	}

	public String getFramework() {
		return framework;
	}

	public void setFramework(String framework) {
		this.framework = framework;
	}

	public String getBuildTool() {
		return buildTool;
	}

	public void setBuildTool(String buildTool) {
		this.buildTool = buildTool;
	}

	public String getSourceVersion() {
		return sourceVersion;
	}

	public void setSourceVersion(String sourceVersion) {
		this.sourceVersion = sourceVersion;
	}

	public String getTargetLanguage() {
		return targetLanguage;
	}

	public void setTargetLanguage(String targetLanguage) {
		this.targetLanguage = targetLanguage;
	}

	public String getTargetFramework() {
		return targetFramework;
	}

	public void setTargetFramework(String targetFramework) {
		this.targetFramework = targetFramework;
	}

	public int getFiles() {
		return files;
	}

	public void setFiles(int files) {
		this.files = files;
	}



}
