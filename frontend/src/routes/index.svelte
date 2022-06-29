<script context="module">
	import { backend } from '$lib/store.js';

	import Item from '$lib/Item.svelte';

	export async function load({ fetch }) {
		const _resp = await fetch(`${backend}/nft`, {
			method: 'get',
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (_resp.ok) {
			let resp = await _resp.json();

			return {
				props: {
					metas: resp.data
				}
			};
		}
	}
</script>

<script>
	export let metas;

	let length = 100;
</script>

{#each metas.slice(0, length) as meta}
	<Item {meta} />
{/each}
