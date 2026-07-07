package com.migrationplatform.model;

import com.fasterxml.jackson.annotation.JsonProperty;

public class MigrationInfo {

	@JsonProperty("source_framework")
	private String sourceFramework;

	@JsonProperty("recommended_target")
	private String recommendedTarget;

	@JsonProperty("ui_type")
	private String uiType;

	@JsonProperty("migration_complexity")
	private String migrationComplexity;

	private double confidence;

	@JsonProperty("migration_type")
	private String migrationType;

	@JsonProperty("source_version")
	private String sourceVersion;

	@JsonProperty("target_version")
	private String targetVersion;

	public String getSourceFramework() {
		return sourceFramework;
	}

	public void setSourceFramework(String sourceFramework) {
		this.sourceFramework = sourceFramework;
	}

	public String getRecommendedTarget() {
		return recommendedTarget;
	}

	public void setRecommendedTarget(String recommendedTarget) {
		this.recommendedTarget = recommendedTarget;
	}

	public String getUiType() {
		return uiType;
	}

	public void setUiType(String uiType) {
		this.uiType = uiType;
	}

	public String getMigrationComplexity() {
		return migrationComplexity;
	}

	public void setMigrationComplexity(String migrationComplexity) {
		this.migrationComplexity = migrationComplexity;
	}

	public double getConfidence() {
		return confidence;
	}

	public void setConfidence(double confidence) {
		this.confidence = confidence;
	}
}
