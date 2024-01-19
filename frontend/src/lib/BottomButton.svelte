<script lang="ts">
    import { EditOutline, CameraFotoOutline, MicrophoneOutline } from 'flowbite-svelte-icons';

    export let icon: "text" | "camera" | "microphone";
</script>

<div class="flex justify-center items-center rounded-full border-2 border-sky-500 bg-slate-100 w-24 h-24">
    {#if icon === "text"}
        <EditOutline class="w-12 h-12 text-sky-500 outline-none"></EditOutline>
    {:else if icon === "microphone"}
        <MicrophoneOutline class="w-12 h-12 text-sky-500 outline-none"></MicrophoneOutline>
    {:else}
        <CameraFotoOutline class="w-12 h-12 text-sky-500 outline-none"></CameraFotoOutline>
    {/if}
</div>
