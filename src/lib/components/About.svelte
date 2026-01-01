<script lang="ts">
	const stack = [
		{
			title: 'Languages',
			items: ['TypeScript', 'Dart', 'C# / F#', 'Go']
		},
		{
			title: 'Frontend',
			items: ['Vue.js', 'React', 'Svelte']
		},
		{
			title: 'Mobile',
			items: ['Flutter', 'React Native', 'Expo']
		},
		{
			title: 'Backend',
			items: ['.NET 8', 'Go-Gin', 'Node/Express']
		},
		{
			title: 'Infrastructure',
			items: ['Kubernetes', 'Docker', 'NGINX', 'Azure DevOps', 'GitHub Actions']
		}
	];
</script>

<section id="about" class="about">
	<div class="section-header">
		<h2><span class="hash">#</span> About</h2>
	</div>
	<div class="about-content">
		<div class="about-text">
			<p class="about-lead">30 years of software development, now from a hobby farm in rural Michigan.</p>
			<p>I'm Nathan—architect, developer, and farmer. Between caring for chickens, goats, donkeys, turkeys, and ducks, I build software for businesses who need it done right. The farm runs on the same principles I bring to software: dedication, persistence in troubleshooting, constant learning, and genuine care—whether for code or for animals.</p>
			<p>My focus is 0-to-1 development: taking your idea from concept to production with clean architecture, comprehensive testing, and documentation that actually helps.</p>
		</div>
		<div class="about-stack">
			{#each stack as section}
				<div class="stack-section">
					<h4>{section.title}</h4>
					<ul>
						{#each section.items as item}
							<li>{item}</li>
						{/each}
					</ul>
				</div>
			{/each}
		</div>
		<a href="https://nathanfox.net" class="link-blog" target="_blank" rel="noopener">Read technical articles on nathanfox.net →</a>
	</div>
</section>

<style>
	.about {
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

	.about-content {
		display: grid;
		gap: 2rem;
	}

	.about-text {
		max-width: 650px;
	}

	.about-lead {
		font-size: 1.15rem;
		color: var(--color-text);
		margin-bottom: 1rem;
		font-weight: 500;
	}

	.about-text p {
		color: var(--color-text-muted);
		margin-bottom: 1rem;
		line-height: 1.7;
	}

	.about-stack {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
		gap: 1.5rem;
		padding: 1.5rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.stack-section h4 {
		font-size: 0.75rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		color: var(--color-accent);
		margin-bottom: 0.75rem;
	}

	.stack-section ul {
		list-style: none;
		padding: 0;
		margin: 0;
	}

	.stack-section li {
		padding: 0.3rem 0;
		font-size: 0.9rem;
		color: var(--color-text-muted);
	}

	.link-blog {
		display: inline-block;
		margin-top: 1rem;
		color: var(--color-accent);
		text-decoration: none;
		font-size: 0.9rem;
	}

	.link-blog:hover {
		text-decoration: underline;
	}

	@media (max-width: 768px) {
		.about {
			padding: 3rem 1.5rem;
		}

		.about-stack {
			grid-template-columns: repeat(2, 1fr);
		}
	}
</style>
