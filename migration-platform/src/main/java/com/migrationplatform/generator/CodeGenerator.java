package com.migrationplatform.generator;

import com.migrationplatform.model.ClassMetadata;

public interface CodeGenerator {
	GeneratedFile generate(ClassMetadata cls);
}