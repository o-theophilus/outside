<script>
	import { backend } from '$lib/store.js';
	export let meta;
</script>

<section>
	<img src="{backend}/photo/{meta.id}/thumbnail" alt={meta.id} />
	<div class="details">
		<div class="label">
			<span>id </span>
			<span>gender </span>
			<span>ethnicity </span>
			<span>hair </span>
			<span>eyebrow </span>
			<span>eye </span>
			<span>nose </span>
			<span>mouth </span>
			<span>costume </span>
			<span>background </span>
		</div>

		<div class="value">
			<span>{meta.id}</span>
			<span>{meta.gender}</span>
			<span>{meta.ethnicity}</span>
			<span>{meta.hair}</span>
			<span>{meta.eyebrow}</span>
			<span>{meta.eye}</span>
			<span>{meta.nose}</span>
			<span>{meta.mouth}</span>
			<span>{meta.costume}</span>
			<span>{meta.background}</span>
		</div>
	</div>
</section>

<style>
	img {
		border-radius: var(--brad1);
	}
	
	section,
	.details,
	.label,
	.value {
		display: flex;
	}
	
	section {
		gap: var(--gap2);
		background-color: gray;
		border-radius: var(--brad1);

		padding: var(--gap2);
	}

	.details {
		gap: var(--gap2);
		font-size: small;
	}

	section,
	.label,
	.value {
		flex-direction: column;
	}
</style>
