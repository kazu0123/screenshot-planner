<script lang="ts">
    import { onMount } from 'svelte';
    import { writable, type Writable } from "svelte/store";

    import { isCalendarEvent, type CalendarEvent } from "$lib/CalendarEvent";

    import SubmitButton from '$lib/SubmitButton.svelte';

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

    async function submitCalendarEvents() {
        const responses = $calendarEvents.map((calendarEvent) => {
            return fetch("http://127.0.0.1:8000/create-event", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(calendarEvent),
            });
        });

        const eventURLs = await Promise.all( responses.map( async (response) => (await response).text()) );

        eventURLs.forEach((eventURL, index) => {
            console.log(index, eventURL);
        });
    }
</script>

<h1 class="w-full mb-5 text-4xl">イベント登録確認</h1>

<ul class="w-full h-full grow overflow-y-scroll">
{#each $calendarEvents as calendarEvent}
    <li>
        <h2 class="text-2xl my-3">{calendarEvent.event_title}</h2>

        <div>
            <p>開始日時</p>
            <p>{calendarEvent.start_datetime}</p>
        </div>

        <div>
            <p>終了日時</p>
            <p>{calendarEvent.end_datetime}</p>
        </div>

        <div>
            <p>実施場所</p>
            <p>{calendarEvent.event_location}</p>
        </div>

        <div>
            <p>繰り返し</p>
            <p>{calendarEvent.recurrence}</p>
        </div>

        <div>
            <p>追加情報</p>
            <p>{calendarEvent.event_description}</p>
        </div>
    </li>
{/each}
</ul>

<SubmitButton on:click={submitCalendarEvents}>カレンダーに登録</SubmitButton>

<style>
    li > div :first-child {
        background-color: rgb(241 245 249);
    }
</style>
