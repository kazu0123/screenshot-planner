<button type="button" on:click>
    <slot />
</button>

<style>
    button {
        --sky-50: rgb(240 249 255);
        --sky-300: rgb(125 211 252);
        --sky-600: rgb(2 132 199);

        width: 100%;
        height: 4rem;
        outline: none;

        background-color: var(--sky-600);

        border-radius: 0.5rem;
        border-width: 2px;
        border-color: var(--sky-50);

        color: var(--sky-50);
        font-size: 1.5rem;
        line-height: 2rem;
        font-weight: 500;
    }

    button:active {
        background-color: var(--sky-50);

        border-color: var(--sky-600);
        color: var(--sky-600);
    }

    button:focus {
        box-shadow: 0 0 0 4px var(--sky-300);
    }
</style>
