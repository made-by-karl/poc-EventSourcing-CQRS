package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.domain.event.DomainEvent;
import tools.jackson.databind.DeserializationFeature;
import tools.jackson.databind.ObjectMapper;
import tools.jackson.databind.json.JsonMapper;

class EventSerializer {

    private static final ObjectMapper MAPPER = JsonMapper.builder()
        .disable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES)
        .build();

    static String serialize(DomainEvent event) {
        try {
            return MAPPER.writeValueAsString(event);
        } catch (Exception e) {
            throw new EventSerializationException("Failed to serialize event: " + event.getEventType(), e);
        }
    }

    static DomainEvent deserialize(String json, String eventType) {
        Class<? extends DomainEvent> type = EventTypeRegistry.TYPES.get(eventType);
        if (type == null) {
            throw new EventSerializationException("Unknown event type: " + eventType, null);
        }
        try {
            return MAPPER.readValue(json, type);
        } catch (Exception e) {
            throw new EventSerializationException("Failed to deserialize event of type: " + eventType, e);
        }
    }
}
