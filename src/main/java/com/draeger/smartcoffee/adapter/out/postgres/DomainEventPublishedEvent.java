package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.domain.event.DomainEvent;
import org.springframework.context.ApplicationEvent;

public class DomainEventPublishedEvent extends ApplicationEvent {

    private final DomainEvent domainEvent;

    public DomainEventPublishedEvent(Object source, DomainEvent domainEvent) {
        super(source);
        this.domainEvent = domainEvent;
    }

    public DomainEvent getDomainEvent() {
        return domainEvent;
    }
}
