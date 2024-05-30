package com.jiyasoft.project.lowcode;

import java.util.HashMap;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONObject;

class JsonTypeHandlerFactory {
    private static final Map<Class<?>, JsonTypeHandler> handlerMap = new HashMap<>();

    static {
        handlerMap.put(JSONObject.class, new JsonObjectHandler());
        handlerMap.put(JSONArray.class, new JsonArrayHandler());
        handlerMap.put(String.class, new JsonStringHandler());
        handlerMap.put(Integer.class, new JsonIntegerHandler());
        handlerMap.put(Boolean.class, new JsonBooleanHandler());
        handlerMap.put(Double.class, new JsonDoubleHandler());
        handlerMap.put(Long.class, new JsonLongHandler());
    }

    public static JsonTypeHandler getHandler(Object value) {
        return handlerMap.getOrDefault(value.getClass(), new JsonUnknownHandler());
    }
}
