<script lang="ts">
	const services: {
		tag: string;
		title: string;
		description: string;
		tech: string[];
		link?: string;
	}[] = [
		{
			tag: 'mfe-architecture',
			title: 'Micro-Frontend Shell',
			description:
				'Break free from frontend monoliths. Svelte 5 shells with native ES modules, team autonomy, and independent deployability.',
			tech: ['svelte-5', 'es-modules', 'k8s'],
			link: '/mfe-shell/'
		},
		{
			tag: 'mobile',
			title: 'Mobile Development',
			description:
				'Native-quality mobile apps for iOS, Android, and web. From first commit to App Store.',
			tech: ['flutter', 'react-native', 'expo']
		},
		{
			tag: 'backend',
			title: 'Microservices',
			description:
				'0-to-1 backend development. Domain-driven design with 100% test coverage, every time.',
			tech: ['.net', 'c#', 'f#', 'go', 'node']
		},
		{
			tag: 'infrastructure',
			title: 'Cloud & DevOps',
			description:
				'Kubernetes orchestration, Docker containers, CI/CD pipelines. Production-ready from day one.',
			tech: ['k8s', 'docker', 'nginx', 'azure-devops', 'github-actions']
		},
		{
			tag: 'ai-assisted',
			title: 'GenAI Development',
			description:
				'Modern AI-assisted workflows. Pattern-driven architecture that accelerates delivery.',
			tech: ['claude', 'tdd', 'patterns']
		}
	];
</script>

<section id="services" class="services">
	<div class="section-header">
		<h2><span class="hash">#</span> What Grows Here</h2>
		<p class="section-subtitle">Full-stack development from the ground up</p>
	</div>
	<div class="services-grid">
		{#each services as service}
			<div class="service-card">
				<div class="service-header">
					<span class="service-tag">{service.tag}</span>
				</div>
				<h3>{service.title}</h3>
				<p>{service.description}</p>
				<div class="service-tech">
					{#each service.tech as tech}
						<code>{tech}</code>
					{/each}
				</div>
				{#if service.link}
					<a href={service.link} class="service-link">Learn More &rarr;</a>
				{/if}
			</div>
		{/each}
	</div>
</section>

<style>
	.services {
		padding: 5rem 2rem;
		max-width: var(--max-width);
		margin: 0 auto;
		border-top: 1px solid var(--color-border);
	}

	.section-header {
		margin-bottom: 2rem;
	}

	.section-header h2 {
		font-size: 1.5rem;
		font-weight: 600;
		margin-bottom: 0.5rem;
	}

	.hash {
		color: var(--color-text-muted);
		margin-right: 0.25rem;
	}

	.section-subtitle {
		color: var(--color-text-muted);
		font-size: 0.95rem;
	}

	.services-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
		gap: 1.25rem;
	}

	.service-card {
		padding: 1.5rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		transition: border-color var(--transition-fast), transform var(--transition-fast);
	}

	.service-card:hover {
		border-color: var(--color-accent);
		transform: translateY(-2px);
	}

	.service-header {
		margin-bottom: 0.75rem;
	}

	.service-tag {
		font-family: var(--font-mono);
		font-size: 0.7rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		color: var(--color-accent);
		background: rgba(124, 179, 66, 0.15);
		padding: 0.25rem 0.5rem;
		border-radius: var(--radius-sm);
	}

	.service-card h3 {
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.5rem;
	}

	.service-card p {
		color: var(--color-text-muted);
		font-size: 0.9rem;
		margin-bottom: 1rem;
		line-height: 1.6;
	}

	.service-tech {
		display: flex;
		flex-wrap: wrap;
		gap: 0.5rem;
	}

	.service-tech code {
		font-family: var(--font-mono);
		font-size: 0.75rem;
		color: var(--color-text-muted);
		background: var(--color-bg);
		padding: 0.2rem 0.5rem;
		border-radius: var(--radius-sm);
		border: 1px solid var(--color-border);
	}

	.service-link {
		display: inline-block;
		margin-top: 1rem;
		font-size: 0.85rem;
		font-weight: 500;
		color: var(--color-accent);
		transition: opacity var(--transition-fast);
	}

	.service-link:hover {
		opacity: 0.8;
	}

	@media (max-width: 768px) {
		.services {
			padding: 3rem 1.5rem;
		}
	}
</style>
