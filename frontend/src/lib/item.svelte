<script>
	import { backend } from '$lib/store.js';
	export let meta;
</script>

<section>
	<div class="img">
		<img src="{backend}/photo/{meta.id}/thumbnail" alt={meta.id} />
	</div>
	<div class="details">
		<div class="label">
			<span>id </span>
			<span>background </span>
			<span>ethnicity </span>
			<span>eye </span>
			<span>eyebrow </span>
			<span>gender </span>
			<span>hair </span>
			<span>mouth </span>
			<span>nose </span>
		</div>

		<div class="value">
			<span>{meta.id}</span>
			<span>{meta.background}</span>
			<span>{meta.ethnicity}</span>
			<span>{meta.eye}</span>
			<span>{meta.eyebrow}</span>
			<span>{meta.gender}</span>
			<span>{meta.hair}</span>
			<span>{meta.mouth}</span>
			<span>{meta.nose}</span>
		</div>


	</div>
</section>

<style>
	section,
	.details,
	.label,
	.value {
		display: flex;
	}
	section {
		background-color: gray;
		gap: var(--gap2);
		padding: var(--gap2);
	}

	section,
	.label,
	.value {
		flex-direction: column;
	}
</style>
