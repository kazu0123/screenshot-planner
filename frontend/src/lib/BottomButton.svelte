<script lang="ts">
    import { EditOutline, CameraFotoOutline, MicrophoneOutline } from 'flowbite-svelte-icons';

    export let icon: "text" | "camera" | "microphone";
</script>

<div>
    {#if icon === "text"}
        <EditOutline class="w-12 h-12 text-sky-600 outline-none" />
    {:else if icon === "microphone"}
        <MicrophoneOutline class="w-12 h-12 text-sky-600 outline-none" />
    {:else}
        <CameraFotoOutline class="w-12 h-12 text-sky-600 outline-none" />
    {/if}
</div>

<style>
    div {
        --sky-50: rgb(240 249 255);
        --sky-600: rgb(2 132 199);

        display: flex;
        justify-content: center;
        align-items: center;

        width: 6rem;
        height: 6rem;
        outline: none;

        background-color: var(--sky-50);

        border-radius: calc(infinity * 1px);
        border-width: 2px;
        border-color: var(--sky-600);

        color: var(--sky-600);
    }
</style>
