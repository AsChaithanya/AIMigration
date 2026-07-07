package com.migrationplatform.planner;

import com.migrationplatform.model.ClassMetadata;

import com.migrationplatform.model.Relationship;

import org.springframework.stereotype.Component;

import java.util.*;

@Component

public class DependencyResolver {

    public List<String> resolve(List<ClassMetadata> classes,

                                List<Relationship> relationships) {

        // Graph: dependency -> dependent

        Map<String, List<String>> graph = new HashMap<>();

        // In-degree of each class

        Map<String, Integer> inDegree = new HashMap<>();

        // Initialize

        for (ClassMetadata cls : classes) {

            graph.put(cls.getName(), new ArrayList<>());

            inDegree.put(cls.getName(), 0);

        }

        // Build graph

        for (Relationship rel : relationships) {

            String dependent = rel.getFrom();

            String dependency = rel.getTo();

            if (graph.containsKey(dependency) && graph.containsKey(dependent)) {

                graph.get(dependency).add(dependent);

                inDegree.put(dependent, inDegree.get(dependent) + 1);

            }

        }

        // Queue all nodes with no dependencies

        Queue<String> queue = new LinkedList<>();

        for (String cls : inDegree.keySet()) {

            if (inDegree.get(cls) == 0) {

                queue.offer(cls);

            }

        }

        List<String> migrationOrder = new ArrayList<>();

        while (!queue.isEmpty()) {

            String current = queue.poll();

            migrationOrder.add(current);

            for (String neighbour : graph.get(current)) {

                inDegree.put(neighbour, inDegree.get(neighbour) - 1);

                if (inDegree.get(neighbour) == 0) {

                    queue.offer(neighbour);

                }

            }

        }

        // Detect circular dependency

        if (migrationOrder.size() != classes.size()) {

            throw new RuntimeException("Circular dependency detected.");

        }

        return migrationOrder;

    }

}
