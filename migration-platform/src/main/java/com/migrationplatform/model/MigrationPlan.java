package com.migrationplatform.model;

import java.util.List;

public class MigrationPlan {
	private List<String> migrationOrder;

	public List<String> getMigrationOrder() {
		return migrationOrder;
	}

	public void setMigrationOrder(List<String> migrationOrder) {
		this.migrationOrder = migrationOrder;
	}
}