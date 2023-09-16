<script>
    import MenuBar from './MenuBar.svelte';

    import { onMount } from 'svelte';

    let items = Array(30).fill().map((_, i) => i + 1);

    onMount(() => {
        const container = document.getElementById('infinite-scroll-container');

        container.addEventListener('scroll', (e) => {
            if (container.scrollTop + container.clientHeight >= container.scrollHeight) {
                // User has scrolled to the bottom, load more items
                const lastItem = items[items.length - 1];
                for (let i = 1; i <= 10; i++) {
                    items = [...items, lastItem + i];
                }
            }
        });
    });

    
</script>

<MenuBar items={[{href: '/dashboardMap', label: 'Map'},{href: '/feed', label: 'Feed'}]} />



<div id="infinite-scroll-container" class="scroll-container">
    {#each items as item}
        <div class="item">{item}</div>
    {/each}
</div>

<style>
    .scroll-container {
        height: 300px;
        overflow-y: scroll;
        border: 1px solid black;
        width: 200px;
    }

    .item {
        padding: 10px;
        border-bottom: 1px solid #ccc;
    }
</style>

