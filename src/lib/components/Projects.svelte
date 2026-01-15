<script lang="ts">
	const apps = [
		{
			name: 'DevHours',
			description: 'Development time tracking by project',
			tech: 'react-native',
			color: 'purple',
			appStore: 'https://apps.apple.com/us/app/devhours/id6756197386',
			playStore: null
		},
		{
			name: 'HayTracker',
			description: 'Inventory management for hay and straw bales',
			tech: 'flutter',
			color: 'green',
			appStore: 'https://apps.apple.com/us/app/haytracker/id6757104455',
			playStore: null
		},
		{
			name: 'Propane Tracker',
			description: 'Tank monitoring and delivery tracking',
			tech: 'flutter',
			color: 'orange',
			appStore: 'https://apps.apple.com/us/app/propanetracker/id6757357644',
			playStore: 'https://play.google.com/store/apps/details?id=com.codepasture.propane_tracker&hl=en_US'
		}
	];

	const openSource = [
		{
			category: 'Reference Architectures',
			projects: [
				{ name: 'MFE Svelte Shell', desc: 'Micro-frontend shell example', url: 'https://github.com/nathanfox/mfe-svelte-shell-example' },
				{ name: 'Rapid UI Prototype', desc: 'GenAI rapid prototyping system', url: 'https://github.com/nathanfox/rapid-ui-prototype-example' }
			]
		},
		{
			category: 'Developer Tools',
			projects: [
				{ name: 'PulseURL', desc: 'URL traffic analytics for microservices', url: 'https://github.com/pulseurl' },
				{ name: 'k8s-vscode-remote-debug', desc: 'Multi-language K8s debugging', url: 'https://github.com/nathanfox/k8s-vscode-remote-debug' },
				{ name: 'nginx-dev-gateway', desc: 'Lightweight K8s API gateway', url: 'https://github.com/nathanfox/nginx-dev-gateway' },
				{ name: 'env-run', desc: 'Environment management (Bash)', url: 'https://github.com/nathanfox/env-run' },
				{ name: 'env-run-pwsh', desc: 'Environment management (PowerShell)', url: 'https://github.com/nathanfox/env-run-pwsh' }
			]
		}
	];
</script>

<section id="projects" class="projects">
	<div class="section-header">
		<h2><span class="hash">#</span> Recent Harvest</h2>
		<p class="section-subtitle">Apps in production</p>
	</div>

	<div class="apps-list">
		{#each apps as app}
			<div class="app-row">
				<div class="app-name">
					<span class="app-indicator {app.color}"></span>
					{app.name}
				</div>
				<div class="app-desc">{app.description}</div>
				<div class="app-meta">
					<code>{app.tech}</code>
					{#if app.appStore || app.playStore}
						<div class="store-badges">
							{#if app.appStore}
								<a href={app.appStore} target="_blank" rel="noopener" class="store-badge">
									<img src="/app-store-badge.svg" alt="Download on the App Store" />
								</a>
							{/if}
							{#if app.playStore}
								<a href={app.playStore} target="_blank" rel="noopener" class="store-badge">
									<img src="/google-play-badge.png" alt="Get it on Google Play" />
								</a>
							{/if}
						</div>
					{:else}
						<span class="platforms">Coming Soon</span>
					{/if}
				</div>
			</div>
		{/each}
	</div>

	<div class="open-source">
		<h3><span class="hash">#</span> Open Source</h3>
		{#each openSource as category}
			<div class="os-category">
				<h4>{category.category}</h4>
				<ul>
					{#each category.projects as project}
						<li>
							<a href={project.url} target="_blank" rel="noopener">{project.name}</a>
							<span class="os-desc">{project.desc}</span>
						</li>
					{/each}
				</ul>
			</div>
		{/each}
	</div>
</section>

<style>
	.projects {
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

	.apps-list {
		display: flex;
		flex-direction: column;
		gap: 1px;
		background: var(--color-border);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		overflow: hidden;
		margin-bottom: 3rem;
	}

	.app-row {
		display: grid;
		grid-template-columns: 180px 1fr auto;
		align-items: center;
		gap: 2rem;
		padding: 1.25rem 1.5rem;
		background: var(--color-bg-elevated);
		transition: background var(--transition-fast);
	}

	.app-row:hover {
		background: var(--color-bg-hover);
	}

	.app-name {
		font-weight: 600;
		display: flex;
		align-items: center;
		gap: 0.75rem;
	}

	.app-name a {
		color: var(--color-text);
		text-decoration: none;
	}

	.app-name a:hover {
		color: var(--color-accent);
	}

	.app-indicator {
		width: 10px;
		height: 10px;
		border-radius: 50%;
		flex-shrink: 0;
	}

	.app-indicator.green {
		background: var(--color-accent);
	}

	.app-indicator.orange {
		background: var(--color-orange);
	}

	.app-indicator.purple {
		background: var(--color-purple);
	}

	.app-desc {
		color: var(--color-text-muted);
		font-size: 0.9rem;
	}

	.app-meta {
		display: flex;
		align-items: center;
		gap: 1rem;
	}

	.app-meta code {
		font-family: var(--font-mono);
		font-size: 0.75rem;
		color: var(--color-accent);
		background: rgba(124, 179, 66, 0.15);
		padding: 0.2rem 0.5rem;
		border-radius: var(--radius-sm);
	}

	.platforms {
		color: var(--color-text-muted);
		font-size: 0.8rem;
	}

	.store-badges {
		display: flex;
		gap: 0.5rem;
		align-items: center;
	}

	.store-badge img {
		height: 28px;
		opacity: 0.9;
		transition: opacity var(--transition-fast);
	}

	.store-badge img[src*="google-play"] {
		height: 42px;
		margin: -7px 0;
	}

	.store-badge:hover img {
		opacity: 1;
	}

	.open-source h3 {
		font-size: 1.25rem;
		font-weight: 600;
		margin-bottom: 1.5rem;
	}

	.os-category {
		margin-bottom: 1.5rem;
	}

	.os-category h4 {
		font-size: 0.75rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		color: var(--color-accent);
		margin-bottom: 0.75rem;
	}

	.os-category ul {
		list-style: none;
		padding: 0;
	}

	.os-category li {
		padding: 0.5rem 0;
		display: flex;
		gap: 1rem;
		align-items: baseline;
	}

	.os-category a {
		color: var(--color-text);
		text-decoration: none;
		font-weight: 500;
	}

	.os-category a:hover {
		color: var(--color-accent);
	}

	.os-desc {
		color: var(--color-text-muted);
		font-size: 0.9rem;
	}

	@media (max-width: 768px) {
		.projects {
			padding: 3rem 1.5rem;
		}

		.app-row {
			grid-template-columns: 1fr;
			gap: 0.5rem;
		}

		.app-meta {
			justify-content: flex-start;
		}

		.os-category li {
			flex-direction: column;
			gap: 0.25rem;
		}
	}
</style>
