<script lang="ts">
    import { onMount } from "svelte";
import { writable, type Writable } from "svelte/store";

    const calendarEventURLs: Writable<string[]> = writable([]);

    function parseCalendarEventURLs(inputText: string): string[] {
        let data = JSON.parse(inputText);

        if (!Array.isArray(data)) {
            throw new Error("Invalid data format. Expected an array.");
        }
        
        if (!data.every((item: unknown): item is string  => typeof item === "string")) {
            throw new Error ("Invalid data.");
        }

        return data
    }

    onMount(() => {
        const storedData = sessionStorage.getItem("calendarEventURLs");
        if (storedData == null) { throw new Error("calendarEventURLs is null in sessionStorage."); }

        calendarEventURLs.set( parseCalendarEventURLs(storedData) );
    })
</script>

<ul>
    {#each $calendarEventURLs as calendarEventURL, index}
        <li><a class="text-blue-600 underline" target="_blank" href="{calendarEventURL}">イベント{index + 1}</a></li>
    {/each}
</ul>
