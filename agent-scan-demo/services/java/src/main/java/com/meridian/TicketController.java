package com.meridian;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * REST endpoints for support tickets.
 */
@RestController
@RequestMapping("/api/tickets")
public class TicketController {

    /** Simple ticket data-transfer object. */
    public record TicketDto(long id, String subject, String status, int priority) {}

    private final List<TicketDto> tickets = new ArrayList<>(List.of(
        new TicketDto(1, "Login fails", "open", 2),
        new TicketDto(2, "Export broken", "open", 2),
        new TicketDto(3, "Feature request", "open", 0),
        new TicketDto(4, "Password reset loop", "open", 3)
    ));

    @GetMapping
    public List<TicketDto> listOpen() {
        return tickets.stream().filter(t -> t.status().equals("open")).toList();
    }

    @GetMapping("/{id}")
    public TicketDto get(@PathVariable long id) {
        return tickets.stream()
            .filter(t -> t.id() == id)
            .findFirst()
            .orElse(null);
    }

    @PostMapping
    public TicketDto create(@RequestBody Map<String, Object> payload) {
        long id = tickets.size() + 1;
        TicketDto dto = new TicketDto(
            id,
            String.valueOf(payload.getOrDefault("subject", "")),
            "open",
            (int) payload.getOrDefault("priority", 0)
        );
        tickets.add(dto);
        return dto;
    }
}
