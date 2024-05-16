package com.jiyasoft.project.lowcode;

import org.json.JSONArray;
import org.json.JSONObject;

class JsonObjectHandler implements JsonTypeHandler {
    @Override
    public void handle(String key, Object value, int indent) {
    	JsonTypeDetector.printIndented(key + ": JSONObject", indent);
        JsonTypeDetector.determineTypes((JSONObject) value, indent + 1); // Recursive call for nested JSON objects
    }
}

class JsonArrayHandler implements JsonTypeHandler {
    @Override
    public void handle(String key, Object value, int indent) {
    	JsonTypeDetector.printIndented(key + ": JSONArray", indent);
        JsonTypeDetector.determineArrayTypes(key, (JSONArray) value, indent + 1);
    }
}

class JsonStringHandler implements JsonTypeHandler {
    @Override
    public void handle(String key, Object value, int indent) {
    	JsonTypeDetector.printIndented(key + ": String", indent);
    }
}

class JsonIntegerHandler implements JsonTypeHandler {
    @Override
    public void handle(String key, Object value, int indent) {
    	JsonTypeDetector.printIndented(key + ": Integer", indent);
    }
}

class JsonBooleanHandler implements JsonTypeHandler {
    @Override
    public void handle(String key, Object value, int indent) {
    	JsonTypeDetector.printIndented(key + ": Boolean", indent);
    }
}

class JsonDoubleHandler implements JsonTypeHandler {
    @Override
    public void handle(String key, Object value, int indent) {
    	JsonTypeDetector.printIndented(key + ": Double", indent);
    }
}

class JsonLongHandler implements JsonTypeHandler {
    @Override
    public void handle(String key, Object value, int indent) {
    	JsonTypeDetector.printIndented(key + ": Long", indent);
    }
}

class JsonUnknownHandler implements JsonTypeHandler {
    @Override
    public void handle(String key, Object value, int indent) {
    	JsonTypeDetector.printIndented(key + ": Unknown Type", indent);
    }
}
