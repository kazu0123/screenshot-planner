<script lang="ts">
    import { writable, type Writable } from "svelte/store";
    import { isCalendarEvent, type CalendarEvent } from "$lib/CalendarEvent";

    let calendarEvents: Writable<CalendarEvent[]> = writable([]);

    function loadCalendarEvents() {
        const storedData = sessionStorage.getItem("calendarEvents");
        if (!storedData) {
            console.error("No calendarEvents data found in sessionStorage.");
            return false;
        }

        let data;
        try {
            data = JSON.parse(storedData);
        } catch (error) {
            console.error("Error parsing JSON data:", error);
            return false;
        }

        if (!Array.isArray(data)) {
            console.error("Invalid calendarEvents data format. Expected an array.");
            return false;
        }

        if (data.length === 0) {
            calendarEvents.set([]);
            return true;
        }

        if (data.every(isCalendarEvent)) {
            calendarEvents.set(data);
            return true;
        } else {
            console.error("Invalid calendarEvents data. Not all items are valid CalendarEvent.");
            return false;
        }
    }
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
