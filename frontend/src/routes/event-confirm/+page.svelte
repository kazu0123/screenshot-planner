<script lang="ts">
    import { writable, type Writable } from "svelte/store";
    import { type CalendarEvent } from "$lib/CalendarEvent";

    let calendarEvents: Writable<CalendarEvent[]> = writable([]);
</script>

<ul>
{#each $calendarEvents as calendarEvent}
    <li>
        <h2>{calendarEvent.event_title}</h2>
        <p>{calendarEvent.start_datetime}</p>
        <p>{calendarEvent.end_datetime}</p>
    </li>
{/each}
</ul>
