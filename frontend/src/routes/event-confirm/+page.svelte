<script lang="ts">
    import { onMount } from 'svelte';
    import { writable, type Writable } from "svelte/store";
    import { isCalendarEvent, type CalendarEvent } from "$lib/CalendarEvent";

    let calendarEvents: Writable<CalendarEvent[]> = writable([]);

    function parseCalendarEventsJSON(inputText: string): CalendarEvent[] {
        let data = JSON.parse(inputText);

        if (!Array.isArray(data)) {
            throw new Error("Invalid data format. Expected an array.");
        }

        if (!data.every(isCalendarEvent)) {
            throw new Error ("Invalid calendarEvents data. Not all items are valid CalendarEvent.");
        }

        return data
    }

    onMount(() => {
        const storedData = sessionStorage.getItem("calendarEvents");
        if (storedData == null) { throw new Error("calendarEvents is null in sessionStorage."); }

        calendarEvents.set( parseCalendarEventsJSON(storedData) );
    });
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
