<script lang="ts">
    import { goto } from "$app/navigation";
    import { isCalendarEvent } from "$lib/CalendarEvent";
    import SubmitButton from "$lib/SubmitButton.svelte";
    import { writable } from "svelte/store";
    import { Spinner } from 'flowbite-svelte';

    const textareaValue = writable("");
    let processing = writable(false);

    async function handleClick(event: MouseEvent) {
        $processing = true;

        const requestURL = new URL("http://127.0.0.1:8000/parse-event-details");
        requestURL.searchParams.append("message", $textareaValue);

        const response = await fetch(requestURL, {
            method: "POST",
        });

        const data = await response.json();

        if (!Array.isArray(data) || !data.every(isCalendarEvent)) {
            throw new Error("Unexpected response format from /parse-event-details");
        }

        sessionStorage.setItem("calendarEvents", JSON.stringify(data));

        goto("/event-confirm");
    }
</script>

<section class="w-full grow">
    <h1 class="w-full mb-5 text-4xl">テキストから</h1>
    <textarea
        bind:value={$textareaValue}
        class="rounded-lg border-2 border-sky-500 w-full h-80 resize-none"
        placeholder="予定の情報を入力"
    />
</section>
<section class="w-full">
    <SubmitButton disabled={$processing} on:click={handleClick}>
        {#if $processing}
            <Spinner></Spinner>
        {:else}
            送信
        {/if}
    </SubmitButton>
</section>
