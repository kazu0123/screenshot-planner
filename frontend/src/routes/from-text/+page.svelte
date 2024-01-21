<script lang="ts">
    import SubmitButton from "$lib/SubmitButton.svelte";
</script>

<main class="flex flex-col w-96 h-svh p-5">
    <section class="w-full grow">
        <h1 class="w-full mb-5 text-4xl">テキストから</h1>
        <textarea
            class="rounded-lg border-2 border-sky-500 w-full h-80 resize-none"
            placeholder="予定の情報を入力"
        />
    </section>
    <section class="w-full">
        <SubmitButton>送信</SubmitButton>
    </section>
</main>
