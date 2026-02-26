package com.draeger.smartcoffee.application.port.in;

public record CaffeineAlertDto(String user, int doubleEspressosInLast2Hours) {
}
