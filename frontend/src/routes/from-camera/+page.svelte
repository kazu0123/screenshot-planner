<script lang="ts">
    import { goto } from "$app/navigation";
    import { isCalendarEvent, type CalendarEvent } from "$lib/CalendarEvent";
    import SubmitButton from "$lib/SubmitButton.svelte";
    import { Spinner } from "flowbite-svelte";
    import { writable } from "svelte/store";

    const processing = writable(false);

    let files: FileList;
    let imageURI = "";

    function updateImageURI(event: Event) {
        URL.revokeObjectURL(imageURI);

        const file = files.item(0);
        if (file == null) { return }

        imageURI = URL.createObjectURL(file);
    }

    async function imageToText(image: File): Promise<string> {
        const file = files.item(0);
        if (file == null) { throw new Error("file is null"); }

        const formData = new FormData();
        formData.append("file",file);

        const requestURL = new URL("http://127.0.0.1:8000/image-to-text");

        const response = await fetch(requestURL, {
            method: "POST",
            body: formData,
        });

        const result = await response.text();
        
        return result
    }

    async function textToCalendarEvents(text: string): Promise<CalendarEvent[]> {
        const requestURL = new URL("http://127.0.0.1:8000/parse-event-details");
        requestURL.searchParams.append("message", text);

        const response = await fetch(requestURL, {
            method: "POST",
        });

        const data = await response.json();

        if (!Array.isArray(data) || !data.every(isCalendarEvent)) {
            throw new Error("Unexpected response format from /parse-event-details");
        }

        return data
    }

    async function handleClick(event: MouseEvent) {
        $processing = true;

        const file = files.item(0);
        if (file == null) { return }

        const text = await imageToText(file);
        const calendarEvents = await textToCalendarEvents(text);

        sessionStorage.setItem("calendarEvents", JSON.stringify(calendarEvents));

        goto("/event-confirm");
    }
</script>

<section class="w-full grow">
    <h1 class="w-full mb-5 text-4xl">画像から</h1>
    {#if imageURI == ""}
        <p>画像をアップロードしてください</p>
    {:else}
        <img src="{imageURI}" alt="" class="w-full">
    {/if}
</section>
<section class="w-full">
    <input bind:files={files} type="file" capture="environment" on:change={updateImageURI}>
    <SubmitButton disabled={$processing} on:click={handleClick}>
        {#if $processing}
            <Spinner></Spinner>
        {:else}
            送信
        {/if}
    </SubmitButton>
</section>
