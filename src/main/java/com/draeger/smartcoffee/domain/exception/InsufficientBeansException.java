package com.draeger.smartcoffee.domain.exception;

public class InsufficientBeansException extends RuntimeException {

    public InsufficientBeansException(String message) {
        super(message);
    }
}
