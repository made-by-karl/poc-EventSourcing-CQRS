package com.draeger.smartcoffee.adapter.out.postgres;

import com.draeger.smartcoffee.domain.event.BeansRefilled;
import com.draeger.smartcoffee.domain.event.CoffeeProduced;
import com.draeger.smartcoffee.domain.event.DomainEvent;
import com.draeger.smartcoffee.domain.event.MachineMaintained;
import com.draeger.smartcoffee.domain.event.MachineRegistered;

import java.util.Map;

class EventTypeRegistry {

    static final Map<String, Class<? extends DomainEvent>> TYPES = Map.of(
        "MachineRegistered", MachineRegistered.class,
        "CoffeeProduced",    CoffeeProduced.class,
        "BeansRefilled",     BeansRefilled.class,
        "MachineMaintained", MachineMaintained.class
    );
}
