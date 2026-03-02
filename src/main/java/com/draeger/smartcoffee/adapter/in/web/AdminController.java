package com.draeger.smartcoffee.adapter.in.web;

import com.draeger.smartcoffee.adapter.out.postgres.ProjectionRebuildService;
import com.draeger.smartcoffee.application.port.in.RebuildResultDto;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/admin")
public class AdminController {

    private final ProjectionRebuildService rebuildService;

    public AdminController(ProjectionRebuildService rebuildService) {
        this.rebuildService = rebuildService;
    }

    @PostMapping("/projections/rebuild")
    public ResponseEntity<RebuildResultDto> rebuildProjections() {
        RebuildResultDto result = rebuildService.rebuildAll();
        return ResponseEntity.ok(result);
    }
}
