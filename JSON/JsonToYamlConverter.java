import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONException;
import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

import java.util.HashMap;
import java.util.Map;

public class JsonToYamlConverter {
    public static void main(String[] args) {
        // JSON string with a backslash in the city name
        String jsonString = """
        {
            "name": "John",
            "age": 30,
            "city": "New\\\\York\\\\Manhattan",
            "skills": ["Java", "Python", "SQL"],
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "zipcode": "10001"
            },
            "projects": [
                {"name": "Project A", "duration": "6 months"},
                {"name": "Project B", "duration": "3 months"}
            ]
        }
        """;

        try {
            // Step 1: Parse the JSON
            JSONObject jsonObject = new JSONObject(jsonString);

            // Step 2: Convert JSON Object to Map
            Map<String, Object> map = jsonToMap(jsonObject);

            // Step 3: Convert Map to YAML
            DumperOptions options = new DumperOptions();
            options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
            Yaml yaml = new Yaml(options);
            String yamlString = yaml.dump(map);

            System.out.println(yamlString);
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    // Function to convert JSONObject to Map
    public static Map<String, Object> jsonToMap(JSONObject jsonObject) throws JSONException {
        Map<String, Object> map = new HashMap<>();

        for (String key : jsonObject.keySet()) {
            Object value = jsonObject.get(key);
            if (value instanceof JSONArray) {
                value = jsonToList((JSONArray) value);
            } else if (value instanceof JSONObject) {
                value = jsonToMap((JSONObject) value);
            }
            map.put(key, value);
        }

        return map;
    }

    // Function to convert JSONArray to List
    public static Object jsonToList(JSONArray array) throws JSONException {
        java.util.List<Object> list = new java.util.ArrayList<>();
        for (int i = 0; i < array.length(); i++) {
            Object value = array.get(i);
            if (value instanceof JSONArray) {
                value = jsonToList((JSONArray) value);
            } else if (value instanceof JSONObject) {
                value = jsonToMap((JSONObject) value);
            }
            list.add(value);
        }
        return list;
    }
}

/**
<dependencies>
    <!-- JSON-java for JSON processing -->
    <dependency>
        <groupId>org.json</groupId>
        <artifactId>json</artifactId>
        <version>20210307</version>
    </dependency>
    <!-- SnakeYAML for YAML processing -->
    <dependency>
        <groupId>org.yaml</groupId>
        <artifactId>snakeyaml</artifactId>
        <version>2.2</version>
    </dependency>
</dependencies>
*/
