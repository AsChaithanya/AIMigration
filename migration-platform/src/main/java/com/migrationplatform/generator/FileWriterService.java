package com.migrationplatform.generator;

import java.io.IOException;

import java.nio.file.Files;

import java.nio.file.Path;

import java.nio.file.Paths;

import org.springframework.stereotype.Service;

@Service

public class FileWriterService {

    public void save(GeneratedFile file) throws IOException {

        Path output = Paths.get(

                "output",

                file.getFileName());

        Files.createDirectories(output.getParent());

        Files.writeString(

                output,

                file.getContent());

    }

}
