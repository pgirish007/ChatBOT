package com.jiyasoft.project.lowcode;

import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONTokener;

import java.util.Iterator;

public class JsonTypeDetector {

    public static void main(String[] args) {
        // Example JSON string
        String jsonString = "{\n"
        		+ "	\"items\":\n"
        		+ "		{\n"
        		+ "			\"item\":\n"
        		+ "				[\n"
        		+ "					{\n"
        		+ "						\"id\": \"0001\",\n"
        		+ "						\"type\": \"donut\",\n"
        		+ "						\"name\": \"Cake\",\n"
        		+ "						\"ppu\": 0.55,\n"
        		+ "						\"batters\":\n"
        		+ "							{\n"
        		+ "								\"batter\":\n"
        		+ "									[\n"
        		+ "										{ \"id\": \"1001\", \"type\": \"Regular\" },\n"
        		+ "										{ \"id\": \"1002\", \"type\": \"Chocolate\" },\n"
        		+ "										{ \"id\": \"1003\", \"type\": \"Blueberry\" },\n"
        		+ "										{ \"id\": \"1004\", \"type\": \"Devil's Food\" }\n"
        		+ "									]\n"
        		+ "							},\n"
        		+ "						\"topping\":\n"
        		+ "							[\n"
        		+ "								{ \"id\": \"5001\", \"type\": \"None\" },\n"
        		+ "								{ \"id\": \"5002\", \"type\": \"Glazed\" },\n"
        		+ "								{ \"id\": \"5005\", \"type\": \"Sugar\" },\n"
        		+ "								{ \"id\": \"5007\", \"type\": \"Powdered Sugar\" },\n"
        		+ "								{ \"id\": \"5006\", \"type\": \"Chocolate with Sprinkles\" },\n"
        		+ "								{ \"id\": \"5003\", \"type\": \"Chocolate\" },\n"
        		+ "								{ \"id\": \"5004\", \"type\": \"Maple\" }\n"
        		+ "							]\n"
        		+ "					},\n"
        		+ "\n"
        		+ "					...\n"
        		+ "\n"
        		+ "				]\n"
        		+ "		}\n"
        		+ "}";

        // Create a JSONObject from the string
        JSONObject jsonObject = new JSONObject(new JSONTokener(jsonString));

        // Call the method to determine types
        determineTypes(jsonObject, 0);
    }

    public static void determineTypes(JSONObject jsonObject, int indent) {
        // Iterate over keys in the JSON object
        Iterator<String> keys = jsonObject.keys();
        while (keys.hasNext()) {
            String key = keys.next();
            Object value = jsonObject.get(key);

            JsonTypeHandler handler = JsonTypeHandlerFactory.getHandler(value);
            handler.handle(key, value, indent);
        }
    }

    public static void determineArrayTypes(String key, JSONArray jsonArray, int indent) {
        for (int i = 0; i < jsonArray.length(); i++) {
            Object value = jsonArray.get(i);

            JsonTypeHandler handler = JsonTypeHandlerFactory.getHandler(value);
            handler.handle(key + "[" + i + "]", value, indent);
        }
    }

    public static void printIndented(String message, int indent) {
        for (int i = 0; i < indent; i++) {
            System.out.print("    "); // 4 spaces per indent level
        }
        System.out.println(message);
    }
}



