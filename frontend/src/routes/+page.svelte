<script lang="ts">
    import BottomButton from "$lib/BottomButton.svelte";
</script>

<h1 class="relative bottom-24 text-4xl">予定登録アプリ</h1>
<ul class="flex absolute bottom-5">
    <li class="first:ml-0 ml-2"><a href="/from-text"><BottomButton icon="text"></BottomButton></a></li>
    <li class="first:ml-0 ml-2"><a href="/from-camera"><BottomButton icon="camera"></BottomButton></a></li>
    <li class="first:ml-0 ml-2"><a href="/from-microphone"><BottomButton icon="microphone"></BottomButton></a></li>
</ul>
