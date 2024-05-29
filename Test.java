import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.json.JsonWriteFeature;

public class Main {
    public static void main(String[] args) throws Exception {
        // Create a YAMLFactory
        YAMLFactory yamlFactory = new YAMLFactory();
        
        // Create an ObjectMapper with the YAMLFactory
        ObjectMapper objectMapper = new ObjectMapper(yamlFactory);
        
        // Disable the escaping of non-ASCII characters
        objectMapper.configure(JsonGenerator.Feature.ESCAPE_NON_ASCII, false);
        
        // Also, configure the ObjectMapper to handle backslashes properly
        objectMapper.getFactory().configure(JsonWriteFeature.ESCAPE_BACKSLASHES.mappedFeature(), false);
        
        // Create a sample object
        MyObject myObject = new MyObject();
        myObject.setName("John Doe");
        myObject.setUrl("C:\\Users\\JohnDoe\\Documents");

        // Serialize the object to YAML
        String yaml = objectMapper.writeValueAsString(myObject);
        
        // Print the YAML
        System.out.println(yaml);
    }

    // Sample class to serialize
    public static class MyObject {
        private String name;
        private String url;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getUrl() {
            return url;
        }

        public void setUrl(String url) {
            this.url = url;
        }
    }
}
