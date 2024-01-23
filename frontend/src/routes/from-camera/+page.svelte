<script lang="ts">
    import SubmitButton from "$lib/SubmitButton.svelte";
    import { Spinner } from "flowbite-svelte";
    import { writable } from "svelte/store";

    const processing = writable(false);
</script>

<main class="flex flex-col w-96 h-svh p-5">
    <section class="w-full grow">
        <h1 class="w-full mb-5 text-4xl">画像から</h1>
    </section>
    <section class="w-full">
        <SubmitButton disabled={$processing}>
            {#if $processing}
                <Spinner></Spinner>
            {:else}
                送信
            {/if}
        </SubmitButton>
    </section>
</main>
