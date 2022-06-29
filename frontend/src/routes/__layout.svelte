<script>
	import '$lib/css/var.css';
	import '$lib/css/main.css';
	import Nav from '$lib/nav.svelte';

	let innerWidth;
	let scrollY;
</script>

<svelte:window bind:innerWidth bind:scrollY />
<main>
	<Nav />
	<slot />
</main>

<style>
</style>
