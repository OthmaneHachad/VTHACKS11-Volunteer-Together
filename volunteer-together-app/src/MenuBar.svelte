<script>
    // Any reactive statements or functions for menu actions can go here.
    export let items = []; // Optionally receive an array of items for the menu
</script>

<style>
    .menu-bar {
        display: flex;
        justify-content: center; /* This will center the items */
        align-items: center;
        width: 100%;
        padding: 10px 20px;
        background-color: rgba(0, 0, 0, 0.0); /* 20% black opacity */
        position: absolute;
        top: 0;
        gap: 150px; /* Space between menu items */
        z-index: 2; /* Making sure it's above most of the content */
    }

    .menu-item {
        display: flex; /* This is to ensure menu items are horizontally displayed */
        
    }

    .menu-bar a {
        color: black;
        font-weight: bold;
        text-decoration: none;
    }

    /* Hover effect for menu items */
    .menu-bar a:hover {
        text-decoration: underline;
    }
</style>

<div class="menu-bar">
    {#each items as item}
        <a href={item.href} class="menu-item">{item.label}</a>
    {/each}
</div>
