<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Hero from '$lib/components/Hero.svelte';
	import Services from '$lib/components/Services.svelte';
	import Projects from '$lib/components/Projects.svelte';
	import About from '$lib/components/About.svelte';
	import Contact from '$lib/components/Contact.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<svelte:head>
	<title>Code Pasture | Full-Stack Development 0 → 1</title>
	<meta name="description" content="Custom mobile apps and microservices, cultivated with 30 years of experience. From first commit to production." />
</svelte:head>

<Header />

<main>
	<Hero />
	<Services />
	<Projects />
	<About />
	<Contact />
</main>

<Footer />
