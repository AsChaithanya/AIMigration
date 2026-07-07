package com.migrationplatform.model;

import java.io.IOException;

import java.util.ArrayList;

import java.util.List;

import com.fasterxml.jackson.core.JsonParser;

import com.fasterxml.jackson.databind.DeserializationContext;

import com.fasterxml.jackson.databind.JsonDeserializer;

import com.fasterxml.jackson.databind.JsonNode;

import com.fasterxml.jackson.databind.ObjectMapper;

public class FieldMetadataListDeserializer extends JsonDeserializer<List<FieldMetadata>> {

	@Override

	public List<FieldMetadata> deserialize(JsonParser p, DeserializationContext ctxt) throws IOException {

		ObjectMapper mapper = (ObjectMapper) p.getCodec();

		JsonNode node = mapper.readTree(p);

		List<FieldMetadata> fields = new ArrayList<>();

		if (node.isArray()) {

			for (JsonNode fieldNode : node) {

				if (fieldNode.isTextual()) {

					// DTO format: "sFrom"

					FieldMetadata field = new FieldMetadata();

					field.setName(fieldNode.asText());

					fields.add(field);

				} else if (fieldNode.isObject()) {

					// UI format: { "name": "...", "type": "...", ... }

					fields.add(mapper.treeToValue(fieldNode, FieldMetadata.class));

				}

			}

		}

		return fields;

	}

}
