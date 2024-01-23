<script lang="ts">
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
</script>

<main class="flex flex-col w-96 h-svh p-5">
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
        <SubmitButton disabled={$processing}>
            {#if $processing}
                <Spinner></Spinner>
            {:else}
                送信
            {/if}
        </SubmitButton>
    </section>
</main>
